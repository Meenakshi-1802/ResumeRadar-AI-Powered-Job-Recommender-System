from mcp.server.fastmcp import FastMCP
from src.helper import extract_text_from_pdf, ask_ai
from src.job_api import fetch_linkedin_jobs, fetch_naukri_jobs

# Initialize MCP server
mcp = FastMCP("Job Recommender")
@mcp.tool()
def analyze_resume(resume_text: str) -> dict:
    """
    Analyze a resume and return summary, skill gaps, and roadmap.
    
    Args:
        resume_text: The full text content of the resume
    
    Returns:
        Dictionary with summary, gaps, and roadmap
    """
    summary = ask_ai(
        f"Summarize this resume highlighting skills, education, and experience:\n\n{resume_text}",
        max_tokens=500
    )
    gaps = ask_ai(
        f"Analyze this resume and highlight missing skills, certifications needed for better jobs:\n\n{resume_text}",
        max_tokens=400
    )
    roadmap = ask_ai(
        f"Suggest a future career roadmap including job roles, skills to acquire, certifications:\n\n{resume_text}",
        max_tokens=400
    )
    return {
        "summary": summary,
        "skill_gaps": gaps,
        "roadmap": roadmap
    }

@mcp.tool()
def get_job_recommendations(keywords: str, location: str = "India") -> dict:
    """
    Fetch job recommendations based on keywords.
    
    Args:
        keywords: Job title or skill keywords (e.g. "data scientist python")
        location: Target location (default: India)
    
    Returns:
        Dictionary with linkedin_jobs and naukri_jobs lists
    """
    linkedin_jobs = fetch_linkedin_jobs(keywords, rows=10)
    naukri_jobs = fetch_naukri_jobs(keywords, rows=10)
    
    return {
        "linkedin_jobs": linkedin_jobs,
        "naukri_jobs": naukri_jobs,
        "total": len(linkedin_jobs) + len(naukri_jobs)
    }

@mcp.tool()
def extract_job_keywords(resume_text: str) -> str:
    """
    Extract best job search keywords from a resume.
    
    Args:
        resume_text: The full text content of the resume
    
    Returns:
        Comma-separated list of job keywords
    """
    keywords = ask_ai(
        f"Based on this resume, suggest the best job titles and keywords for job search. "
        f"Return comma-separated list only, no explanation:\n\n{resume_text}",
        max_tokens=100
    )
    return keywords.strip()

@mcp.tool()
def get_skill_gaps(resume_text: str, target_role: str) -> str:
    """
    Get skill gaps for a specific target job role.
    
    Args:
        resume_text: The full text content of the resume
        target_role: The job role to target (e.g. "Data Scientist")
    
    Returns:
        Detailed skill gap analysis
    """
    gaps = ask_ai(
        f"Compare this resume against requirements for {target_role} role. "
        f"List specific missing skills, tools, certifications needed:\n\n{resume_text}",
        max_tokens=400
    )
    return gaps


@mcp.tool()
def get_career_roadmap(resume_text: str, target_role: str = None) -> str:
    """
    Generate a personalized career roadmap.
    
    Args:
        resume_text: The full text content of the resume
        target_role: Optional specific target role
    
    Returns:
        Step-by-step career roadmap
    """
    role_context = f"targeting {target_role}" if target_role else "for general career growth"
    roadmap = ask_ai(
        f"Create a detailed 6-month career roadmap {role_context} based on this resume. "
        f"Include: skills to learn, projects to build, certifications to get:\n\n{resume_text}",
        max_tokens=500
    )
    return roadmap

if __name__ == "__main__":
    print("🚀 Job Recommender MCP Server starting...")
    mcp.run(transport="stdio")