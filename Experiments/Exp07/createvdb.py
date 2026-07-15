#To create vector database from the given ayurvedic pdf
import os
from langchain.text_splitter import CharacterTextSplitter
#from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings

#This module creates a vector database
#Define the directory containing the text file and the persistent directory
current_dir=os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(current_dir,"books2","ayurvedicremedies.pdf")#creating file path names
#Vector database will be created in persistent directory(pd) chroma_db
pd=os.path.join(current_dir,"db","chroma_db")

#Check if chroma vector store already exists
if not os.path.exists(pd):
    print("Initializing vector store")
    #Ensure that the text file (for context) exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"The file {file_path} does not exist."
        )
    #Read the text content from file
    loader=PyPDFLoader(file_path)
    documents=loader.load()

    #Split the documents into chunks
    text_splitter=CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    #Now apply text_splitter
    docs=text_splitter.split_documents(documents)
    #These are the docs that need to be stored in vector database

    #create embeddings
    embed=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    #create vector store
    db=Chroma.from_documents(docs,embed,persist_directory=pd)
else:
    print("Vector database already exists")