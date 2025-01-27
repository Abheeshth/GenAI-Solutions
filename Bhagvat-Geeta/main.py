# import pandas as pd
# import os
# from langchain.text_splitter import CharacterTextSplitter
# from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import FAISS
# from langchain.memory import ConversationBufferMemory
# from langchain.chains import ConversationalRetrievalChain
# from langchain_openai import ChatOpenAI
# from langchain_community.document_loaders import PyPDFLoader
# from langchain_core.messages import SystemMessage
# from langchain_core.prompts import HumanMessagePromptTemplate,SystemMessagePromptTemplate,ChatPromptTemplate

# # Set your OpenAI API key
# api_key = "sk-proj-zy8GjcMAc03HW73V8i4ET3BlbkFJbpmBd4ECj0FpLQcC59YF"
# os.environ["OPENAI_API_KEY"] = api_key

# embeddings = OpenAIEmbeddings()
# vectorstore = FAISS.load_local('db_faiss', embeddings, allow_dangerous_deserialization = True)


# context = "You are krishna"
# ##########
# system_prompt = """
# You are Sri Krishna, the divine guide and charioteer. You will address the user as 'Parth' in every response. 
# Whenever Parth asks a question or presents a problem, you will start by reciting a relevant slok from the Bhagavad Gita. 
# After reciting the slok, you will explain how it relates to Parth's issue and provide guidance based on the teachings of the slok.{context}
# """



# #general_user_template = "Question:```{question}```"
# messages = [
#             SystemMessagePromptTemplate.from_template(system_prompt)
#             #HumanMessagePromptTemplate.from_template(general_user_template)
# ]
# qa_prompt = ChatPromptTemplate.from_messages( messages )


# # Set up the LLM and conversation chain
# llm = ChatOpenAI(temperature=0.7, model_name="gpt-4o")
# memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
# conversation_chain = ConversationalRetrievalChain.from_llm(
#     llm=llm,
#     chain_type="stuff",
#     retriever=vectorstore.as_retriever(),
#     memory=memory,
#     combine_docs_chain_kwargs={"prompt": qa_prompt}
# )


# # ANSI escape codes for colors
# class Colors:
#     USER_INPUT = "\033[94m"  # Blue
#     AI_OUTPUT = "\033[92m"   # Green
#     RESET = "\033[0m"        # Reset color

# # Function to run the chatbot
# def run_chatbot():
#     print("Hi Parth How are you")
#     while True:
#         query = input(f"{Colors.USER_INPUT}You: {Colors.RESET}")
#         if query.lower() in ['exit', 'quit']:
#             print("Goodbye!")
#             break
#         result = conversation_chain.invoke({"question": query})
#         answer = result.get("answer", "Sorry, I couldn't find an answer to your question.")
#         print(f"{Colors.AI_OUTPUT}Sri Krishna: {answer}{Colors.RESET}")

# # Start the chatbot
# if __name__ == "__main__":
#     run_chatbot()



import os
import chainlit as cl
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from langchain_core.prompts import HumanMessagePromptTemplate, SystemMessagePromptTemplate, ChatPromptTemplate
from api_key import api_key 

# Set your OpenAI API key
os.environ["OPENAI_API_KEY"] = api_key

# Load embeddings and vectorstore
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.load_local('db_faiss', embeddings, allow_dangerous_deserialization=True)

# Define the context and system prompt
context = "You are Krishna"
system_prompt = """
You are Sri Krishna, the divine guide and charioteer. You will address the user as 'Parth' in every response. 
Whenever Parth asks a question or presents a problem, you will start by reciting a relevant slok from the Bhagavad Gita. 
After reciting the slok, you will explain how it relates to Parth's issue and provide guidance based on the teachings of the slok. {context}
"""

messages = [
    SystemMessagePromptTemplate.from_template(system_prompt)
]

qa_prompt = ChatPromptTemplate.from_messages(messages)

# Set up the LLM and conversation chain
llm = ChatOpenAI(temperature=0.7, model_name="gpt-4o")
memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
conversation_chain = ConversationalRetrievalChain.from_llm(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(),
    memory=memory,
    combine_docs_chain_kwargs={"prompt": qa_prompt}
)

# Initialize conversation with a greeting
@cl.on_chat_start
async def start_conversation():
    await cl.Message(content=".____कान्हा❤️____.: Hi Parth, how are you?").send()

# Handle user messages
@cl.on_message
async def handle_message(message):
    query = message.content
    result = conversation_chain.invoke({"question": query})
    answer = result.get("answer", "Sorry, I couldn't find an answer to your question.")
    await cl.Message(
        content=f".____कान्हा❤️____.: {answer}"
    ).send()

# Run the Chainlit app (default on port 8000)
if __name__ == "__main__":
    cl.main()
