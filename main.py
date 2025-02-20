from fastapi import FastAPI
from pydantic import BaseModel
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain.chains import RetrievalQA

from src.helper import download_hugging_face_embedding
from src.prompt import prompt_template
from config import MODEL_PATH, INDEX_NAME

# Initialize FastAPI app
app = FastAPI()

# Setup embeddings and vector store
embeddings = download_hugging_face_embedding()
vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

# Define the prompt template
PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

# Initialize the language model
llm = CTransformers(
    model=MODEL_PATH,
    model_type="llama",
    config={
        "max_new_tokens": 512,
        "temperature": 0.8,
    },
)

# Initialize the RetrievalQA chain
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs={"prompt": PROMPT}
)

class QueryRequest(BaseModel):
    query: str

@app.get("/")
async def health():
    return {"status": "OK"}

@app.post("/query")
async def get_answer(request: QueryRequest):
    input_query = request.query
    result = qa({"query": input_query})
    return {"result": result["result"]}