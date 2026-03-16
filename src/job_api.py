import requests
import os
from dotenv import load_dotenv

load_dotenv()

RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

def fetch_linkedin_jobs(keywords: str, rows: int = 10) -> list:
    """Fetch global jobs via JSearch API (RapidAPI)"""
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": keywords,
        "page": "1",
        "num_pages": "2",
        "employment_types": "FULLTIME"
    }
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        jobs = response.json().get("data", [])[:rows]
        return [
            {
                "title": j.get("job_title", "N/A"),
                "company": j.get("employer_name", "N/A"),
                "location": j.get("job_city", "Remote"),
                "description": j.get("job_description", "")[:200] + "...",
                "link": j.get("job_apply_link", "#"),
                "source": "LinkedIn / Indeed"
            }
            for j in jobs
        ]
    except Exception as e:
        print(f"[LinkedIn fetch error]: {e}")
        return []


def fetch_naukri_jobs(keywords: str, rows: int = 10) -> list:
    """Fetch India jobs via JSearch API (RapidAPI)"""
    url = "https://jsearch.p.rapidapi.com/search"
    headers = {
        "X-RapidAPI-Key": RAPIDAPI_KEY,
        "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
    }
    params = {
        "query": f"{keywords} India",
        "page": "1",
        "num_pages": "2",
        "employment_types": "FULLTIME"
    }
    try:
        response = requests.get(url, headers=headers, params=params, timeout=10)
        jobs = response.json().get("data", [])[:rows]
        return [
            {
                "title": j.get("job_title", "N/A"),
                "company": j.get("employer_name", "N/A"),
                "location": j.get("job_city", "India"),
                "description": j.get("job_description", "")[:200] + "...",
                "link": j.get("job_apply_link", "#"),
                "source": "Naukri / Indeed India"
            }
            for j in jobs
        ]
    except Exception as e:
        print(f"[Naukri fetch error]: {e}")
        return []