from crewai import Agent
from langchain_openai import ChatOpenAI


class CustomAgents:
    agents_config = 'agents.yaml'

    def __init__(self):
        self.OpenAIGPT35 = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0.5)

    def research_agent(self):
        return Agent(
            ## TODO: HOW CAN I SETUP THIS AGENT USING AGENT'S ATTRIBUTES?

            llm=self.OpenAIGPT35,
        )

    def review_agent(self):
        return Agent(
            ## TODO: HOW CAN I SETUP THIS AGENT TO ITERATE MORE TO GET THE BEST ANSWER?

            llm=self.OpenAIGPT35,
        )
