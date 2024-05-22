from _document_loader_01 import pdf_loader
from _document_splitter_02 import our_text_splitter
from _vector_stores_03 import create_or_load_vector_stores_db
from _prompt_and_chains_04 import retriever_chain
from langchain_community.llms.ollama import Ollama

# Path for the document
pdf_path = "dataset/Attention.pdf"
# Path to store or load the vector db.
vector_db_file_path = "database/FIASS_data/faiss_vectorstore.bin"
# Ollama LLM from langchain 
llm = Ollama(model="llama2")

# Loading the document
print("1. document loading function started.")
splitted_data = pdf_loader(pdf_path) # Loading the pdf document from the function of _document_loader_01 file.


# Splitting the document.
# print("2. document splitting function started.")
# splitted_data = our_text_splitter(docs)

# Create new vector db if doesn't exist or load existing ones.
print("3. vector store or load function started.")
vector_db = create_or_load_vector_stores_db(vector_db_file_path, splitted_data)

# Create document chain and retriever chain
print("4. function that create a retriever chain with llm and vector db started loading function started.")
our_retriever_chain = retriever_chain(llm=llm, vector_db=vector_db)

# Invoke the retriever chain
print("5. Function that invoke the retriever chain started.")
response = our_retriever_chain.invoke({"input":"What is self attention in Attention is all you need."})

print("Response ::: ",response['answer'])


