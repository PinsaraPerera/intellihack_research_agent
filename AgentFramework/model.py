from langchain_openai import ChatOpenAI
from .config import OPEN_AI_API_KEY

class ModelDefine:
    def __init__(self, model_name: str = "gpt-3.5-turbo", temperature: float = 0.3):
        self.model_name = model_name
        self.temperature = temperature
        self.llm = None

    def define_model(self):
        self.llm = ChatOpenAI(
            api_key=OPEN_AI_API_KEY,
            model_name=self.model_name,
            temperature=self.temperature,
        )

    def get_model(self):
        return self.llm
