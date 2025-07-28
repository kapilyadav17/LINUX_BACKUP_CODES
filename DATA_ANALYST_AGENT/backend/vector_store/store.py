from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter

def create_vector_store(docs, persist_directory="backend/vector_store/db"):
    embeddings = OpenAIEmbeddings()
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    texts = text_splitter.split_documents(docs)

    vectordb = Chroma.from_documents(documents=texts, embedding=embeddings, persist_directory=persist_directory)
    vectordb.persist()
    return vectordb
