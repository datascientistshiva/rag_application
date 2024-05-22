from langchain_community.document_loaders import PyPDFLoader
from langchain_community.document_loaders import WebBaseLoader

from  langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.utilities import ArxivAPIWrapper
from langchain_community.tools import ArxivQueryRun

from langchain_community.utilities import WikipediaAPIWrapper
from langchain_community.tools import WikipediaQueryRun

def main():
    print("Document loader application:")

# Load a single file from pdf_path and return the loaded documents.
def pdf_loader(pdf_path):
    loader = PyPDFLoader(pdf_path)
    docs = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = 1000, chunk_overlap = 200)
    documents = text_splitter.split_documents(docs)
    return documents

def Web_based_document_loader(url):
    pass

if __name__ == "__main__":
    main()
