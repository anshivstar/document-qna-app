from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from utils.embed import answer_query, embed_and_store
from utils.ingest import parse_pdf
from tempfile import NamedTemporaryFile
import shutil
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

# CORS for frontend access
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# upload pdf files.
@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    with NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        shutil.copyfileobj(file.file, tmp)
        tmp_path = tmp.name

    # Here we are parsing the PDF and creating the FAISS index

    chunks = parse_pdf(tmp_path)
    embed_and_store(chunks)

    return {"message": "File processed successfully", "chunks": len(chunks)}

# Answer a query based on the uploaded document
@app.post("/query")
async def query_document(question: str = Form(...)):
    answer = answer_query(question)  
    return {"answer": answer}

