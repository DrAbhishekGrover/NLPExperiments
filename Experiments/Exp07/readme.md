This experiment creates a chatbot which is acting like an Ayurvedic consultant for the user. The user may query about diseases and eating habits. The chatbot will suggest ayurvedic advise. RAG is used to give a reference of a standard ayurvedic literature to the chatbot. The reponse of the chatbot is in reference to the document.

File 1: createvdb.py
1. The document which the chatbot uses for referencing should be available in vector database format. In vector database format, text is first divided into chunks, then converted to embeddings and then stored in the database. This file implements ingestion phase of RAG pipeline.

File 2: ayurvedicconsult.py
1. This file implements the chatbot and the retrieval phase of RAG pipeline.
2. Create a retriever object and LLM model object.
3. Give a system prompt that the LLM should use retrived content to give response to the user.
4. In Langchain, create a retrieval chain object. Response from LLM is obtained by calling invoke function on this object. User query and chat_history are passed as arguments. The function first converts query to embeddings. Then compares the query with chunks in vector database. The most relevant chunks (for e.g. 3) are fetched, converted to text and passed as context to LLM. The LLM reponds based on fetched content and chat_history.
5. The chat between user and AI is executed in a while loop.
