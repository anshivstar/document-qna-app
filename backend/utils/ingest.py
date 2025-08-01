import pdfplumber
import numpy as np
import faiss
from openai import OpenAIError
from utils.vector_utils import get_embedding

CHUNK_SIZE = 200

#parse pdf file and return text 

def parse_pdf(file_path):
    text = ""
    with pdfplumber.open(file_path) as pdf:
       for pdf_page in pdf.pages:
        text += pdf_page.extract_text() + "\n"
    return split_into_chunks(text)

# Split text into chunks of a specified size

def split_into_chunks(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    chunks =[]
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i + chunk_size]))
    return chunks

# Create a FAISS index from the text chunks

def create_faiss_index(chunks):
    vectors = []
   
    for chunk in chunks:
        try:
            vec = get_embedding(chunk)
            vectors.append(vec)
        except Exception as e:
            print(f"Error embedding chunk: {e}")
            continue
    if not vectors:
        raise ValueError("No embeddings were generated. Check your input text.")

    vectors = np.array(vectors).astype("float32")

    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(vectors)

    return index, chunks

