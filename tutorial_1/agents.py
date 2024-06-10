from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI


# TODO: YOU ARE TO FILL UP THE FOLLOWING AGENT DETAILS (ROLE, BACKSTORY, GOAL)
#  FOCUSING ON THE AGENT'S PURPOSE (RESEARCH & REVIEW) FOR THE TOPIC : "What is the best way to learn a new language?"


# This is an example of how to define custom agents.
# You can define as many agents as you want.
# You can also define custom tasks in tasks.py
class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

    def research_agent(self):
        return Agent(
            # TODO: WRITE YOUR 1ST AGENT ROLE, BACKSTORY & GOAL HERE
            role="Define agent 1 role here",
            backstory=dedent(f"""Define agent 1 backstory here"""),
            goal=dedent(f"""Define agent 1 goal here"""),
            allow_delegation=False,
            verbose=True,
            # ↑ Whether the agent execution should be in verbose mode
            llm=self.OpenAIGPT35,
        )

    def review_agent(self):
        return Agent(
            # TODO: WRITE YOUR 2ND AGENT ROLE, BACKSTORY & GOAL HERE
            role="Define agent 2 role here",
            backstory=dedent(f"""Define agent 2 backstory here"""),
            goal=dedent(f"""Define agent 2 goal here"""),
            allow_delegation=False,
            verbose=True,
            # ↑ Whether the agent execution should be in verbose mode
            llm=self.OpenAIGPT35,
        )
