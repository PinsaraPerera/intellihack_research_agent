from crewai import Crew

class initializeCrew:
    def __init__(self, agents: list, tasks: list):
        self.agents = agents
        self.tasks = tasks

    def initialize_crew(self):
        crew = Crew(
            agents=self.agents,
            tasks=self.tasks,
            verbose=2
        )
        return crew
