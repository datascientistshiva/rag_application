import pickle
import os
from langchain.vectorstores.faiss import FAISS
from langchain.embeddings.ollama import OllamaEmbeddings

def create_or_load_vector_stores_db(db_path, documents):
    if os.path.exists(db_path):
        vector_db = load_vector_stores(db_path)
    else:
        vector_db = create_vector_stores(documents)
    return vector_db


def create_vector_stores(documents):
    vector_db = FAISS.from_documents(documents=documents, embedding=OllamaEmbeddings())
    dump_vector_stores(vector_db)
    return vector_db

def dump_vector_stores(vector_db_file_path,vector_embedding_data):
    with open(vector_db_file_path, "wb") as f:
        pickle.dump(vector_embedding_data, f)
    print("FAISS vector store saved to a binary file.")
    

def load_vector_stores(vector_db_file_path):
    # If the file exists, load the data
    with open(vector_db_file_path, "rb") as f:
        faiss_document = pickle.load(f)      
    print("FAISS vector data loaded successfully from file.")
    return faiss_document

def vector_similarity_search(vector_db_file_path,query):
    if os.path.exists(vector_db_file_path):
        vector_db = load_vector_stores()
    else:
        vector_db = create_vector_stores()
    result = vector_db.similarity_search(query)
    answer = result[0].page_content
    print(f"Result of the {query} is :: ", result[0].page_content)   
    return answer




