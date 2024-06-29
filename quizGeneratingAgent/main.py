from quizGeneratingAgent.agents import QuizGeneratingAgent
from quizGeneratingAgent.tasks import QuizGeneratingTask
from crewai import Crew

def main(no_of_questions: int):
    agents = QuizGeneratingAgent()
    tasks = QuizGeneratingTask()

    # create agents
    questionGeneratingAgent = agents.questionGeneratingAgent()
    formatValidatorAgent = agents.formatValidatorAgent()

    # create tasks
    generate_quizes = tasks.generate_quizes(number_of_questions=no_of_questions, agent=questionGeneratingAgent)
    format_output = tasks.format_output(agent=formatValidatorAgent)

    format_output.context = [generate_quizes]

    # create crew
    crew = Crew(
        agents=[questionGeneratingAgent, formatValidatorAgent],
        tasks=[generate_quizes, format_output],
        verbose=2,
    )

    # execute crew
    result = crew.kickoff()

    print("####################################")
    print(result)

# if __name__ == "__main__":
#     main(no_of_questions=5)