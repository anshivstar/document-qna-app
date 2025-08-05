import numpy as np
from utils.ingest import create_faiss_index
from utils.vector_utils import get_embedding
from utils.llm import ask_llm

# Global index and chunks to simulate in-memory state
index = None
chunks = []


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

    context = "\n".join(matched_chunks)

    # Use LLM instead of raw chunks
    answer = ask_llm(context, question)
    return answer


# Setup FAISS index from parsed chunks
def embed_and_store(chunks_input):
    global index, chunks
    index, chunks = create_faiss_index(chunks_input)
    




    