import os
from dotenv import load_dotenv
from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA

# Load API key
load_dotenv()

# Step 1: Load documents
loader = TextLoader("knowledge.txt")
documents = loader.load()

# Step 2: Split into chunks
splitter = CharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = splitter.split_documents(documents)

# Step 3: Embed and store in Chroma
embedding = OpenAIEmbeddings()
vectordb = Chroma.from_documents(docs, embedding, persist_directory="chroma_db")

# Step 4: Create retriever
retriever = vectordb.as_retriever()

# Step 5: Create QA chain
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Step 6: Ask a question
query = "What is LangChain?"
response = qa_chain.run(query)

print("Q:", query)
print("A:", response)
