# TinyLlama RAG Chatbot 🤖📄

A lightweight Retrieval-Augmented Generation chatbot using [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) to answer questions about your PDF documents. This open-source solution combines efficient text retrieval with generative AI for document-based conversations.

## Features ✨
- **Document Intelligence**: Extract insights from PDF files
- **Lightweight LLM**: Uses TinyLlama-1.1B (1.1B parameter model)
- **Context-Aware Responses**: Retrieves relevant context before answering
- **Streamlit UI**: User-friendly web interface
- **Efficient Vector Search**: FAISS for fast similarity matching
- **Section-Aware Processing**: Preserves document structure

Installation ⚙️
bash
# Clone repository
git clone https://github.com/your-username/tinyllama-rag-chatbot.git
cd tinyllama-rag-chatbot

# Install dependencies
pip install -r requirements.txt

Setup 🛠️
Add your knowledge base PDF:

Place your PDF file in the data/ directory

Rename it to knowledge_base.pdf or update the path in ingest.py


Usage 🚀
1. Process your document
bash
python ingest.py
This will:

Extract text from your PDF

Split it into meaningful chunks

Create a FAISS vector store

Save embeddings and metadata

2. Launch the chatbot
bash
streamlit run app.py
The web interface will open in your browser where you can ask questions about your document.

Note: The knowledge base PDF and generated vector stores are excluded from version control. Place your PDF in the data/ directory before running the application.
