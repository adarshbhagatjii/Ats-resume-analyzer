# 🚀 ATS Resume Analyzer with Memory

An AI-powered Resume Screening System that simulates how modern **Applicant Tracking Systems (ATS)** evaluate resumes against job descriptions.

Built using **LLMs + RAG (Retrieval-Augmented Generation)**, this project helps candidates optimize their resumes, improve job matching, and get AI-driven career insights.

---

## 📌 Live Demo

🔗 **Live Demo:** [ATS Resume Analyzer](https://ats-resumee-analyzer.streamlit.app/)

---

## 🧠 Project Overview

This application allows users to:

* Upload a **Resume (PDF)**
* Upload a **Job Description (PDF)**
* Perform **ATS-based analysis**
* Chat with the system using **memory-enabled AI**

It combines **LangChain + Groq LLM + Vector Search (FAISS)** to deliver fast and intelligent responses.

---

## ✨ Key Features

✅ ATS Resume Scoring & Analysis
✅ Resume vs Job Description Matching
✅ AI-powered Career Suggestions
✅ Memory-enabled Chat System
✅ Fast LLM Responses using Groq
✅ Clean UI with Top Navigation
✅ Retrieval-Augmented Generation (RAG) Pipeline

---

## 🏗️ Architecture

```
User Input (Resume + JD)
        ↓
PDF Loader (PyPDFLoader)
        ↓
Text Splitting (RecursiveCharacterTextSplitter)
        ↓
Embeddings (HuggingFace)
        ↓
Vector Store (FAISS)
        ↓
Retriever (Top-K relevant chunks)
        ↓
LLM (Groq - LLaMA 3.3 70B)
        ↓
Response + Memory (ConversationBufferMemory)
```

---

## ⚙️ Tech Stack

### 🖥️ Frontend

* Streamlit

### 🧠 Backend / AI

* LangChain
* Groq (LLaMA 3.3 70B)
* HuggingFace Embeddings

### 📦 Data Handling

* FAISS (Vector Database)
* PyPDFLoader
* RecursiveCharacterTextSplitter

### 🔧 Utilities

* Python
* dotenv

---

## 📂 Project Structure

```
📦 ats-resume-analyzer
 ┣ 📜 app.py
 ┣ 📜 requirements.txt
 ┣ 📜 .env     # add your own env file 
 ┗ 📜 README.md
```

---

## 🔑 Environment Variables

Create a `.env` file and add:

```
GROQ_API_KEY=your_api_key_here
```

---

## ▶️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/ats-resume-analyzer.git
cd ats-resume-analyzer
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the App

```bash
streamlit run app.py
```

---

## 💬 How It Works

1. Upload your **Resume & Job Description**
2. Click **Analyze Resume**
3. System builds a **vector database**
4. Ask questions or generate **ATS report**
5. Chat continues with **memory context**

---

---

## 👨‍💻 Author

**Adarsh Bhagat**
🚀 Software Engineer | MERN Stack Developer | AI/ML Enthusiast

---

## 🌟 Future Enhancements

* 📊 ATS Score Visualization (Progress Bar)
* 📄 Downloadable PDF Report
* 🎤 Voice-based Resume Assistant
* 🌐 Deployment with Custom Domain
* 🔍 Keyword Highlighting in Resume

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repo and submit a PR.

---

## 📜 License

This project is licensed under the **MIT License**.

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!

