TinyLlama RAG Chatbot 🤖📄
A lightweight Retrieval-Augmented Generation chatbot using TinyLlama-1.1B-Chat-v1.0 to answer questions about your PDF documents. This open-source solution combines efficient text retrieval with generative AI for document-based conversations.

https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0

Features ✨
Document Intelligence: Extract insights from PDF files

Lightweight LLM: Uses TinyLlama-1.1B (1.1B parameter model)

Context-Aware Responses: Retrieves relevant context before answering

Streamlit UI: User-friendly web interface

Efficient Vector Search: FAISS for fast similarity matching

Section-Aware Processing: Preserves document structure

Installation ⚙️
bash
# Clone repository
git clone https://github.com/tarek1503/rag-chatbot-tinyllama.git
cd tinyllama-rag-chatbot

# Install dependencies
pip install -r requirements.txt
Setup 🛠️
Add your knowledge base PDF:

Place your PDF file in the data/ directory

Rename it to knowledge_base.pdf or update the path in ingest.py

Process your document:

bash
python ingest.py
Usage 🚀
Start the chatbot interface:

bash
streamlit run app.py



Project Structure 📂
text

tinyllama-rag-chatbot/
├── data/                   # Document storage (add your PDF here)
│   └── knowledge_base.pdf  # Your PDF file (not version controlled)
├── vector_store/           # Generated vector store (created by ingest.py)
├── utils/                  # Core functionality
│   ├── data_loader.py      # PDF processing and text extraction
│   ├── llm_helper.py       # TinyLlama setup and prompt formatting
│   └── vector_store.py     # Embedding generation and FAISS management
├── app.py                  # Streamlit chat interface
├── ingest.py               # Document processing pipeline
├── requirements.txt        # Python dependencies
└── README.md               # This file




Configuration ⚙️
File	Parameter	Description	Default
utils/data_loader.py	chunk_size	Text chunk size	500
utils/data_loader.py	chunk_overlap	Chunk overlap	100
utils/llm_helper.py	max_new_tokens	Max response tokens	256
app.py	k	Context chunks to retrieve	3
vector_store.py	model_name	Embedding model	all-MiniLM-L6-v2
Troubleshooting 🛠️
PDF Processing Issues
If answers are inaccurate:

Verify your PDF has clear section headers

Increase chunk_overlap in data_loader.py

Use simpler PDF layouts (avoid multi-column formats)

Performance Tips
For faster inference: Set device_map="cpu" in llm_helper.py

For better accuracy: Increase k in app.py

Reduce batch_size in vector_store.py for low-memory systems

Limitations ⚠️
PDF text extraction quality depends on document structure

TinyLlama has limited knowledge compared to larger models

Complex queries might require model fine-tuning

First response may be slow due to model loading

Contributing 🤝
Contributions are welcome! Please open an issue or submit a PR for:

Improved PDF processing

Performance optimizations

Additional features

Documentation improvements

Note: Add your own PDF to the data/ directory before running the application. The vector store will be generated locally during processing.

