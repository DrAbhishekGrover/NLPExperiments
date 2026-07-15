from dotenv import load_dotenv
#from langchain_google_genai import ChatGoogleGenerativeAI
#from langchain.schema import AIMessage,HumanMessage,SystemMessage
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage
from langchain_groq import ChatGroq

load_dotenv()
#model=ChatGoogleGenerativeAI(model="gemini-2.0-flash")
model=ChatGroq(model="llama-3.1-8b-instant")
chat_history=[]#Use a lsit to store messages
system_message=SystemMessage(content="You are an ayurvedic doctor who cures patient using ayurveda. Limit your response to 50 words.")
chat_history.append(system_message)
#Chat loop
while True:
    query=input("You: ")
    if query.lower()=="exit":
        break
    chat_history.append(HumanMessage(content=query))
    result=model.invoke(chat_history)
    response=result.content
    chat_history.append(AIMessage(content=response))
    print("AI: "+response)
