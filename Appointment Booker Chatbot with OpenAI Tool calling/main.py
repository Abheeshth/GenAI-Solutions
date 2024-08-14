from openai import OpenAI 
from api_key import api_key
from details import get_doctor_availability,get_doctors,tool
import json

GPT_MODEL = 'gpt-4o'



# openapi client 
client = OpenAI(api_key = api_key)

# define role 
initial_prompt = {'role':"system",
                  "content":"""
                                1. You are a helpful assistant designed to book appointments with doctors
                                2. You need to take all info that is relevant to booking
                                3. Ask about their symptoms and preferred doctors and availabity 
                                4. Give them appointment details in a reciept form 
                                5. Answer in in precise manner dont give long answers or questions
                                6. do not send any irrelevant info cause health care is a serious topic dont generate names of deaseas and doctors by your own 

"""}

##handle history 
messages = [initial_prompt]

#color
green = '\033[92m'
red = '\033[91m'
reset = '\033[0m'


#function user input and Ai response 




def handle_response(user_input):
    global messages
    messages.append({'role':'user', "content":user_input})

    response = client.chat.completions.create(
        model = GPT_MODEL,
        messages = messages,
        tools = tool,
        tool_choice="auto")
    
    response_message = response.choices[0].message
    messages.append(response_message)
    print(f'{green}AI: {response_message.content}{reset}')
    #print(response_message)

# tool functionality 
    tool_calls = response_message.tool_calls
    if tool_calls:
        for tool_call in tool_calls:
            tool_call_id = tool_call.id 
            tool_function_name = tool_call.function.name 
            tool_query  = json.loads(tool_call.function.arguments)
            Q = True

            if tool_function_name == 'get_doctors':
                results  = get_doctors(tool_query['query'])
            elif tool_function_name == 'get_doctor_availability':
                results = get_doctor_availability(tool_query['doctor_name'])
            else:
                results = 'error'
                Q = False
            
            if Q:
                messages.append({
                    "role": "tool", 
                    "tool_call_id": tool_call_id, 
                    "name": tool_function_name, 
                    "content": results
                })
            else: 
                print(f"Error: function {tool_function_name} does not exist")

        model_response_with_function_call = client.chat.completions.create(
            model=GPT_MODEL,
            messages=messages,
        )

        messages.append(model_response_with_function_call.choices[0].message)
        print(f"{green}AI: {model_response_with_function_call.choices[0].message.content}{reset}")






#intial question

print(f"{green}AI: Hello! I can help you book an appointment with a doctor. Can you please tell me what symptoms you're experiencing?{reset}")

# the flow of converation

while True:
    user_input = input('YOU: ')
    handle_response(user_input) 



