from crewai import Agent
from quizGeneratingAgent.llm import llms
from quizGeneratingAgent.tools import QuizGeneratingToolset

class QuizGeneratingAgent():
    def questionGeneratingAgent(self):
        return Agent(
            role="MCQ Quiz Creator",
            goal="Generate high-quality MCQ questions with four options each.",
            backstory=(
                """
                You are an expert in creating MCQs from a given syllabus. 
                Your task is to generate questions that are easy to moderate in difficulty, effectively assessing user knowledge.
                Create meaningful questions only. Do not include any questions related to author names, publication dates, or similar irrelevant information.
                Only forcus on the content of the syllabus. Use tool again and again to generate questions.
                """
            ),
            verbose=True,
            tools=QuizGeneratingToolset.tools(),
            allow_delegation=False,
            llm=llms["questionGenerator"]
        )

    def formatValidatorAgent(self):
        return Agent(
            role="MCQ Format Validator",
            goal="Ensure the generated MCQs are in valid JSON format.",
            backstory=(
                """
                You are an expert in validating and formatting MCQ outputs. 
                Your task is to ensure the questions, options, and correct answers are in the correct JSON format and 
                adhere to the given syllabus. Validate the generated MCQs and ensure they are free from any metadata or irrelevant information.
                """
            ),
            verbose=True,
            tools=QuizGeneratingToolset.tools(),
            allow_delegation=True,
            llm=llms["formatValidator"]
        )
