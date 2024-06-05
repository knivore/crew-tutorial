from textwrap import dedent

from crewai import Crew
from langchain_community.tools import DuckDuckGoSearchRun

from agents import CustomAgents
from tasks import CustomTasks


class CustomCrew:
    def __init__(self, question):
        self.question = question

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        research_agent = agents.research_agent()
        review_agent = agents.review_agent()

        # Custom tasks include agent name and variables as input
        research_task = tasks.research_task(question, research_agent)
        review_task = tasks.review_task(question, review_agent)

        # Define your custom crew here
        crew = Crew(
            agents=[research_agent, review_agent],
            tasks=[research_task, review_task],
            verbose=True,
        )

        result = crew.kickoff()
        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Tutorial 2")
    print("-------------------------------")
    question = input(dedent("""What's your question?: """))

    custom_crew = CustomCrew(question)
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
