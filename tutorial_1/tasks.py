from crewai import Task
from textwrap import dedent


# TODO: YOU ARE TO FILL UP THE FOLLOWING TASK DETAILS (DESCRIPTION, EXPECTED_OUTPUT) FOR THE
#  AGENT'S PURPOSE (RESEARCH & REVIEW) FOR THE TOPIC : "What is the best way to learn a new language?"

# This is an example of how to define custom tasks.
# You can define as many tasks as you want.
# You can also define custom agents in agents.py
class CustomTasks:
    def research_task(self, agent):
        return Task(
            description=dedent(
                f"""
                
                """
            ),
            expected_output="""
            
            """,
            agent=agent,
        )

    def review_task(self, agent):
        return Task(
            description=dedent(
                f"""
            
                """
            ),
            expected_output="""
            
            """,
            agent=agent,
        )
