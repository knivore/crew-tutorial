from crewai import Task


class CustomTasks:
    tasks_config = 'tasks.yaml'

    def research_task(self, agent):
        return Task(
            # TODO: HOW CAN I SETUP THIS TASK USING TASK'S ATTRIBUTES?

            agent=agent,
        )

    def review_task(self, agent):
        return Task(
            # TODO: HOW CAN I SETUP THIS TASK USING TASK'S ATTRIBUTES AND OUTPUT AS A FILE?

            agent=agent,
            context=[self.research_task],
            # ↑ specify which task's output should be used as context for subsequent tasks
        )
