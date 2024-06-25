from AgentFramework import setupAgent, setupCrew, setupTask, model
from AgentFramework.tools import tools


def kickOff(CONFIGURATIONS: dict):
    agents = []
    for agent_config in CONFIGURATIONS["agents"]:
        model_instance = model.ModelDefine(
            model_name=agent_config["model_name"],
            temperature=agent_config["temperature"],
        )
        model_instance.define_model()
        llm = model_instance.get_model()

        # define tools
        choosed_tools = [tools[tool] for tool in agent_config["tools"]]

        # Create a new agent
        agent_instance = setupAgent.setupCrewAgent(
            name=agent_config["agent_name"],
            role=agent_config["role"],
            goal=agent_config["goal"],
            backstory=agent_config["backstory"],
            allow_delegation=agent_config["allow_delegation"],
            llm=llm,
            tools=choosed_tools,
        )

        agents.append(agent_instance.setup_agent())

    tasks = []
    for task_config in CONFIGURATIONS["tasks"]:
        agent_name = task_config["agent"]
        agent_instance = next(
            agent[agent_name] for agent in agents if agent_name in agent
        )
        task_instance = setupTask.agentTask(
            agent=agent_instance,
            description=task_config["description"],
            expected_output=task_config["expected_output"],
        )
        tasks.append(task_instance.create_task())

    list_of_agents = [agent for agent_dict in agents for agent in agent_dict.values()]

    crew_instance = setupCrew.initializeCrew(list_of_agents, tasks)

    return crew_instance.initialize_crew()


def run(setup: dict):
    crew_instance = kickOff(CONFIGURATIONS=setup)
    result = crew_instance.kickoff()
    return result


example = {
    "agents": [
        {
            "agent_name": "Agent 1",
            "model_name": "gpt-3.5-turbo",
            "temperature": 0.3,
            "role": "Senior Research Assistance",
            "goal": "Research",
            "backstory": "I am a senior research assistant at a prestigious university.",
            "allow_delegation": False,
            "tools": ["search_tool"],
        },
        {
            "agent_name": "Agent 2",
            "model_name": "gpt-3.5-turbo",
            "temperature": 0.7,
            "role": "professional Short-Article writer",
            "goal": "summarize the latest advancrments in AI chatbots in Mental Health in a concise article",
            "backstory": "I am a professional writer with a background in AI and LLM",
            "allow_delegation": True,
            "tools": [],
        },
    ],
    "tasks": [
        {
            "agent": "Agent 1",
            "description": "I need to do a research on Mental health chatbots and need the resoures",
            "expected_output": "Existing Mental health chatbots and there pros , cons and the resources links to the papers.",
        },
        {
            "agent": "Agent 2",
            "description": "I need a short article on the latest advancements in AI chatbots in Mental Health",
            "expected_output": "A concise article on the latest advancements in AI chatbots in Mental Health",
        },
    ],
}
