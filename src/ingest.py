import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain_postgres import PGVector
from dotenv import load_dotenv

load_dotenv()

# Get the project root directory (parent of src/)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Get PDF_PATH from environment or use default
PDF_PATH_ENV = os.getenv("PDF_PATH", "document.pdf")
if os.path.isabs(PDF_PATH_ENV):
    PDF_PATH = PDF_PATH_ENV
else:
    # Resolve relative path from project root
    PDF_PATH = os.path.join(PROJECT_ROOT, PDF_PATH_ENV)

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")

def ingest_pdf():
    if not os.path.exists(PDF_PATH):
        raise ValueError(f"File path {PDF_PATH} does not exist")
    
    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=150)
    chunks = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)
    PGVector.from_documents(
        documents=chunks,
        embedding=embeddings,
        connection=DATABASE_URL,
        collection_name=PG_VECTOR_COLLECTION_NAME
    )
    print(f"Ingested {len(chunks)} chunks into the database")

if __name__ == "__main__":
    ingest_pdf()