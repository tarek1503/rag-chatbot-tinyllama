import os
import faiss
import numpy as np
from sentence_transformers import SentenceTransformer
import sys
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def create_vector_store(texts, save_path):
    """
    Creates and saves a FAISS vector store from text chunks.
    
    Args:
        texts: List of text chunks
        save_path: Path to save the FAISS index
    """
    try:
        # Choose the most efficient model based on platform
        if sys.platform.startswith('win'):
            model_name = 'paraphrase-MiniLM-L3-v2'  # Smallest for Windows
        elif sys.platform.startswith('linux') or sys.platform.startswith('darwin'):
            model_name = 'all-MiniLM-L6-v2'  # Balanced for Linux/Mac
        else:
            model_name = 'all-MiniLM-L6-v2'  # Default
            
        logger.info(f"Using embedding model: {model_name}")
        
        # Load embedding model
        model = SentenceTransformer(model_name)
        
        # Generate embeddings in batches to reduce memory usage
        batch_size = 32
        embeddings = []
        
        for i in range(0, len(texts), batch_size):
            batch = texts[i:i + batch_size]
            batch_embeddings = model.encode(
                batch, 
                show_progress_bar=False, 
                convert_to_numpy=True,
                normalize_embeddings=True
            )
            embeddings.append(batch_embeddings)
            
        embeddings = np.vstack(embeddings).astype('float32')
        
        logger.info(f"Created embeddings with shape: {embeddings.shape}")
        
        # Create FAISS index
        dimension = embeddings.shape[1]
        index = faiss.IndexFlatIP(dimension)  # Inner product for cosine similarity
        index.add(embeddings)
        
        # Save index
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        faiss.write_index(index, save_path)
        
        # Save metadata with smaller chunks
        metadata_path = f"{save_path}_metadata.txt"
        with open(metadata_path, "w", encoding="utf-8") as f:
            f.write("\n".join(texts))
        
        logger.info(f"Vector store created at {save_path}")
        logger.info(f"Metadata saved at {metadata_path}")
        
        return True
        
    except Exception as e:
        logger.error(f"Error creating vector store: {str(e)}")
        return False