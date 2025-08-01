from sentence_transformers import SentenceTransformer
import numpy as np
import faiss 
from utils.ingest import create_faiss_index, split_into_chunks
from utils.vector_utils import get_embedding


# Load local embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Global index and chunks to simulate in-memory state
index = None
chunks = []

# Get embedding from SentenceTransformer


def answer_query(question):
    global index, chunks

    if index is None or not chunks:
        raise ValueError("Please upload a document before asking questions.")
    
    # Turn the question into an embedding (vector)
    question_vector = np.array([get_embedding(question)]).astype("float32")

    _,top_indices = index.search(question_vector,k=3)

    # Get the matching chunks
    if len(top_indices[0]) == 0:
        return "No relevant information found."
  
    matched_chunks = [chunks[i] for i in top_indices[0] if i < len(chunks)]

    # Combine and return the result
    result = "\n".join(matched_chunks)
    return f"Here are the most relevant parts of your document:\n\n{result}"


# Setup FAISS index from parsed chunks
def embed_and_store(chunks_input):
    global index, chunks
    index, chunks = create_faiss_index(chunks_input)
    print(f"[DEBUG] Received {len(chunks_input)} chunks")




    