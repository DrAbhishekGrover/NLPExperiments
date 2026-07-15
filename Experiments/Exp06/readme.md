This experiment implements a chatbot using APIs. Prompt Engineering is used to give role to the chatbot. All messages exchanged between user and
and chatbot are stored in a list chat_history so that the chatbot knows the entire context of the conversation. Every time the API is used to get
response from LLM, chat_history is passed as a parameter in API call.
