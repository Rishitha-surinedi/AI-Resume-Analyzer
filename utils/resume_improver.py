from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def improve_resume(resume_text):

    prompt = f"""
Analyze this resume and provide:

1. ATS Improvements
2. Missing Skills
3. Missing Sections
4. Better Resume Bullet Points

Resume:

{resume_text}
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error occurred: {str(e)}"