[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.85.0-brightgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.0.1-yellowgreen)](https://github.com/hwchase17/langchain)
[![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-lightgrey?logo=pinecone)](https://www.pinecone.io/)
[![Llama 2](https://img.shields.io/badge/Meta-Llama%202-critical?logo=meta)](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)
# RAG QA Chatbot

<div>
    <a href="https://www.loom.com/share/7c60a5cb31b04c5995e440762d6509b1">
      <p>RAG QA Chatbot - Watch Video</p>
    </a>
    <a href="https://www.loom.com/share/7c60a5cb31b04c5995e440762d6509b1">
      <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/7c60a5cb31b04c5995e440762d6509b1-ba3bbe6b4767cf63-full-play.gif">
    </a>
  </div>


## Project Overview

The **RAG QA Chatbot** is a Retrieval-Augmented Generation system designed to answer questions using content from provided documents. The project leverages:
- **FastAPI** for the backend API,
- **Streamlit** for the frontend UI,
- **LangChain** to manage document retrieval and interaction with the LLM,
- **Meta Llama2** (quantized model) for generating answers,
- **Pinecone** for vector storage and retrieval.

**For the demo, the document used is The Gale Encyclopedia of Medicine book.**

## Steps to run the project

#### 1) Create virtual environment 
```bash
$ conda create -n `environment_name` python=3.10 -y
```

#### 2) Activate environment 
```bash
$ conda activate `environment_name`
```

### 3) Install requirements  
```bash
$ pip install -r requirements.txt
```

### Create a `.env` file in the root directory and add your Pinecone credentials as follows:
```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### Download the quantize model from the link provided in model folder & keep the model in the model directory:

```ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin


## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main
```

```bash
# run the following command
uvicorn main:app --host localhost --port 5000 --reload
```

```bash
# Finally run the following command
streamlit run app_streamlit.py
```






