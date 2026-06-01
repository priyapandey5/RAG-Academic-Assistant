# 🎓 RAG Academic Assistant

An AI-powered Academic Assistant that answers student queries using a Retrieval-Augmented Generation (RAG) pipeline built on institutional academic data.


<img width="1920" height="835" alt="Screenshot (123)" src="https://github.com/user-attachments/assets/8b1068c3-50c9-4781-9444-c1ccad731bb2" />



The system is designed to provide accurate responses about:

* Admissions
* Fee Structure
* Scholarships
* Classes and Academic Support
* Examinations
* Student Policies
* Academic Resources

The assistant retrieves relevant information from a pre-indexed academic knowledge base and generates contextual responses using Google Gemini.

---

# 🚀 Features

## Academic Question Answering

Students can ask questions related to:

* Admissions
* Fees
* Scholarships
* Classes
* Examinations
* Academic Policies

---

## Retrieval-Augmented Generation (RAG)

The assistant does not rely solely on the LLM.

Instead, it:

1. Searches a pre-built academic knowledge base
2. Retrieves the most relevant content
3. Sends the retrieved context to Gemini
4. Generates a grounded response

---

## Fast Semantic Search

Uses:

* Sentence Transformers
* FAISS Vector Database

to retrieve relevant academic information efficiently.

---

## Context-Aware Responses

The assistant generates responses based on institutional data rather than generic internet knowledge, reducing hallucinations and improving reliability.

---

## Conversation Memory

Stores chat history using MongoDB for session-based conversations.

---

# 🎯 Project Objective

The goal of this project is to provide students with an intelligent academic support assistant capable of answering institution-specific questions through a RAG architecture powered by:

* FastAPI
* Streamlit
* FAISS
* Sentence Transformers
* Google Gemini
* MongoDB

* 
Academic PDF Dataset
        ↓
Text Chunking
        ↓
Embeddings
        ↓
FAISS Index Creation
        ↓
Academic Assistant


