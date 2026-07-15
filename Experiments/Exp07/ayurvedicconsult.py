#To chat with ayurvedic consultant
import os
from dotenv import load_dotenv
from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import Chroma
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_google_genai import ChatGoogleGenerativeAI,GoogleGenerativeAIEmbeddings

load_dotenv()
current_dir=os.path.dirname(os.path.abspath(__file__))
pd=os.path.join(current_dir,"db","chroma_db")
embed=GoogleGenerativeAIEmbeddings(model="models/embedding-001")
db=Chroma(persist_directory=pd,embedding_function=embed)

retriever=db.as_retriever(search_type="similarity",search_kwargs={"k":3})
model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")

cq_systemprompt=("Given a chat history and latest user question give response.")
cq_prompt=ChatPromptTemplate.from_messages(
    [
        ("system",cq_systemprompt),MessagesPlaceholder("chat_history"),("human","{input}")
    ]
)
history_aware_retriever=create_history_aware_retriever(model,retriever,cq_prompt)
qa_prompt=ChatPromptTemplate.from_messages(
    [
        ("system","Use the retrieved context to answer the questions\n\n{context}"),MessagesPlaceholder("chat_history"),("human","{input}")
        ]
        )
qa_chain=create_stuff_documents_chain(model,qa_prompt)
rag_chain=create_retrieval_chain(history_aware_retriever,qa_chain)
def mychat():
    print("Ask your queries. Type exit to end conversation.")
    chat_history=[]
    while True:
        query=input("You: ")
        if query.lower()=="exit":
            break
        result=rag_chain.invoke({"input":query,"chat_history":chat_history})
        print(f"AI:{result['answer']}")
        chat_history.append(HumanMessage(content=query))
        chat_history.append(SystemMessage(content=result["answer"]))

if __name__=="__main__":
    mychat()
