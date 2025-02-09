from crewai import Crew,Process
from tasks import architecture_folder,Coding
from agents import Architect_agent,Sde_agent
from parser import parse


game_name = input('Enter the game name: ').strip()
game_description = input("enter a brief discription of the game: ").strip()
programming_language = input("enter the programming language: ").strip()


architecture_folder.description = architecture_folder.description.format(
    game_name = game_name,
    game_description = game_description,
    programming_language = programming_language
)



crew =Crew(
    agents= [Architect_agent,Sde_agent],
    tasks = [architecture_folder,Coding],
    Process = Process.sequential,
    verbose = True 
)


crew_output = crew.kickoff()

# display the ooutput
print(f"raw output: {crew_output.raw}")


try :
    parse("code.md")
except Exception as e:
    print(f"Error during parsing : {e}")

    




