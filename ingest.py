import os
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
    main()