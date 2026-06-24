from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def skill_gap_analysis(resume, jd):

    prompt = f"""
Compare the resume and job description.

Provide:

1. Matching Skills
2. Missing Skills
3. Recommended Skills

Resume:
{resume}

Job Description:
{jd}
"""

    response = client.models.generate_content(
        model="gemini-flash-lite-latest",
        contents=prompt
    )

    return response.text