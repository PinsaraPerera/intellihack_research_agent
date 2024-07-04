from crewai import Agent
from .llm import llms
from .tools import QuizGeneratingToolset

class QuizGeneratingAgent():
    def __init__(self, user_email, vectorstore):
        self.toolset = QuizGeneratingToolset(user_email, vectorstore)

    def questionGeneratingAgent(self):
        return Agent(
            role="MCQ Quiz Creator specialist",
            goal="Generate high-quality MCQ questions with four options each.",
            backstory=(
                """
                You are an expert in creating MCQs from a given syllabus. 
                Your task is to generate questions that are easy to moderate in difficulty, effectively assessing user knowledge.
                Focus solely on the content of the syllabus. DO NOT INCLUDE questions related to author names, publication dates, or irrelevant information.
                Use the 'search_data_from_vector_database' tool at least five times.
                """
            ),
            verbose=True,
            tools=self.toolset.tools(),
            allow_delegation=True,
            llm=llms["questionGenerator"]
        )

    def formatValidatorAgent(self):
        return Agent(
            role="MCQ Format Validator",
            goal="Ensure the generated MCQs are in valid JSON format.",
            backstory=(
                """
                You are an expert in validating and formatting MCQ outputs. 
                Your task is to ensure the questions, options, and correct answers are in the correct JSON format and adhere to the given syllabus.
                Remove any metadata or irrelevant information.
                """
            ),
            verbose=True,
            tools=self.toolset.tools(),
            allow_delegation=True,
            llm=llms["formatValidator"]
        )
