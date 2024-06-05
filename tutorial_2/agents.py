from textwrap import dedent
from crewai import Agent
from langchain_openai import ChatOpenAI

# TODO: Import the WebsiteSearchTool tool from crewai_tools

class CustomAgents:
    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

    def research_agent(self):
        # TODO: Add the WebsiteSearchTool tool to the agent.
        #  Bonus Problem: Does the agent always use the tool? If not, how can you make it use the tool?
        return Agent(
            role="Research Agent",
            backstory=dedent(f"""Analyze and provide description along with insights on the topic"""),
            goal=dedent(f"""Expert in analyzing and identifying the key points and current trends on the topic and 
            provide the best possible answer to the user's question."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )

    def review_agent(self):
        return Agent(
            role="Review and Editing Agent",
            backstory=dedent(f"""A meticulous editor with an eye for detail, ensuring every piece of content is clear, 
            accurate, engaging, and grammatically perfect with sources provided and referenced."""),
            goal=dedent(f"""Expert in validating and reviewing of information and refining the topic to ensure the 
            clarity, accuracy, engagement, grammatical accuracy, and relevance to the user's question."""),
            allow_delegation=False,
            verbose=True,
            llm=self.OpenAIGPT35,
        )
