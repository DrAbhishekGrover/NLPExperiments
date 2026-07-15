This experiment implements a chatbot using APIs. Prompt Engineering is used to give role to the chatbot. All messages exchanged between user and chatbot are stored in a list chat_history so that the chatbot knows the entire context of the conversation. Every time the API is used to get response from LLM, chat_history is passed as a parameter in API call.

1. Import necessary libraries from dotenv and langchain. API keys for accessing LLM is usually stored in .env file. The function load_dotenv is used to load API keys. Libraries and functions from Langchain help in seamless and robust integration of LLM in developer applications.
2. Create a model object. You may choose any LLM.
3. Create a list chat_history. All messages exchanged between user andand chatbot are stored in a list chat_history so that the chatbot knows the entire context of the conversation.
4. In chat_history, prompts from developer are appended as a system message. Messages from user are appended as HumanMessage and Messages from LLM are appended as AIMessage.
5. Every time the API is used to get response from LLM, chat_history is passed as a parameter in API call. The characterization (SystemMessage, HumanMessage and AIMessage) done in step 4 helps the LLM to understand context everytime it is called. 
