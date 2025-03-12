# OpenAI Chatbot (Flask API)

A simple chatbot using OpenAI API and Flask.

## 📌 Features
- Uses OpenAI's GPT-4o model
- REST API for chatbot interactions
- Can be deployed on Railway, Render, or a VPS

## 🚀 Quick Start

### 1️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 2️⃣ Set OpenAI API Key
Rename `.env.example` to `.env` and add your API key:
```
OPENAI_API_KEY=your_api_key_here
```

### 3️⃣ Run Locally
```bash
python app.py
```

### 4️⃣ Deploy to Railway (Fastest)
1. Sign up at [Railway.app](https://railway.app/)
2. Deploy from GitHub
3. Set `OPENAI_API_KEY` as an environment variable

### 5️⃣ Deploy to Render
1. Sign up at [Render.com](https://render.com/)
2. Deploy from GitHub
3. Set `OPENAI_API_KEY` in **Environment Variables**

### 6️⃣ Deploy on a VPS
```bash
ssh root@your-server-ip
git clone https://github.com/your-repo-link.git
cd your-repo
pip install -r requirements.txt
python3 app.py
```

✅ Your chatbot is ready! 🚀
