'''import os
from utils.data_loader import load_and_split_pdf
from utils.vector_store import create_vector_store

def main():
    # Configuration
    DATA_DIR = "data"
    PDF_FILE = "knowledge_base.pdf"
    VECTOR_STORE_PATH = "vector_store/faiss_index"
    
    # Load and process document
    documents = load_and_split_pdf(os.path.join(DATA_DIR, PDF_FILE))
    
    # Create and save vector store
    create_vector_store(documents, VECTOR_STORE_PATH)
    print(f"Vector store created at {VECTOR_STORE_PATH}")

if __name__ == "__main__":
    main()'''

import os
from utils.data_loader import load_file, split_text  # Updated import
from utils.vector_store import create_vector_store

def main():
    DATA_DIR = "data"
    VECTOR_STORE_PATH = "vector_store/faiss_index"
    
    documents = []
    for filename in os.listdir(DATA_DIR):
        if filename.startswith("."):  # Skip hidden files
            continue
            
        file_path = os.path.join(DATA_DIR, filename)
        ext = os.path.splitext(filename)[1].lower()
        
        if ext not in [".pdf", ".docx"]:
            continue
            
        try:
            print(f"Processing: {filename}")
            # Use the new functions:
            text = load_file(file_path)  # Changed from load_and_split_pdf
            chunks = split_text(text)    # Split the loaded text
            documents.extend(chunks)
        except Exception as e:
            print(f"Failed to process {filename}: {str(e)}")
    
    create_vector_store(documents, VECTOR_STORE_PATH)
    print(f"Created vector store with {len(documents)} chunks")

if __name__ == "__main__":
    main()