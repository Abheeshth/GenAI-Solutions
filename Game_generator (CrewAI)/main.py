import os
from crewai import Crew
from textwrap import dedent


from agents import CustomAgents
from tasks import CustomTasks

# Import the parser function to process the code.md output.
from parser import parse_code_output


# os.environ["OPENAI_ORGANIZATION"] = config("OPENAI_ORGANIZATION_ID")

# Main Crew class that sets up agents and tasks.
class CustomCrew:
    def __init__(self, game_name, game_description, programming_language):
        self.game_name = game_name
        self.game_description = game_description
        self.programming_language = programming_language

    def run(self):
        # Initialize custom agents and tasks.
        agents_obj = CustomAgents()
        tasks_obj = CustomTasks()

        # Define two specialized agents:
        # - architecture_agent: Responsible for designing the folder structure.
        # - coding_agent: Responsible for generating the executable game code.
        architecture_agent = agents_obj.architecture_agent()
        coding_agent = agents_obj.coding_agent()

        # Create tasks using the agents.
        architecture_task = tasks_obj.architecture_task(architecture_agent,
            self.game_name,
            self.game_description,
            self.programming_language,)
        coding_task = tasks_obj.coding_task(
            coding_agent,
            self.game_name,
            self.game_description,
            self.programming_language
        )

        # Build and run the crew.
        crew = Crew(
            agents=[architecture_agent, coding_agent],
            tasks=[architecture_task, coding_task],
            verbose=True,
        )

        result = crew.kickoff()

        # After the crew runs, parse the generated code.md file.
        parse_code_output("code.md")

        return result


if __name__ == "__main__":
    print("## Welcome to Crew AI Game Generator")
    print("------------------------------------")
    game_name = input(dedent("Enter the game name: ")).strip()
    game_description = input(dedent("Enter a brief description of the game: ")).strip()
    programming_language = input(
        dedent("Enter the programming language (e.g., Python): ")
    ).strip()

    custom_crew = CustomCrew(game_name, game_description, programming_language)
    result = custom_crew.run()

    print("\n\n########################")
    print("## Crew Run Result:")
    print("########################\n")
    print(result)
