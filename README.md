# 🧠 Text Summarizer — LangChain + Gemini + FastAPI

A generative AI web application that summarizes text using Google's Gemini model, built with LangChain and FastAPI.

## 🌐 Live Demo

- **Frontend:** [https://mnpro98.github.io/Generative-AI-Application-with-LangChain/](https://mnpro98.github.io/Generative-AI-Application-with-LangChain/)
- **Backend API:** [https://generative-ai-application-with-langchain.onrender.com](https://generative-ai-application-with-langchain.onrender.com)

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, Vanilla JS |
| Backend | FastAPI, Python |
| AI / LLM | Google Gemini via LangChain |
| Hosting (Frontend) | GitHub Pages |
| Hosting (Backend) | Render |

---

## 📁 Project Structure

```
├── main.py               # FastAPI app and route definitions
├── services/
│   ├── app_logic.py      # Summarization chain logic
│   └── gemini_llm.py     # Gemini LLM factory function
├── index.html            # Frontend UI
├── requirements.txt      # Python dependencies
└── .env                  # Environment variables (not committed)
```

---

## 🚀 Running Locally

### 1. Clone the repository
```bash
git clone https://github.com/mnpro98/Generative-AI-Application-with-LangChain.git
cd Generative-AI-Application-with-LangChain
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Set up environment variables
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

You can get a free API key at [aistudio.google.com](https://aistudio.google.com).

### 5. Start the backend
```bash
uvicorn main:app --reload
```

### 6. Open the frontend
Open `index.html` in your browser, or serve it locally with:
```bash
python -m http.server 3000
```

Then visit `http://localhost:3000`.

---

## 📡 API Reference

### `POST /summarize`

Summarizes the provided text.

**Request body:**
```json
{
  "text": "Your long text here..."
}
```

**Response:**
```json
{
  "message": "Summarized text here."
}
```

---

## ⚙️ Deployment

### Backend — Render
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port 8000`
- Add `GOOGLE_API_KEY` as an environment variable in the Render dashboard

### Frontend — GitHub Pages
- Go to **Settings → Pages**
- Set source to **main** branch, **/ (root)** folder
- Update `API_URL` in `index.html` to point to your Render backend URL

---

## 📝 License

MIT License — feel free to use and modify this project.
