from crewai import Agent
from textwrap import dedent
from langchain_openai import ChatOpenAI

class CustomAgents:
    def __init__(self):
        # Use the GPT-3.5 Turbo model for both agents.
        # self.llm1 = ChatOpenAI(model_name="gpt-3.5-turbo")
        # self.llm2 = ChatOpenAI(model_name="o3-mini")
        self.llm1 = "gpt-3.5-turbo"
        self.llm2 = "o3-mini"
    def architecture_agent(self):
        return Agent(
            role="Software Architect",
            backstory=dedent(
                """
                With over 10 years of experience in software design and architecture,
                you excel at crafting efficient python project structures including requirement and other coding files utils files and whatever is needed.
                """
            ),
            goal=dedent(
                """
                Analyze game requirements and design a complete project folder structure.
                List all files with their relative paths and include brief comment descriptions for each file.
                """
            ),
            verbose=True,
            llm=self.llm1,
        )

    def coding_agent(self):
        return Agent(
            role="Senior Game Developer",
            backstory=dedent(
                """
                With over 10 years of experience in game development using Python,
                you excel at writing modular, executable game code that meets detailed specifications.
                """
            ),
            goal=dedent(
                """
                Develop a complete, executable game based on the provided requirements.
                Split the code into multiple files (e.g., main game file, requirements file, etc.)
                according to best practices.
                """
            ),
            verbose=True,
            llm=self.llm2,
        )
