from fastapi import FastAPI, File, UploadFile, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import os

from ingestion.loaders import load_file
from vector_store.store import create_vector_store
from rag.rag import run_query


UPLOAD_DIR = "./backend/uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        file_path = f"temp_files/{file.filename}"
        with open(file_path, "wb") as f:
            f.write(contents)

        documents = load_file(file_path)  # this could be failing
        create_vector_store(documents)
        
        return {"message": "File uploaded and stored successfully."}
    
    except Exception as e:
        print("🔥 Error in /upload:", e)
        return JSONResponse(status_code=500, content={"message": f"Internal Server Error: {str(e)}"})

@app.post("/query")
async def query_data(question: str = Form(...), filename: str = Form(...)):
    answer = run_query(question)
    return JSONResponse({"answer": answer})
