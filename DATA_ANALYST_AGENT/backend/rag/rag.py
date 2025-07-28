from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQA

def run_query(question, persist_directory="backend/vector_store/db"):
    vectordb = Chroma(persist_directory=persist_directory, embedding_function=OpenAIEmbeddings())
    retriever = vectordb.as_retriever()

    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)

    qa = RetrievalQA.from_chain_type(llm=llm, retriever=retriever, return_source_documents=False)
    return qa.run(question)
