🧠 Doc Ask App

An AI-powered Chat + Document Assistant that allows you to chat naturally and upload PDFs or text documents to ask context-based questions — all within a single unified web app, built using FastAPI, LangChain, FAISS, and React.

This project replicates the capabilities of Lovable.io’s “Doc Ask App” — but is built entirely from scratch using open-source technologies.

🚀 Features

✅ Unified Chat + Document Reader Interface
✅ Upload PDF or Text files for context
✅ Automatic text extraction and embedding
✅ Ask natural language questions about uploaded content
✅ ChatGPT-like UI built with React + FastAPI backend
✅ FAISS-based semantic search for document retrieval
✅ OpenAI embeddings for intelligent responses

🧰 Tech Stack
Layer	Tools
Frontend	React + Vite + Axios
Backend	FastAPI + LangChain + FAISS + OpenAI
Database / Vector Store	FAISS
Environment	Python 3.10+, Node 18+
🗂️ Folder Structure
doc-ask-app/
├── backend/
│   ├── main.py
│   ├── routes_doc.py          # Document reader API
│   ├── doc_reader.py          # Text extraction & embeddings
│   ├── auth/
│   │   ├── models.py
│   │   ├── routes.py
│   │   ├── schemas.py
│   │   ├── utils.py
│   ├── database.py
│   ├── config.py
│   ├── utils.py
│   ├── requirements.txt
│   └── storage/               # Uploaded files
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
        │   ├── ChatBox.jsx
        │   ├── FileUpload.jsx
        │   └── Loader.jsx
        └── utils/
            └── api.js

⚙️ Backend Setup (FastAPI + LangChain)
1️⃣ Create and activate a virtual environment
cd backend
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

2️⃣ Install dependencies
pip install -r requirements.txt


(Ensure fastapi, uvicorn, pdfminer.six, python-multipart, langchain, openai, and faiss-cpu are installed.)

3️⃣ Add environment variables

Create a .env file inside the backend folder:

OPENAI_API_KEY=your_openai_api_key_here

4️⃣ Start the backend server
uvicorn main:app --reload


Backend runs at → http://127.0.0.1:8000

💻 Frontend Setup (React + Vite)
1️⃣ Install dependencies
cd frontend
npm install

2️⃣ Start the development server
npm run dev


Frontend runs at → http://localhost:5173

🔗 Connecting Frontend & Backend

In your vite.config.js file:

server: {
  proxy: {
    "/api": "http://127.0.0.1:8000"
  }
}


This ensures that frontend API calls like /api/upload and /api/chat go directly to your FastAPI backend.

🧾 Usage Steps

Start both backend & frontend servers.

Open the app in your browser → http://localhost:5173

Upload a .pdf or .txt document.

Ask natural questions — the app retrieves relevant content from your document.

Switch between “Chat” and “Document Reader” seamlessly.

🧠 How It Works
1️⃣ Document Upload

Extracts text from PDF/TXT files.

Splits text into smaller chunks.

Creates embeddings using OpenAI’s API.

2️⃣ Vector Storage

Stores embeddings locally using FAISS Vector Store.

3️⃣ Question Answering

When a user asks a question, the app finds the most relevant text chunks.

LangChain & OpenAI GPT generate a contextual answer.

🧪 API Endpoints
Endpoint	Method	Description
/api/upload	POST	Upload a document (PDF/TXT)
/api/documents	GET	List uploaded documents
/api/doc-question	POST	Ask a question about a document
/api/chat	POST	ChatGPT-like text conversation
💬 Troubleshooting

❌ Error: Module not found ‘fastapi’ → Run pip install -r requirements.txt
❌ CORS policy blocked request → Add CORS middleware in main.py
❌ Invalid API key → Check .env and ensure OpenAI key is valid.

🧩 Future Enhancements

🔹 Multi-document support
🔹 Persistent chat & document history
🔹 Voice-based input
🔹 Dark mode & better UI themes
