from crewai import Task
from textwrap import dedent


class CustomTasks:
    def research_task(self, topic, agent):
        return Task(
            description=dedent(
                f"""
                Analyze the topic : "{topic}". Focus on research and provide insights that are relevant 
                to the topic. Use various sources to gather information and compile a detailed report 
                with key points and recommendations.
                """
            ),
            expected_output="""A detailed report on the topic with key points, insights, and recommendations. 
            Sources provided and referenced.""",
            agent=agent,
        )

    def review_task(self, topic, agent):
        return Task(
            description=dedent(
                f"""
                Review the topic : "{topic}". Check for clarity, engagement, grammatical accuracy, and relevance. 
                Edit and refine the content, ensuring it aligns with the user's question and provides accurate 
                information. Ensure sources are provided and referenced.
                """
            ),
            expected_output="""A refined and edited content on the topic with clarity, engagement, grammatical 
            accuracy and relevance. Sources provided and referenced.""",
            agent=agent,
            context=[self.research_task],
            # ↑ specify which task's output should be used as context for subsequent tasks
        )
