from src.helper import load_pdf, text_split, download_hugging_face_embedding
from langchain_pinecone import PineconeVectorStore
from config import INDEX_NAME

extracted_data = load_pdf("./data")
text_chunks = text_split(extracted_data=extracted_data)
embeddings = download_hugging_face_embedding()

vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)
vectorstore.from_texts([t.page_content for t in text_chunks], index_name=INDEX_NAME, embedding=embeddings)