---

# Healthcare Assistant Chatbot

This project is a healthcare assistant chatbot that provides home remedies and health advice using OpenAI's GPT-4 model. The chatbot is designed to be a helpful healthcare assistant, offering concise and precise responses focused on the user's health.

## Features
- Provides home remedies based on user input
- Focuses on user health with short and precise answers
- Continuous conversation handling
- Simple and user-friendly interface with color-coded responses

## Prerequisites
- Python 3.x
- OpenAI library (`openai`)
- API key from OpenAI

## Installation

1. Clone this repository:
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required libraries:
    ```bash
    pip install openai
    ```

3. Create a file named `api_key.py` in the project directory and add your OpenAI API key:
    ```python
    api_key = 'your-openai-api-key'
    ```

## Usage

1. Import necessary modules and initialize the OpenAI client with your API key:
    ```python
    from openai import OpenAI
    from api_key import api_key

    GPT_MODEL = 'gpt-4o'
    client = OpenAI(api_key=api_key)
    ```

2. Define the initial prompt for the chatbot:
    ```python
    initial_prompt = {
        "role": "system",
        "content": """
                    1. You are a helpful healthcare assistant.
                    2. Give home remedies to your user.
                    3. Always try to focus on their health.
                    4. Please write your answers in a precise and short way.
                    """
    }
    ```

3. Initialize the message history:
    ```python
    messages = [initial_prompt]
    ```

4. Set ANSI escape codes for coloring the responses:
    ```python
    green = '\033[92m'
    red = '\033[91m'
    reset = '\033[0m'
    ```

5. Define the function to handle user inputs and AI responses:
    ```python
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
    ```

6. Start the initial conversation:
    ```python
    print(f"{green}AI: Hello! I can help you if you want any home remedies to improve your health. Can you please tell me what symptoms you're experiencing?{reset}")
    ```

7. Run the conversation loop:
    ```python
    while True:
        user_input = input("You: ")

        if user_input.lower() in ['exit', 'quit']:
            print("Ending conversation.")
            break

        handle_response(user_input)
    ```

## Example

```bash
python main.py
```

The chatbot will greet you and ask for your symptoms. You can then input your symptoms and receive home remedy advice. Type `exit` or `quit` to end the conversation.

## License
This project is licensed under the MIT License.

