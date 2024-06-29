from crewai import Task


class QuizGeneratingTask:
    def __init__(self):
        self.format = {
            "questions": [
                {
                    "question": "qeustion1",
                    "options": ["ans1", "ans2", "ans3", "ans4"],
                    "correct": "correct answer",
                },
                {
                    "question": "qeustion2",
                    "options": ["ans1", "ans2", "ans3", "ans4"],
                    "correct": "correct answer",
                },
            ]
        }

    def generate_quizes(self, number_of_questions, agent):
        return Task(
            description=(
                f"""
            Generate {number_of_questions} multiple-choice questions (MCQs) with four options each. 
            The questions should cover the entire content of our database, adhering strictly to the given syllabus. 
            Ensure the questions are simple, easy to understand, and derived from the syllabus using the provided tool.
            Only generate valid questions that are relevant to the syllabus.

            number_of_questions: {number_of_questions} needed to be generated.
            """
            ),
            expected_output=(
                f"""
            Quesions , options and correct answer should be generated as valid JSON format. The format is given below:

            format: {self.format}
            """
            ),
            agent=agent,
            async_execution=False,
        )

    def format_output(self, agent):
        return Task(
            description=(
                f"""
            Make sure the quesions generated are relevant to the syllabus. Do not include any metadata of the documents,
            author details, publication dates, etc. Only focus on the content of the syllabus. Don't create same type of
            questions again and again. Make sure the questions are unique and meaningful. Use the provided tool to generate
            questions and validate the output.
            Validate and format the generated MCQ output to ensure it is in valid JSON format.
            The format is as follows:
            format: {self.format}
            """
            ),
            expected_output=(
                f"""
            A well-formatted JSON output as specified.
            """
            ),
            agent=agent,
            async_execution=False,
        )
