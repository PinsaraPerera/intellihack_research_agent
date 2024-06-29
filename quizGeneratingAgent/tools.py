from langchain.agents import tool
from .createVectorDB import search_vector_db

class QuizGeneratingToolset():
    @tool
    def search_data_from_vector_database(query: str):
        """
        Function to search the data from the vector database. This database contains the full informations which need
        to be used to generate the questions. This function will return the search results based on the query.
        just try query like for search contents, topics to get the idea of the data in the database.
        """

        results = search_vector_db(query)
        return results

    @tool
    def search_sample_output_format(query: str):
        """This returns a sample output format for the generated questions, options and correct answer"""
        return {
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


    def tools():
        return [
            QuizGeneratingToolset.search_data_from_vector_database,
            QuizGeneratingToolset.search_sample_output_format
        ]