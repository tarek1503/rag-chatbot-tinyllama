# TinyLlama RAG Chatbot 🤖📄

A lightweight Retrieval-Augmented Generation chatbot using [TinyLlama-1.1B-Chat-v1.0](https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0) to answer questions about your PDF documents. This open-source solution combines efficient text retrieval with generative AI for document-based conversations.

![RAG Architecture](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Q8J0Z7K-2W3L3W3Q3Q3Q3Q.png)

## Features ✨
- **Document Intelligence**: Extract insights from PDF files
- **Lightweight LLM**: Uses TinyLlama-1.1B (1.1B parameter model)
- **Context-Aware Responses**: Retrieves relevant context before answering
- **Streamlit UI**: User-friendly web interface
- **Efficient Vector Search**: FAISS for fast similarity matching
- **Section-Aware Processing**: Preserves document structure

## Installation ⚙️
```bash
# Clone repository
git clone https://github.com/tarek1503/rag-chatbot-tinyllama.git
cd rag-chatbot-tinyllama

# Install dependencies
pip install -r requirements.txt
