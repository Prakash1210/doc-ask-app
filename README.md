# 📚 Doc Ask App

An AI-powered document assistant that lets you **upload PDFs or text files** and then **ask questions** about their content — powered by **FastAPI**, **LangChain**, **FAISS**, and **React**.  

This project replicates the features of the [Lovable.io Doc Ask App](https://doc-ask-app.lovable.app/) — but built completely from scratch using open-source tools.

---

## 🚀 Features

- 📄 Upload **PDF** or **Text** files
- ⚙️ Automatic **text extraction** from documents
- 🧠 Converts text into **embeddings** using OpenAI
- 🔍 Stores embeddings using **FAISS Vector Store**
- 💬 Ask natural language questions about your uploaded document
- ⚡ Built with **FastAPI (Backend)** + **React (Frontend)**

---

## 🧰 Tech Stack

| Layer | Tools |
|-------|--------|
| **Frontend** | React + Vite + Axios |
| **Backend** | FastAPI + LangChain + FAISS + OpenAI |
| **Database/Vector Store** | FAISS |
| **Environment** | Python 3.10+, Node 18+ |

---

## 🗂️ Folder Structure

```

doc-ask-app/
│
├── backend/
│   ├── app.py
│   ├── document_handler.py
│   ├── vector_store.py
│   ├── chat_logic.py
│   ├── requirements.txt
│   ├── .env
│   ├── uploads/
│   ├── faiss_index.bin  (auto-created)
│   ├── meta_store.pkl   (auto-created)
│   └── **init**.py
│
└── frontend/
├── package.json
├── vite.config.js
├── public/
│   └── index.html
└── src/
├── App.jsx
├── main.jsx
├── index.css
├── components/
│   ├── FileUpload.jsx
│   ├── ChatBox.jsx
│   └── Loader.jsx
└── utils/
└── api.js

````

---

## ⚙️ Backend Setup (FastAPI + LangChain)

### 1️⃣ Create and activate a virtual environment
```bash
cd backend
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
````

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add your environment variables

Create a file named `.env` inside the `backend` folder:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 4️⃣ Start the backend server

```bash
uvicorn app:app --reload
```

The backend runs at → `http://127.0.0.1:8000`

---

## 💻 Frontend Setup (React + Vite)

### 1️⃣ Install dependencies

```bash
cd frontend
npm install
```

### 2️⃣ Start the development server

```bash
npm run dev
```

Frontend runs at → `http://localhost:5173`

---

## 🔗 Connecting Frontend & Backend

In the `vite.config.js` file (inside `frontend`):

```js
server: {
  proxy: {
    "/api": "http://127.0.0.1:8000"
  }
}
```

This ensures all frontend requests like `/api/upload` and `/api/chat` are routed to your FastAPI backend.

---

## 🧾 Usage Steps

1. Start both **backend** and **frontend** servers.
2. Open the app in your browser → `http://localhost:5173`
3. Upload a `.pdf` or `.txt` document.
4. Ask any question about the content!
5. The model retrieves the most relevant part of the document and generates an intelligent response.

---

## 🧠 How It Works (Under the Hood)

1. **Document Upload**

   * The backend reads and extracts text from your uploaded PDF or TXT file.

2. **Text Chunking + Embeddings**

   * Text is split into smaller chunks.
   * Each chunk is converted into a vector embedding using OpenAI’s Embedding API.

3. **Vector Storage**

   * The embeddings are stored in a local **FAISS** vector index (`faiss_index.bin`).

4. **Question Answering**

   * When a user asks a question, the system finds the most similar text chunks.
   * A final answer is generated using the **LangChain QA model** with OpenAI GPT.

---

## 🧩 Example Workflow

| Step          | Description                                         |
| ------------- | --------------------------------------------------- |
| 📤 Upload     | User uploads a PDF (e.g., “AI_Research_Paper.pdf”)  |
| ⚙️ Processing | Backend extracts text and stores embeddings         |
| 💬 Ask        | User types “What are the key challenges mentioned?” |
| 🧠 Answer     | App retrieves and summarizes the relevant paragraph |

---

## 🧪 Example API Endpoints

| Endpoint      | Method | Description                                |
| ------------- | ------ | ------------------------------------------ |
| `/api/upload` | POST   | Upload a document (PDF/TXT)                |
| `/api/chat`   | POST   | Ask a question about the uploaded document |

---

## 🛠 Troubleshooting

* ❌ *"Error: Module not found ‘fastapi’"*
  → Run `pip install -r requirements.txt`
* ❌ *"CORS policy blocked request"*
  → Ensure FastAPI has CORS middleware (if needed).
* ❌ *"Invalid API key"*
  → Check `.env` file and ensure the key is valid.

---

## 💬 Future Enhancements

* Multi-document upload support
* Chat history persistence
* Voice-based query input
* Improved UI with dark mode

---

## 👨‍💻 Author

**Prakash**
Software Developer | AI & Web Enthusiast

If you found this helpful, ⭐ the repo and feel free to connect!

📧 Email: [prakash4258b@gmail.com](mailto:prakash4258b@example.com)
🌐 LinkedIn: [linkedin.com/in/yourprofile](https://www.linkedin.com/in/prakashbin/)

---

