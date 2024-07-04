from langchain.agents import tool


class QuizGeneratingToolset:
    current_instance = None

    def __init__(self, user_email, vectorstore):
        self.user_email = user_email
        self.vectorstore = vectorstore
        QuizGeneratingToolset.current_instance = self

    def search_data_from_database(self, query: str):
        """Function to search the data from the vector database."""
        if self.vectorstore:
            results = self.vectorstore.search(
                query=query, search_type="similarity", k=5
            )
            if results:
                return results[0].page_content
            return ""
        return ""

    @staticmethod
    @tool
    def search_data_from_vector_database(query: str):
        """
        Function to search the data from the vector database. This database contains the full informations which need
        to be used to generate the questions. This function will return the search results based on the query.
        just try query like for search contents, topics to get the idea of the data in the database.
        """

        toolset = QuizGeneratingToolset.current_instance
        results = toolset.search_data_from_database(query)
        return results

    @staticmethod
    @tool
    def search_sample_output_format(query: str):
        """This returns a sample output format for the generated questions, options and correct answer"""
        return """
        {
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
        """

    def tools(self):
        return [
            QuizGeneratingToolset.search_data_from_vector_database,
            QuizGeneratingToolset.search_sample_output_format,
        ]
