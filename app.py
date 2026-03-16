import streamlit as st
from src.helper import extract_text_from_pdf, ask_ai
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

st.set_page_config(page_title="Job Recommender", page_icon=":briefcase:", layout="wide")

st.markdown("""
    <style>
        .stApp { background-color: #0d0d0d; }
        .main .block-container { background-color: #0d0d0d; }
        .stApp, .stMarkdown, p, li, h1, h2, h3, label { color: #e0e0e0 !important; }
        .dark-card {
            background-color: #1a1a1a;
            border: 1px solid #2e2e2e;
            padding: 15px;
            border-radius: 10px;
            color: #e0e0e0;
            margin-bottom: 10px;
        }
        .job-card {
            background-color: #111827;
            border: 1px solid #374151;
            border-left: 4px solid #4f8ef7;
            padding: 15px;
            border-radius: 10px;
            margin-bottom: 12px;
        }
        [data-testid="stFileUploader"] {
            background-color: #1a1a1a;
            border: 1px dashed #444;
            border-radius: 8px;
        }
        .stButton > button {
            background-color: #4f8ef7;
            color: white;
            border: none;
            border-radius: 6px;
            padding: 0.5rem 1.2rem;
        }
        .stButton > button:hover { background-color: #3a7de0; }
        .stSuccess {
            background-color: #1a2e1a !important;
            color: #6fcf6f !important;
            border-radius: 6px;
        }
        hr { border-color: #2e2e2e; }
        a { color: #4f8ef7 !important; }
    </style>
""", unsafe_allow_html=True)

st.title("🤖 AI Job Recommender")
st.markdown("Upload your resume and get AI-powered job recommendations, skill gap analysis, and career roadmap.")

uploaded_file = st.file_uploader("Upload your resume (PDF)", type=["pdf"])

if uploaded_file:
    with st.spinner("Extracting text from your resume..."):
        resume_text = extract_text_from_pdf(uploaded_file)

    with st.spinner("Summarizing your resume..."):
        summary = ask_ai(
            f"Summarize the following resume highlighting the skills, education, and experience:\n\n{resume_text}",
            max_tokens=500
        )

    with st.spinner("Finding skill gaps..."):
        gaps = ask_ai(
            f"Analyze this resume and highlight missing skills, certifications, and experiences needed for better job opportunities:\n\n{resume_text}",
            max_tokens=400
        )

    with st.spinner("Creating Future Roadmap..."):
        road = ask_ai(
            f"Based on the resume, suggest a future roadmap for career growth, including potential job roles, skills to acquire, and certifications to pursue:\n\n{resume_text}",
            max_tokens=400
        )

    st.markdown("---")
    st.header("Resume Summary 📝")
    st.markdown(f"<div class='dark-card'>{summary}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("Skill Gaps 🔍 & Missing Areas")
    st.markdown(f"<div class='dark-card'>{gaps}</div>", unsafe_allow_html=True)

    st.markdown("---")
    st.header("Future Roadmap & Preparation Strategy 🚀")
    st.markdown(f"<div class='dark-card'>{road}</div>", unsafe_allow_html=True)

    st.success("Analysis completed! ✅ Use the insights to enhance your resume and prepare for your job search.")

    if st.button("Get Job Recommendations 🔍"):
        with st.spinner("Extracting job keywords..."):
            keywords = ask_ai(
                f"Based on this resume summary, suggest the best job titles and keywords for searching jobs. "
                f"Give a comma-separated list only, no explanation.\n\nSummary:{summary}",
                max_tokens=100
            )

        search_keywords_clean = keywords.replace("\n", "").strip()
        st.success(f"Extracted Job Keywords: {search_keywords_clean}")

        with st.spinner("Fetching jobs from LinkedIn and Naukri..."):
            linkedin_jobs = fetch_linkedin_jobs(search_keywords_clean, rows=20)
            naukri_jobs = fetch_naukri_jobs(search_keywords_clean, rows=20)

        # ── Display LinkedIn Jobs ──────────────────────────────────
        st.markdown("---")
        st.header("💼 Global Jobs (LinkedIn / Indeed)")

        if linkedin_jobs:
            for job in linkedin_jobs:
                st.markdown(f"""
                <div class='job-card'>
                    <h4 style='color:#4f8ef7; margin:0;'>{job.get('title','N/A')}</h4>
                    <p style='margin:4px 0;'>🏢 <b>{job.get('company','N/A')}</b> &nbsp;|&nbsp; 
                    📍 {job.get('location','N/A')}</p>
                    <p style='font-size:0.85em; color:#9ca3af;'>{job.get('description','')}</p>
                    <a href='{job.get('link','#')}' target='_blank'>🔗 Apply Now</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No global jobs found. Try different keywords.")

        # ── Display Naukri Jobs ────────────────────────────────────
        st.markdown("---")
        st.header("🇮🇳 India Jobs (Naukri / Indeed India)")

        if naukri_jobs:
            for job in naukri_jobs:
                st.markdown(f"""
                <div class='job-card'>
                    <h4 style='color:#4f8ef7; margin:0;'>{job.get('title','N/A')}</h4>
                    <p style='margin:4px 0;'>🏢 <b>{job.get('company','N/A')}</b> &nbsp;|&nbsp; 
                    📍 {job.get('location','N/A')}</p>
                    <p style='font-size:0.85em; color:#9ca3af;'>{job.get('description','')}</p>
                    <a href='{job.get('link','#')}' target='_blank'>🔗 Apply Now</a>
                </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No India jobs found. Try different keywords.")