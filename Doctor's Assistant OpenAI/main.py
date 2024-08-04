from openai import OpenAI 
from api_key import api_key
GPT_MODEL = 'gpt-4o'
client = OpenAI(
    api_key=api_key,
)

# assign a role 
initial_prompt = {
    "role": "system",
    "content": """
                1.You are helpful healthcare assitant
                2.Give home remedies to your user. 
                3.Always try to focus on his health. 
                4.Please write your answer in precise and in short way"""
}


# Handle history 

messages = [initial_prompt]

## ANSI escape codes for coloring
green = '\033[92m'
red = '\033[91m'
reset = '\033[0m'



# Function to handle user inputs and AI responses
def handle_response(user_input):
    global messages
    messages.append({"role": "user", "content": user_input})
    
    response = client.chat.completions.create(
        model=GPT_MODEL, 
        messages=messages,
    )

    response_message = response.choices[0].message 
    messages.append(response_message)

    print(f"{green}AI: {response_message.content}{reset}")

# intial question

print(f"{green}AI: Hello! I can help you if you want any home remedies to improve your health . Can you please tell me what symptoms you're experiencing?{reset}")


# the flow of conversation 

while True:
    user_input = input("You: ")
    
    if user_input.lower() in ['exit', 'quit']:
        print("Ending conversation.")
        break
    
    handle_response(user_input)
