import streamlit as st
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
from utils.llm_helper import setup_llm, format_prompt, get_response

# Configuration
VECTOR_STORE_PATH = "vector_store/faiss_index"
MODEL_NAME = "all-MiniLM-L6-v2"

@st.cache_resource
def load_resources():
    # Load embedding model
    embed_model = SentenceTransformer(MODEL_NAME)
    
    # Load vector store
    index = faiss.read_index(VECTOR_STORE_PATH)
    
    # Load LLM
    llm_pipeline = setup_llm()
    
    return embed_model, index, llm_pipeline

def retrieve_context(query, embed_model, index, k=3):
    # Embed query
    query_embedding = embed_model.encode([query])
    
    # Search index
    distances, indices = index.search(np.array(query_embedding).astype('float32'), k)
    
    # Retrieve text chunks
    with open(f"{VECTOR_STORE_PATH}_metadata.txt", "r") as f:
        all_chunks = f.read().splitlines()
    
    return [all_chunks[i] for i in indices[0]]

def main():
    st.title("RAG Chatbot with TinyLlama-1.1B-Chat-v1.0")
    st.caption("Retrieval-Augmented Generation using open-source models")
    
    # Initialize session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Load resources
    embed_model, index, llm_pipeline = load_resources()
    
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Handle user input
    if prompt := st.chat_input("Ask about the document"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        with st.chat_message("user"):
            st.markdown(prompt)
        
        with st.spinner("Thinking..."):
            # Retrieve relevant context
            context_chunks = retrieve_context(prompt, embed_model, index)
            context = "\n\n".join(context_chunks)
            
            # Format prompt with context
            formatted_prompt = format_prompt(prompt, context)
            
            # Generate response
            full_response = get_response(llm_pipeline, formatted_prompt)
            
            # Extract only the assistant's response
            response = full_response.split("<|assistant|>")[-1].strip()
        
        # Display response
        with st.chat_message("assistant"):
            st.markdown(response)
        
        st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()