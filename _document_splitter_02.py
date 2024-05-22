from  langchain.text_splitter import RecursiveCharacterTextSplitter

def our_text_splitter(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)    
    print("Docs :: ", splitter)
    splitted_documents = splitter.split_text(docs)
    print("After splitting")
    return splitted_documents


if __name__ == "main":
    our_text_splitter