from langchain.document_loaders import PyPDFLoader, CSVLoader, Docx2txtLoader, TextLoader
from pathlib import Path

def load_file(file_path):
    ext = Path(file_path).suffix.lower()

    if ext == ".pdf":
        loader = PyPDFLoader(file_path)
    elif ext == ".csv":
        loader = CSVLoader(file_path)
    elif ext == ".docx":
        loader = Docx2txtLoader(file_path)
    elif ext == ".txt":
        loader = TextLoader(file_path)
    else:
        raise ValueError(f"Unsupported file type: {ext}")

    return loader.load()
