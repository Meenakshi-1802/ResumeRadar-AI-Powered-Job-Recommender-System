# 🎯 ResumeRadar — AI-Powered Job Recommender System

<div align="center">

![ResumeRadar Banner](https://img.shields.io/badge/ResumeRadar-AI%20Job%20Recommender-4f8ef7?style=for-the-badge\&logo=robot\&logoColor=white)

[![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=flat-square\&logo=python\&logoColor=white)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.55-FF4B4B?style=flat-square\&logo=streamlit\&logoColor=white)](https://streamlit.io)
[![Groq](https://img.shields.io/badge/Groq-LLaMA%203-00A67E?style=flat-square\&logo=groq\&logoColor=white)](https://groq.com)
[![RapidAPI](https://img.shields.io/badge/JSearch-RapidAPI-0055DA?style=flat-square\&logo=rapidapi\&logoColor=white)](https://rapidapi.com)

* An end-to-end Generative AI application that analyzes resumes, detects skill gaps, generates a career roadmap, and recommends real-time job opportunities.*

</div>

---

# 🎬 Live Application

Try the deployed application here:

🚀 https://resumeradar-ai-powered-job-recommender-system-xanbqr3bwbl266r8.streamlit.app/

Upload your resume and instantly get:

• AI Resume Summary
• Skill Gap Analysis
• Career Roadmap
• Real-time Job Recommendations

---

# ⭐ Project Highlights

• Built using **Generative AI (LLaMA 3 via Groq API)**
• Real-time job search using **JSearch API (RapidAPI)**
• Resume parsing with **PyMuPDF**
• Intelligent keyword extraction for job matching
• Deployable AI tool server using **MCP Protocol**
• Clean dark UI built with **Streamlit**

---

# 📌 Problem Statement

Job seekers — especially freshers — face three major challenges:

1️⃣ **Skill Blindspot**
They don't know which skills they lack for their desired job role.

2️⃣ **Manual Job Search**
Searching multiple job platforms takes time.

3️⃣ **No Career Direction**
Most people don't have a clear roadmap to improve their profile.

**ResumeRadar solves these problems using Generative AI + Real-time Job APIs.**

---

# 📸 Application Screenshots

### Resume Upload

<img src="https://github.com/user-attachments/assets/5564b7fe-ed34-4790-8a9c-6e208c759279" width="100%">

---

### AI Resume Analysis

<img src="https://github.com/user-attachments/assets/368b7f5b-3033-47fa-9a4b-ed03ea012bac" width="100%">

---

### Job Recommendations

<img src="https://github.com/user-attachments/assets/4e29e031-0418-44ef-abea-bc77fe516696" width="100%">

---

# 🏗 System Architecture

```
User Uploads Resume
        │
        ▼
Streamlit Web Application
        │
        ├── PyMuPDF → Extract Resume Text
        │
        ├── Groq API (LLaMA 3)
        │      ├ Resume Summary
        │      ├ Skill Gap Analysis
        │      └ Career Roadmap
        │
        └── JSearch API
               └ Fetch Real Job Listings
```

---

# 🛠 Tech Stack

| Layer          | Technology         |
| -------------- | ------------------ |
| Frontend       | Streamlit          |
| AI Model       | LLaMA 3 (Groq API) |
| Resume Parsing | PyMuPDF            |
| Job Data       | JSearch API        |
| Language       | Python             |
| Environment    | python-dotenv      |

---

# 📁 Project Structure

```
ResumeRadar/
│
├── .streamlit/
│   └── config.toml
│
├── src/
│   ├── helper.py
│   └── job_api.py
│
├── app.py
├── mcp_server.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Setup & Installation

### Clone the Repository

```bash
git clone https://github.com/Meenakshi-1802/ResumeRadar.git
cd ResumeRadar
```

---

### Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```
.\.venv\Scripts\activate
```

Mac/Linux

```
source .venv/bin/activate
```

---

### Install Dependencies

```
pip install -r requirements.txt
```

---

### Configure Environment Variables

Create `.env`

```
GROQ_API_KEY=your_groq_api_key
RAPIDAPI_KEY=your_rapidapi_key
```

---

### Run Application

```
streamlit run app.py
```

Open

```
http://localhost:8501
```

---

# 🔮 Future Improvements

• Resume ATS score checker

• Job bookmarking system

• Interview preparation suggestions

• Email job alerts

• Multi-language resume support

• Docker deployment

---

## ⭐ If you found this project useful, please give it a **star**.
