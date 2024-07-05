import os
from dotenv import load_dotenv

load_dotenv()

# Load environment variables
SERPER_API_KEY = os.getenv("SERPER_API_KEY")
BROWSERLESS_API_KEY = os.getenv("BROWSERLESS_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

BUCKET_NAME = os.getenv("BUCKET_NAME")
DATA_FOLDER = "data"
RESOURCE_FOLDER = "resources"
VECTOR_STORE_FOLDER = "vectorStore"