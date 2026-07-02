import os
os.environ["OPENBLAS_NUM_THREADS"] = "1"
os.environ["OMP_NUM_THREADS"] = "1"
import re
import chromadb
from chromadb.utils import embedding_functions
import warnings

# Suppress some noisy warnings from PyTorch/transformers if any
warnings.filterwarnings('ignore')

# Config
MD_DIR = r"d:\cursor projects\Automated MCQ Generator & LLM Evaluator\data\markdown_context"
CHROMA_DB_DIR = r"d:\cursor projects\Automated MCQ Generator & LLM Evaluator\data\chroma_db"
COLLECTION_NAME = "ncert_math_class10"

MAX_CHUNK_SIZE = 800  # Target max characters per chunk

def chunk_markdown_safely(text, max_chunk_size=800):
    """
    Splits markdown safely by paragraphs (\n\n) to avoid breaking LaTeX formulas.
    """
    paragraphs = re.split(r'\n\n+', text)
    chunks = []
    current_chunk = ""
    
    for para in paragraphs:
        # If the paragraph alone is larger than max_chunk_size, we just have to keep it whole 
        # to guarantee we don't split a formula.
        
        # If adding this paragraph exceeds our limit, push the current chunk and start a new one
        if len(current_chunk) + len(para) > max_chunk_size and current_chunk:
            chunks.append(current_chunk.strip())
            current_chunk = para
        else:
            if current_chunk:
                current_chunk += "\n\n" + para
            else:
                current_chunk = para
                
    if current_chunk:
        chunks.append(current_chunk.strip())
        
    return chunks

def ingest():
    print("Initializing ChromaDB...")
    client = chromadb.PersistentClient(path=CHROMA_DB_DIR)
    
    # We use the default sentence-transformer model: all-MiniLM-L6-v2
    print("Loading embedding model (this may take a moment to download on first run)...")
    sentence_transformer_ef = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
    
    collection = client.get_or_create_collection(
        name=COLLECTION_NAME,
        embedding_function=sentence_transformer_ef,
        metadata={"hnsw:space": "cosine"}
    )
    
    for filename in os.listdir(MD_DIR):
        if not filename.endswith(".md"):
            continue
            
        md_path = os.path.join(MD_DIR, filename)
        topic = filename.replace(".md", "").replace("_", " ")
        print(f"\nProcessing {topic}...")
        
        with open(md_path, "r", encoding="utf-8") as f:
            text = f.read()
            
        chunks = chunk_markdown_safely(text, MAX_CHUNK_SIZE)
        
        documents = []
        metadatas = []
        ids = []
        
        for i, chunk in enumerate(chunks):
            documents.append(chunk)
            metadatas.append({"topic": topic, "source": filename, "chunk_index": i})
            ids.append(f"{topic.replace(' ', '_')}_chunk_{i}")
            
        print(f"Adding {len(chunks)} chunks to collection for {topic}...")
        
        collection.upsert(
            documents=documents,
            metadatas=metadatas,
            ids=ids
        )
        
    print("\nIngestion complete!")
    print(f"Total chunks in collection: {collection.count()}")

if __name__ == "__main__":
    ingest()
