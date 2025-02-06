from langchain.vectorstores import Chroma
from langchain.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from convert import convert_all_files

# Initialize embeddings & ChromaDB
embedding_model = OllamaEmbeddings(model="llama2")
vector_db = Chroma(collection_name="policy_docs", embedding_function=embedding_model)

def store_documents():
    documents = convert_all_files()
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)

    for filename, text in documents.items():
        text_chunks = splitter.split_text(text)
        vector_db.add_texts(texts=text_chunks)

    print("✅ Documents stored in ChromaDB!")

if __name__ == "__main__":
    store_documents()
