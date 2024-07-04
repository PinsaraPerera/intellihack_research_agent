from graphingAgent.agents import GraphGeneratingAgent
from graphingAgent.tasks import GraphGeneratingTask
from crewai import Crew


def main(user_input: str):
    # Create the GraphGeneratingAgent
    agents = GraphGeneratingAgent()

    # Create the GraphGeneratingTask
    tasks = GraphGeneratingTask()

    # create agents
    graph_identifying_agent = agents.graph_type_identify_agent()
    graph_code_generating_agent = agents.graph_code_generate_agent()
    graph_code_validating_agent = agents.graph_code_validate_agent()

    # create tasks
    decide_graph_type_task = tasks.decide_graph_type_task(agent=graph_identifying_agent, user_input=user_input)
    generate_graph_code_task = tasks.generate_graph_code_task(agent=graph_code_generating_agent, user_input=user_input)
    validate_graph_code_task = tasks.validate_graph_code_task(agent=graph_code_validating_agent)

    generate_graph_code_task.context = [decide_graph_type_task]
    validate_graph_code_task.context = [generate_graph_code_task]
    # Define the Crew
    crew = Crew(
        agents = [graph_identifying_agent, graph_code_generating_agent, graph_code_validating_agent],
        tasks = [decide_graph_type_task, generate_graph_code_task, validate_graph_code_task],
        verbose=2,
    )
    
    # Execute the Crew
    result = crew.kickoff()

    print("######################################")
    print(result)
    return result

# if __name__ == "__main__":
#     user_input = input("Enter user input: ")
#     main(user_input=user_input)
