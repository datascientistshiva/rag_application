**To run the application, follow below steps**
- Install python in your pc or laptop.
- Clone the application to your local environment
  - **git clone https://github.com/datascientistshiva/rag_application.git**
- **cd rag_application/**
- Create a virtual environment
  - **python -m venv /venv-name** or **python3 -m venv /venv-name**
- To install all the library from requirements.txt file.
  - **pip install -r requirements.txt**
- To run the python application.
  - **python app.py**


**About the application**
***Structure of the application***
1. **requirements.txt**
    - **langchain** : ***Framework used to develop and manage LLM application***
    - **langchain-community** : ***Community of langchain***
    - **PyPDF2** : ***For the pdf loading and processing***
    - **faiss-cpu** : ***Vector store database***

2. **app.py**
    - This is the main python file which is responsible to run our rag application.
    - Here all other functions are called in series of steps, functions are from _document_loader_01, _document_splitter_02, _vector_stores_03 and _prompt_and_chains_04.
    - ***Workflows***
      - Load the document using PyPDFLoader.
      - Spit the document using RecursiceCharacterTextSplitter with chunk_size = 1000 and chunk_overlap = 200 .
      - Create the vector embedding from OllamaEmbedding.
      - Store or load the vector in FIASS vector db.
      - Create document_chain and retriever_chain.
      - Finally, Retriever chain will fetch the embedding which are very similar to user input from the vector db and take that data as a context to LLM which can generate highly accurate information about the document.
      - We can ask about anything from the documents and this application will give you the response.
    
3. **_document_loader_01.py**
    - This file is responsible for loading the document according to our need.
    - Here only PyPDF2 is used for pdf purpose.
    - Document is loaded using PyPDFLoader(pdf_path)

4. **_document_splitter_02.py**
    - This file is respolsible for splitting the document into various chunks
    - In this application chunk_size = 1000 and chunk_overlap = 200.
    - RecursiveCharacterTextSplitter() is used for splitting the documents to gain more meaning of the words.

5. **_vector_stores_03.py**
   - This file is responsible for creating the vector embedding.
   - If vector db already exist then load the vector_db else create the new vector db and store it into drive.
   - Similarity search with vector embedding is also available.
   
6. **_prompt_and_chains_04.py**
   - This application is used for creating and managing prompt template.
   - Created document_chain with the use of **create_stuff_documents_chain(llm, prompt)**
   - Created retriever_chain with the help of document_chain and vector retriever.
   - ***prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context. 
Think step by step before providing a detailed answer. 
I will tip you $1000 if the user finds the answer helpful. 
<context>
{context}
</context>
Question: {input}""")***
   

