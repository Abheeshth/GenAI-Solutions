from crewai import Task
from agents import Architect_agent,Sde_agent


##task1 folder 

architecture_folder = Task(
    description="""
        You need to make the best software architeture folder for the games and best practices in game development.
        Design a complete project folder structure that includes all necessary files.
        For each file, include a 2-3 line comment description explaining its purpose.
        - Game Name: {game_name}
        - Game Description: {game_description}
        - Programming Language: {programming_language}

    """,
    expected_output="""
        The output should list the full folder structure with file paths relative to the current working directory.
        Each file block should follow the format:

        Path: relative/path/to/file.py
        # Brief description of what this file does.
    """,
    agent=Architect_agent,
    output_file="desgine.md"
)


#task 2 coding

Coding = Task(
    description="""
        Develop a complete, executable game based on the following requirements:
        The generated code must be executable; when you run the main file, a game window should appear.
        Use an appropriate library (such as pygame or tkinter) to implement the game.
        write code to there respective files and accorsdin to the description that is given under that path.
        write code for visuals as well cause do not expect from user to uplaod image or audio so only use codes for this
    """,
    expected_output="""
        The output should follow the format below:
        done not add unnneceaary comments or unncessearcy block or explanations

        Path: relative/path/to/main_game_file.py
        Code:
        '''
        # Complete executable game code goes here.
        '''
    """,
    agent=Sde_agent,
    output_file="code.md"
)



