
from langchain_text_splitters import CharacterTextSplitter
import os
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
#from langchain.memory import ConversationBufferMemory
#from langchain.chains import ConversationalRetrievalChain
#from langchain_openai import ChatOpenAI
#from langchain_community.document_loaders import PyPDFLoader
# pip install -qU 
# pip install -qU langchain_community faiss-cpu
# pip install 

# odfpy
# langchain-text-splitters
# langchain_community faiss-cpu
# langchain-core
# langchain-openai


with open("output.txt") as f:
    state_of_the_union = f.read()









text_splitter = CharacterTextSplitter(
    separator="\n\n",
    chunk_size=1000,
    chunk_overlap=200,
    length_function=len,
    is_separator_regex=False
)
texts = text_splitter.create_documents([state_of_the_union])
print(texts[0])
print(len(texts))


# Set your OpenAI API key
api_key = "sk-proj-zy8GjcMAc03HW73V8i4ET3BlbkFJbpmBd4ECj0FpLQcC59YF"
os.environ["OPENAI_API_KEY"] = api_key

db_faiss_path = os.path.join('db_faiss')

# Create the directories
os.makedirs(db_faiss_path, exist_ok=True)
# Verify directory creation
os.path.exists(db_faiss_path)
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(texts, embedding=embeddings)
vectorstore.save_local(db_faiss_path)
