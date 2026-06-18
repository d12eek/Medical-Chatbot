# 🩺 Medical Chatbot — AI-Powered Medical Q&A System

A complete end-to-end Medical Chatbot built using **RAG (Retrieval Augmented Generation)**, **LangChain**, **Pinecone**, **Google Gemini**, and **Flask**.

---

## 📌 Project Overview

This chatbot allows users to ask medical questions and get accurate answers based on a medical reference book. It uses a RAG pipeline to retrieve relevant context from the PDF and generate responses using Google Gemini LLM.

---

## 🏗️ Project Structure

```
Medical-Chatbot/
│
├── .github/
│   └── workflows/
│       └── main.yaml
│
├── data/
│   └── Medical_book.pdf
│
├── research/
│   └── trials.ipynb
│
├── src/
│   ├── __init__.py
│   ├── helper.py
│   └── prompt.py
│
├── static/
│   └── style.css
│
├── templates/
│   └── chat.html
│
├── .env
├── .gitignore
├── app.py
├── Dockerfile
├── requirements.txt
├── setup.py
├── store_index.py
└── README.md
```

---

## ⚙️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Groq (Llama 3.3 70B) |
| Embeddings | HuggingFace `all-MiniLM-L6-v2` |
| Vector Database | Pinecone |
| Framework | LangChain |
| Web App | Flask |
| Frontend | HTML, CSS |
| Deployment | Docker |

---

## 🔄 How It Works

```
📄 Medical PDF
      ↓
  store_index.py  (Run Once)
      ↓
  Load PDF → Split Chunks → HuggingFace Embeddings
      ↓
  Store Vectors in Pinecone
      ↓
👤 User asks a question
      ↓
  app.py (Flask Server)
      ↓
  Convert question → Search Pinecone
      ↓
  Get relevant chunks from PDF
      ↓
  Send to Gemini API
      ↓
  💬 Answer displayed in Chat UI
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/d12eek/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
pip install -e .
```

### 4. Set Up Environment Variables
Create a `.env` file in the root directory:
```env
PINECONE_API_KEY=your_pinecone_api_key
GROQ_API_KEY=your_groq_api_key
```

### 5. Load PDF into Pinecone (Run Once)
```bash
python store_index.py
```

### 6. Run the Application
```bash
python app.py
```

### 7. Open in Browser
```
http://localhost:8080
```

---

## 🔑 API Keys Required

| Key | Where to Get | Cost |
|-----|-------------|------|
| `PINECONE_API_KEY` | [pinecone.io](https://pinecone.io) | ✅ Free |
| `GROQ_API_KEY` | [console.groq.com](https://console.groq.com) | ✅ Free |

---

## 📦 Requirements

```
flask
langchain
langchain-community
langchain-groq
langchain-pinecone
pinecone-client
sentence-transformers
pypdf
python-dotenv
```

---

## 💬 Sample Questions to Ask

- What is diabetes?
- What are the symptoms of malaria?
- What is hypertension?
- How is pneumonia treated?
- What causes anemia?

---

## 🖥️ Screenshots

> Chat UI with medical question and answer

---

## 📝 License

This project is for educational purposes only. Medical information provided by this chatbot should not replace professional medical advice.

---

## 🙏 Acknowledgements

- [LangChain](https://langchain.com)
- [Pinecone](https://pinecone.io)
- [Groq](https://console.groq.com)
- [HuggingFace](https://huggingface.co)
- Original project inspiration: [entbappy/Build-a-Complete-Medical-Chatbot](https://github.com/entbappy/Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS)