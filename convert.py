import os
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader

# Input Folder
INPUT_FOLDER = "documents"

def extract_text_from_file(file_path):
    ext = file_path.split(".")[-1]

    if ext == "pdf":
        loader = PyPDFLoader(file_path)
    elif ext == "docx":
        loader = Docx2txtLoader(file_path)
    elif ext == "txt":
        loader = TextLoader(file_path)
    else:
        print(f"notsuported  format: {file_path}")


        return None

    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])

def convert_all_files():
    text_data = {}
    
    for filename in os.listdir(INPUT_FOLDER):
        file_path = os.path.join(INPUT_FOLDER, filename)
        text = extract_text_from_file(file_path)
        if text:
            text_data[filename] = text
    
    return text_data

if __name__ == "__main__":
    print(" Converting files  ")
    documents = convert_all_files()
    print(f"🔹 Converted {len(documents)} documents")
