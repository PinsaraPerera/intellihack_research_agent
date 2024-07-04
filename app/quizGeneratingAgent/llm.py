import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llms = {
    "questionGenerator": ChatOpenAI(model_name="gpt-4o", temperature=0.7, max_tokens=1000),
    "formatValidator": ChatOpenAI(model_name="gpt-4o", temperature=0.2),
}