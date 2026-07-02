import os
os.environ["HF_HOME"] = r"D:\huggingface_cache"

import chromadb
from chromadb.utils import embedding_functions

CHROMA_DB_DIR = r"d:\cursor projects\Automated MCQ Generator & LLM Evaluator\data\chroma_db"
COLLECTION_NAME = "ncert_math_class10"

# Initialize Chroma Client globally for fast retrieval
client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")

try:
    collection = client.get_collection(name=COLLECTION_NAME, embedding_function=sentence_transformer_ef)
except Exception:
    collection = None

def retrieve_context(query: str, n_results: int = 2) -> str:
    """
    Searches ChromaDB for the most relevant context matching the query.
    Returns a concatenated string of the top results.
    """
    if collection is None:
        return "No context available. Database not initialized."
        
    results = collection.query(
        query_texts=[query],
        n_results=n_results
    )
    
    if not results['documents'] or not results['documents'][0]:
        return "No relevant context found."
        
    # Concatenate the retrieved chunks
    context = "\n\n...\n\n".join(results['documents'][0])
    return context
