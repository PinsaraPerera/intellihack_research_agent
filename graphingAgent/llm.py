import os
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()
# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

llms = {
    "graphIdentifier": ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.7),
    "graphGenerator": ChatOpenAI(model_name="gpt-4o", temperature=0.2),
    # "graphValidator": ChatOpenAI(model_name="gpt-4o", temperature=0.3),
    "graphValidator": ChatOpenAI(model_name="gpt-4o", temperature=0.3),
}