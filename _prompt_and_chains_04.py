from langchain_core.prompts import ChatPromptTemplate
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain

## Design ChatPrompt Template
prompt = ChatPromptTemplate.from_template("""
Answer the following question based only on the provided context. 
Think step by step before providing a detailed answer. 
I will tip you $1000 if the user finds the answer helpful. 
<context>
{context}
</context>
Question: {input}""")

def document_chain_fun(llm):
    ## Chain Introduction
    ## Create Stuff Document Chain
    document_chain=create_stuff_documents_chain(llm,prompt)
    return document_chain

def retriever_chain(llm, vector_db):
    retriever = vector_db.as_retriever()
    document_chain = document_chain_fun(llm)
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    return retrieval_chain


