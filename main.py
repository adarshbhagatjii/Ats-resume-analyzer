# ================== IMPORTS ==================
import streamlit as st
import os
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain.memory import ConversationBufferMemory

load_dotenv()

# ================== PAGE CONFIG ==================
st.set_page_config(page_title="ATS Resume Analyzer", layout="wide")

# ================== CUSTOM CSS ==================
st.markdown("""
<style>
.navbar {
    display: flex;
    justify-content: center;
    gap: 20px;
    background: linear-gradient(90deg, #00D4FF, #090979);
    padding: 15px;
    border-radius: 10px;
    margin-bottom: 20px;
}
.nav-btn {
    color: white;
    font-weight: bold;
    cursor: pointer;
}
.chat-box {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
}
.user { background-color: #1f77b4; color: white; }
.bot { background-color: #2ca02c; color: white; }
</style>
""", unsafe_allow_html=True)

# ================== NAVBAR STATE ==================
if "page" not in st.session_state:
    st.session_state.page = "Home"

# ================== NAVBAR ==================
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("🏠 Home"):
        st.session_state.page = "Home"

with col2:
    if st.button("📊 Analyzer"):
        st.session_state.page = "Analyzer"

with col3:
    if st.button("ℹ️ About"):
        st.session_state.page = "About"

st.markdown("---")

# ================== LLM ==================
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    groq_api_key=st.secrets["GROQ_API_KEY"]
)

parser = StrOutputParser()

# ================== MEMORY ==================
if "memory" not in st.session_state:
    st.session_state.memory = ConversationBufferMemory(
        memory_key="chat_history",
        return_messages=True
    )

# ================== HOME ==================
if st.session_state.page == "Home":

    st.title("🚀 ATS Resume Analyzer")
    st.write("### AI-powered Resume Screening & Career Assistant")

    col1, col2 = st.columns(2)

    with col1:
        st.info("📄 Upload Resume & Job Description")
        st.info("🤖 AI analyzes ATS score")
        st.info("💬 Chat with your resume")

    with col2:
        st.success("🔥 Features:")
        st.write("""
        - Resume vs Job Description Matching  
        - ATS Score Generation  
        - AI Career Suggestions  
        - Memory-enabled Chat  
        """)

# ================== ANALYZER ==================
elif st.session_state.page == "Analyzer":

    st.title("📊 Resume Analyzer")

    col1, col2 = st.columns(2)

    with col1:
        resume_file = st.file_uploader("Upload Resume", type="pdf")

    with col2:
        jd_file = st.file_uploader("Upload Job Description", type="pdf")

    def process_pdf(uploaded_file, filename):
        with open(filename, "wb") as f:
            f.write(uploaded_file.read())

        loader = PyPDFLoader(filename)
        return loader.load()

    prompt = PromptTemplate.from_template("""
    You are an AI ATS system and career assistant.

    Previous conversation:
    {chat_history}

    Context:
    {context}

    Question:
    {question}

    Give professional and helpful answers.
    """)

    if resume_file and jd_file:

        if st.button("🚀 Analyze Resume"):

            with st.spinner("Analyzing Resume..."):
                resume_docs = process_pdf(resume_file, "resume.pdf")
                jd_docs = process_pdf(jd_file, "jd.pdf")

                all_docs = resume_docs + jd_docs

                splitter = RecursiveCharacterTextSplitter(
                    chunk_size=500,
                    chunk_overlap=50
                )

                chunks = splitter.split_documents(all_docs)

                embedding = HuggingFaceEmbeddings()
                vector_db = FAISS.from_documents(chunks, embedding)

                st.session_state.vdb = vector_db

            st.success("✅ ATS Ready!")

    def ask_llm(question):
        retriever = st.session_state.vdb.as_retriever(search_kwargs={"k": 4})
        docs = retriever.invoke(question)

        context = "\n".join([d.page_content for d in docs])

        chat_history = st.session_state.memory.load_memory_variables({})["chat_history"]

        chain = prompt | llm | parser

        result = chain.invoke({
            "context": context,
            "question": question,
            "chat_history": chat_history
        })

        st.session_state.memory.save_context(
            {"input": question},
            {"output": result}
        )

        return result

    if "vdb" in st.session_state:

        st.subheader("📈 ATS Report")

        if st.button("Generate Full ATS Report"):
            st.write(ask_llm("Give full ATS analysis"))

        st.subheader("💬 Chat with Resume")

        user_q = st.text_input("Ask something...")

        if user_q:
            response = ask_llm(user_q)

            st.markdown(f"<div class='chat-box user'>🧑 {user_q}</div>", unsafe_allow_html=True)
            st.markdown(f"<div class='chat-box bot'>🤖 {response}</div>", unsafe_allow_html=True)

    else:
        st.warning("Upload files and click Analyze")

# ================== ABOUT ==================
elif st.session_state.page == "About":

    st.title("ℹ️ About Project")

    st.write("""
    ## 🚀 ATS Resume Analyzer with Memory

    This is an AI-powered ATS Resume Scanner that evaluates resumes against job descriptions using LLM + RAG architecture.

    It helps candidates optimize resumes and improve job matching.
    """)

    st.subheader("👨‍💻 Creator")
    st.write("**Adarsh Bhagat **")

    st.subheader("🧠 Tech Stack")
    st.code("""
    Streamlit
    LangChain
    Groq LLM
    FAISS Vector DB
    HuggingFace Embeddings
    PyPDFLoader
    Python Dotenv
    """)

    st.subheader("✨ Features")
    st.write("""
    - ATS Resume Analysis  
    - Resume vs JD Matching  
    - AI Suggestions  
    - Memory Chat  
    """)