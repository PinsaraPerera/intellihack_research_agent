from crewai import Agent


class setupCrewAgent:
    def __init__(
        self,
        name: str,
        role: str,
        goal: str,
        backstory: str,
        allow_delegation: bool,
        llm: object,
        tools: list = [],
    ):
        self.name = name
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.allow_delegation = allow_delegation
        self.tools = tools
        self.llm = llm

    def setup_agent(self):
        if len(self.tools) == 0:
            agent = Agent(
                role=self.role,
                goal=self.goal,
                backstory=self.backstory,
                verbose=True,
                allow_delegation=self.allow_delegation,
                llm=self.llm,
            )
            return {self.name: agent}
        else:
            agent = Agent(
                role=self.role,
                goal=self.goal,
                backstory=self.backstory,
                verbose=True,
                allow_delegation=self.allow_delegation,
                tools=self.tools,
                llm=self.llm,
            )
            return {self.name: agent}
