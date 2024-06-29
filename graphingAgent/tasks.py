from crewai import Task

class GraphGeneratingTask():
    def decide_graph_type_task(self, agent, user_input):
        return Task(
            description=(f"""
            Need to do a analysis on the user input given below to decide the best graph type which describes
            the user input in the best way possible. Best possible graphs are chosen from Mermaid.js supported graph types.
            which are Mermaid Graph, Mermaid Pie Chart, Mermaid Mindmap and Mermaid XY Chart. Among these
            graphs, need to choose the best graph that interprets the user information accurately.

            user input: {user_input}
            """),
            expected_output=(f"""
            The best possible graph type name for the given data chosen from Mermaid.js supported graph types. 
            output template: 
            "graph_type": "graph_name" only
            """),
            agent=agent,
            async_execution=False
        )

    def generate_graph_code_task(self, agent, user_input):
        return Task(
            description=(f"""
            Need to generate the relevant graph notation code for the given graph type for the given user input.
            The graph notation code must be supported by Mermaid.js. The graph must reflects all the important information
            from the user input. User input are given below. Graph Type is given from the previous task output.

            user input: {user_input}
            """),
            expected_output=(f"""
            The accurate code(syntax) for the identified graph type to the given scenario which supports Mermaid.js. 
            output template:
            "graph_code": "graph_code" only
            """),
            agent=agent,
            async_execution=False
        )

    
    def validate_graph_code_task(self, agent):
        return Task(
            description=(f"""
            Need to validate the generated code is correct and error-free, and capable of rendering the graph directly from Mermaid.js.
            The code must be syntactically correct and error-free. If any issues are found, the agent generates new, corrected code.
            The output is only the diagram source code in a format compatible with Mermaid.js. The code is given below. Output must not 
            wrapped with '''mermaid ''' keyword. only graph notation should be there. if below graph code wrapped with '''mermaid ''' keyword
            first remove it and validate the code. Output must be a valid string of graph code. Don't wrapped the answer by ``` ```.
            """),
            expected_output=(f"""
            The code is correct and error-free, capable of rendering the graph directly from Mermaid.js. Check the syntax again if not correct.
            output template: only graph code. 
            """),
            agent=agent,
            async_execution=False
        )
    