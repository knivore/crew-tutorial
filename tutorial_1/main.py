from crewai import Crew
from agents import CustomAgents
from tasks import CustomTasks


# This is the main class that you will use to define your custom crew.
# You can define as many agents and tasks as you want in agents.py and tasks.py


class CustomCrew:
    def __init__(self):
        pass

    def run(self):
        # Define your custom agents and tasks in agents.py and tasks.py
        agents = CustomAgents()
        tasks = CustomTasks()

        # Define your custom agents and tasks here
        research_agent = agents.research_agent()
        review_agent = agents.review_agent()

        # Custom tasks include agent name and variables as input
        research_task = tasks.research_task(research_agent)
        review_task = tasks.review_task(review_agent)

        # TODO: Define your custom crew here & kickoff the crew

        return result


# This is the main function that you will use to run your custom crew.
if __name__ == "__main__":
    print("## Welcome to Crew AI Tutorial 1")
    print("-------------------------------")
    custom_crew = CustomCrew()
    result = custom_crew.run()
    print("\n\n########################")
    print("## Here is you custom crew run result:")
    print("########################\n")
    print(result)
