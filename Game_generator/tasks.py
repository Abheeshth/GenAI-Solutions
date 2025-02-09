from crewai import Task
from textwrap import dedent

class CustomTasks:
    def architecture_task(self, agent, game_name, game_description, programming_language):
        return Task(
            description=dedent(
                f"""
                Conduct thorough research on game project architectures.
                Design a complete project folder structure that includes all necessary files.
                For each file, include a brief 2-3 line comment description explaining its purpose.
                The folder structure should be relative to the current working directory.
                try not to make so many files dont make file where user need to put images or something that should be codable in tkinter or pygame cause user will not upload anythong
                - Game Name: {game_name}
                - Game Description: {game_description}
                - Programming Language: {programming_language}
                """
            ),
            expected_output=dedent(
                """
                The output should list the full folder structure with relative file paths.
                Each file block should follow this format:

                Path: relative/path/to/filename.ext
                Code:
                '''
                # File content goes here.
                '''
                """
            ),
            agent=agent,
        )

    def coding_task(self, agent, game_name, game_description, programming_language):
        return Task(
            description=dedent(
                f"""
                Develop a complete, executable game based on the  requirements:

                
                The game code must be split into multiple files following a clear folder structure.
                Ensure that when the main file is executed, the game window appears where we can play game for designing purpose you need to wrote the code for it user will not 
                proovide you image or anything use pygame or tkinter to do that .
                here is the detail of the project
                 - Game Name: {game_name}
                - Game Description: {game_description}
                - Programming Language: {programming_language}
                """
            ),
            expected_output=dedent(
                """
                The output should include multiple file blocks. Each block must follow this format:

                Path: relative/path/to/file.ext
                Code:
                '''
                # File content goes here.
                '''
                """
            ),
            agent=agent,
            output_file="code.md",
        )
