from langchain.agents import tool
from app.core.createVectorDB import search_vector_db

class GraphGeneratingToolset():
    @tool
    def graph_syntax_search_tool(query: str):
        """
        Function to search graph syntax in the vector database based on the query.
        This includes most recent and accurate graph syntaxes for the given query.
        
        inputs: 
            query: str: Query to search in the vector database.(based on the graph type)

        outputs:
            results: str: sample graph syntaxes for the given query.
        """

        results = search_vector_db(query)
        return results


    def tools():
        return [
            GraphGeneratingToolset.graph_syntax_search_tool,
        ]