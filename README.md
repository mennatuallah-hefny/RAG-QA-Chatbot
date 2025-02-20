[![Python 3.10](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.85.0-brightgreen?logo=fastapi)](https://fastapi.tiangolo.com/)
[![LangChain](https://img.shields.io/badge/LangChain-0.0.1-yellowgreen)](https://github.com/hwchase17/langchain)
[![Pinecone](https://img.shields.io/badge/Pinecone-Vector%20DB-lightgrey?logo=pinecone)](https://www.pinecone.io/)
[![Llama 2](https://img.shields.io/badge/Meta-Llama%202-critical?logo=meta)](https://ai.meta.com/resources/models-and-libraries/llama-downloads/)

# RAG QA Chatbot

<div>
  <a href="https://www.loom.com/share/7c60a5cb31b04c5995e440762d6509b1">
    <p>RAG QA Chatbot - Watch the Demo Video</p>
  </a>
  <a href="https://www.loom.com/share/7c60a5cb31b04c5995e440762d6509b1">
    <img style="max-width:300px;" src="https://cdn.loom.com/sessions/thumbnails/7c60a5cb31b04c5995e440762d6509b1-ba3bbe6b4767cf63-full-play.gif" alt="Demo Video Thumbnail">
  </a>
</div>

## Project Overview

The **RAG QA Chatbot** is a Retrieval-Augmented Generation system that answers questions by leveraging content extracted from provided documents. This project combines several powerful technologies:
- **FastAPI** for building a robust backend API.
- **Streamlit** for an interactive frontend UI.
- **LangChain** to manage document retrieval and integrate with the language model.
- **Meta's Llama 2 (quantized)** to generate intelligent responses.
- **Pinecone** for efficient vector storage and retrieval.

> **Demo Note:** The demonstration uses *The Gale Encyclopedia of Medicine* as the source document.

## Setup and Installation

Follow these steps to set up and run the chatbot on your local machine.

### 1. Create a Virtual Environment

Create a new conda environment with Python 3.10:
```bash
conda create -n <environment_name> python=3.10 -y
```

### 2. Activate the Environment

Activate your newly created environment:
```bash
conda activate <environment_name>
```

### 3. Install Dependencies

Install the required Python packages:
```bash
pip install -r requirements.txt
```

### 4. Configure Your Environment Variables

Create a `.env` file in the root directory of the project and add your Pinecone API key:
```ini
PINECONE_API_KEY="xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

### 5. Download the Quantized Llama 2 Model

Download the model file named `llama-2-7b-chat.ggmlv3.q4_0.bin` from the following link:
[Download Llama 2 Model](https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main)

Place the downloaded model in the `model` directory of the project.

### 6. Launch the Backend Server

Start the FastAPI server using Uvicorn:
```bash
uvicorn main:app --host localhost --port 5000 --reload
```

### 7. Start the Frontend Application

Run the Streamlit app to launch the chatbot interface:
```bash
streamlit run app_streamlit.py
```
