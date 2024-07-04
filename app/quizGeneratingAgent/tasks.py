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
            Cover the entire content of our database according to the syllabus. Ensure questions are simple, easy to understand, and derived strictly from the syllabus.

            Constraints:
            1. Number of questions must be {number_of_questions}.
            2. Use the 'search_data_from_vector_database' tool at least 5 times with different queries.
            3. First search for topics. And then search for each topic to create questions.
            3. Check the validity of response.
            4. DO NOT USE METADATA, AUTHOR DETAILS, PUBLICATIONS DETAILS OR ANY OTHER IRRELEVANT DETAILS TO CREATE QUESTIONS.
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
            Ensure the questions are unique and meaningful. Use the provided tool to generate and validate the MCQs.
            Validate and format the output to ensure it is a valid JSON object. Adhere strictly to the following format:
            Do not wrapped the output with ```json ``` and also do not use ``` anywhere. Strickly follow the below format only.
            All properties must enclosed in double quotes.

            format: {self.format}
            """
            ),
            expected_output=(
                f"""
            A well-formatted JSON output as specified. All the properties must be enclosed in double quotes.
            """
            ),
            agent=agent,
            async_execution=False,
        )
