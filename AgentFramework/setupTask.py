from crewai import Task

class agentTask:
    def __init__(self, agent, description: str = "", expected_output: str = ""):
        self.agent = agent
        self.description = description
        self.expected_output = expected_output

    def create_task(self):
        task = Task(
            agent=self.agent,
            description=self.description,
            expected_output=self.expected_output,
        )
        return task
