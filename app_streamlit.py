# app_streamlit.py
import streamlit as st
import requests

# URL of your FastAPI endpoint
API_URL = "http://localhost:5000/query"

st.title("RAG QA Chatbot")

# Input field for user question
user_query = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if user_query.strip() == "":
        st.warning("Please enter a question.")
    else:
        # Send a POST request to your FastAPI endpoint with the user's query
        try:
            response = requests.post(API_URL, json={"query": user_query})
            if response.status_code == 200:
                result = response.json()
                st.markdown("### Answer")
                st.write(result.get("result", "No result returned."))
            else:
                st.error(f"Error {response.status_code}: {response.text}")
        except requests.exceptions.RequestException as e:
            st.error(f"An error occurred: {e}")
