

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
