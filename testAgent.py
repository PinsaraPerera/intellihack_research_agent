import os
import logging
from crewai import Agent, Task, Process, Crew
from langchain_openai import ChatOpenAI
from langchain.agents import Tool
from app.core.createVectorDB import search_vector_db
from logging_config import logger

# Load OpenAI API key from environment variable
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def search_data_from_vector_db(query: str):
    """Function to search data from vector database."""
    try:
        results = search_vector_db(query)
        return results
    except Exception as e:
        logger.error(f"Error searching vector DB: {e}")
        return []

def get_input():
    """Function to get user input text for graph data."""
    return "In a school there are 80% boys and 20% girls."

def generate_graph_code(graph_type: str):
    """Function to generate graph code based on the graph type and data."""
    if graph_type == "pie chart":
        return f"pie title Students in a School\n    \"Boys\" : 80%\n    \"Girls\" : 20%"
    elif graph_type == "flowchart":
        return f"graph TD\n    A[Students in a School] -->|Boys| B(80%)\n    A -->|Girls| C(20%)"

# Define tools
search_data_tool = Tool(
    name="searchDataFromVectorDB",
    func=search_data_from_vector_db,
    description="Searches for graph syntax in the vector database based on the graph type.",
)

get_input_tool = Tool(
    name="userInput",
    func=get_input,
    description="Takes user input text for the graph data.",
)

generate_graph_code_tool = Tool(
    name="generateGraphCode",
    func=generate_graph_code,
    description="Generates graph code based on the graph type and user input data.",
)

# Initialize LLMs
llm_graphIdentifier = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.7)
llm_graphGenerator = ChatOpenAI(api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo", temperature=0.3)

# Define Agents
graphTypeIdentifier = Agent(
    role="Graph Type Identifier",
    goal="Identify the most appropriate graph type for the given data.",
    backstory=(
        "This agent is designed to identify the most suitable graph type for visualizing the given data using Mermaid.js. "
        "The supported graph types include flowchart, sequence diagram, class diagram, state diagram, entity relationship diagram, "
        "Mermaid Graph, Mermaid Pie Chart, Mermaid Mindmap, Mermaid XY Chart"
        "The agent analyzes the data and selects the best graph type to clearly and effectively represent the information."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm_graphIdentifier
)

graphCodeGenerator = Agent(
    role="Graph Code Generator",
    goal="Generate accurate and error-free code for the identified graph type using Mermaid.js.",
    backstory=(
        "This agent specializes in generating precise and syntactically correct Mermaid.js code for the identified graph type. "
        "It leverages graph examples and user input data to produce code that can be directly rendered by Mermaid.js without any errors."
    ),
    verbose=True,
    allow_delegation=False,
    tools=[search_data_tool],
    llm=llm_graphGenerator
)

graphCodeValidator = Agent(
    role="Graph Code Validator",
    goal="Ensure the generated Mermaid.js code is correct and renders without errors.",
    backstory=(
        "This agent is tasked with validating the generated Mermaid.js code. "
        "It checks the code for correctness, ensures it is error-free, and verifies that it can be rendered directly by Mermaid.js. "
        "If any issues are found, the agent generates new, corrected code. The output is only the diagram source code in a format compatible with Mermaid.js."
    ),
    verbose=True,
    allow_delegation=False,
    llm=llm_graphGenerator
)

# Define Tasks
task_graphTypeIdentifier = Task(
    description="Identify the best possible graph type for the given data.",
    agent=graphTypeIdentifier,
    expected_output="The best possible graph type for the given data chosen from Mermaid.js supported graph types."
)

task_graphCodeGenerator = Task(
    description="Using the identified graph type and the search result from vectorDB, generate the relevant graph notation code.",
    agent=graphCodeGenerator,
    expected_output="The code for the identified graph type which supports Mermaid.js."
)

task_graphCodeValidator = Task(
    description="Validate that the generated code is correct and error-free, and capable of rendering the graph directly from Mermaid.js.",
    agent=graphCodeValidator,
    expected_output="The code is correct and error-free, capable of rendering the graph directly from Mermaid.js. Check the syntax again if not correct."
)

# Define Crew
crew = Crew(
    agents=[graphTypeIdentifier, graphCodeGenerator, graphCodeValidator],
    tasks=[task_graphTypeIdentifier, task_graphCodeGenerator, task_graphCodeValidator],
    verbose=2,
    process=Process.sequential
)

if __name__ == "__main__":
    try:
        user_input = {"userInput": '''In a school there are 80% boys and 20% girls.'''}
        result = crew.kickoff(inputs=user_input)
        print("######################################")
        print(result)
    except Exception as e:
        logger.error(f"Error during crew execution: {e}")
