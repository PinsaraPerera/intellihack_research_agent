from crewai import Agent
from graphingAgent.llm import llms
from graphingAgent.tools import GraphGeneratingToolset

class GraphGeneratingAgent():
    def graph_type_identify_agent(self):
        return Agent(
            role="Graph Type Identifying Specialist",
            goal="Identify the most appropriate graph type which describes the user input in the best way possible.",
            backstory=("""
            As a Graph Type Identifying Specialist, You are responsible for identifying the most suitable graph type that accurately represents the given data.
            Also you are responsible for choosing the best possible graph type from Mermaid.js supported graph types which are Mermaid Graph, Mermaid Pie Chart, Mermaid Mindmap and Mermaid XY Chart.
            You have years of experience in analyzing data and recommending the best graph type to visualize the information effectively.
            """),
            verbose=True,
            allow_delegation=False,
            llm=llms["graphIdentifier"]
        )

    def graph_code_generate_agent(self):
        return Agent(
            role="Mermaid.js supported Graph Code Generating Specialist",
            goal="Generate the relevant graph notation code for the identified graph type for the given data.",
            backstory=("""
            As a experienced Mermaid.js supported Graph Code generating Specialist, You are responsible for generate
            error-free and accurate code for the given graph type for the given data. The graph notation code must be supported by Mermaid.js.
            An expert in generating precise and syntactically correct Mermaid.js code for the identified graph type. Do not do
            any additional formatting to the code. The code must be directly rendered by Mermaid.js without any errors.
            """),
            verbose=True,
            allow_delegation=False,
            tools=GraphGeneratingToolset.tools(),
            llm=llms["graphGenerator"],
        )

    def graph_code_validate_agent(self):
        return Agent(
            role="Mermaid.js supported Graph Code Validating Specialist",
            goal="Ensure the generated Mermaid.js code is correct and renders without errors.",
            backstory=("""
            As a Graph Validator specialist you are famouse for validate and correcting the graph code to make it error-free and capable of
            rendering the graph directly from Mermaid.js. Since Mermaid.js can render the graph directly and you know that
            by wrapping the code with '''mermaid ''' keyword will not render the graph. So you are responsible for validating the code and remove
            unneccessary formattings and keywords from the code. follow the tool to specific graph syntaxes.
            """),
            verbose=True,
            allow_delegation=False,
            # tools=GraphGeneratingToolset.tools(),
            llm=llms["graphValidator"],
        )