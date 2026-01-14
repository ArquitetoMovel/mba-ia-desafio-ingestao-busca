import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
from langchain_postgres import PGVector
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")
OPENAI_EMBEDDING_MODEL = os.getenv("OPENAI_EMBEDDING_MODEL")
PG_VECTOR_COLLECTION_NAME = os.getenv("PG_VECTOR_COLLECTION_NAME")

embeddings = OpenAIEmbeddings(model=OPENAI_EMBEDDING_MODEL)
vector_store = PGVector(
                embeddings=embeddings, 
                connection=DATABASE_URL, 
                collection_name=PG_VECTOR_COLLECTION_NAME
              )

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

PROMPT_TEMPLATE = """
CONTEXTO:
{contexto}

REGRAS:
- Responda somente com base no CONTEXTO.
- Se a informação não estiver explicitamente no CONTEXTO, responda:
  "Não tenho informações necessárias para responder sua pergunta."
- Nunca invente ou use conhecimento externo.
- Nunca produza opiniões ou interpretações além do que está escrito.

EXEMPLOS DE PERGUNTAS FORA DO CONTEXTO:
Pergunta: "Qual é a capital da França?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Quantos clientes temos em 2024?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

Pergunta: "Você acha isso bom ou ruim?"
Resposta: "Não tenho informações necessárias para responder sua pergunta."

PERGUNTA DO USUÁRIO:
{pergunta}

RESPONDA A "PERGUNTA DO USUÁRIO"
"""

def search_prompt(question=None):
    if question is None:
        raise ValueError("Question is required")
    
    docs = vector_store.similarity_search(question, k=10)
    contexto = "\n\n".join([doc.page_content for doc in docs])
    
    prompt = PROMPT_TEMPLATE.format(contexto=contexto, pergunta=question)
    response = llm.invoke(prompt)
    return response.content
    