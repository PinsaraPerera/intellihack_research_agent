import os
from langchain.text_splitter import RecursiveCharacterTextSplitter
from google.cloud import storage
from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from pathlib import Path
from dotenv import load_dotenv
import tempfile

load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

DB_FAISS_PATH = Path("vectorstores", "db_faiss")
DATA_PATH = Path("data")


# create vector database
def create_vector_db():
    # Load the data
    loader = DirectoryLoader(DATA_PATH, glob="*.pdf", loader_cls=PyPDFLoader)
    documents = loader.load()
    # Split the data
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    texts = splitter.split_documents(documents)
    # Load the embeddings
    embeddings = OpenAIEmbeddings()
    # Create the vector store
    vectorstore = FAISS.from_documents(texts, embeddings)
    # Ingest the data
    vectorstore.save_local(DB_FAISS_PATH)


# load vector database
def load_vector_db():
    vectorstore = FAISS.load_local(DB_FAISS_PATH, embeddings=OpenAIEmbeddings(), allow_dangerous_deserialization=True)
    return vectorstore

vectorstore = load_vector_db()

# search data from vector database
def search_vector_db(query: str):
    results = vectorstore.search(query=query,search_type="similarity", k=2)
    return results

# Optional: add feedback mechanism for continuous improvement
def update_vector_db(new_data):
    global vectorstore
    vectorstore.add(new_data)
    vectorstore.save_local(DB_FAISS_PATH)


# if __name__ == "__main__":
#     create_vector_db()
