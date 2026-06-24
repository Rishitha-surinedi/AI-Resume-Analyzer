from google import genai
from dotenv import load_dotenv
import os

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

def generate_questions(jd):
    prompt = f"""
Generate:

- 5 Technical Questions
- 3 Behavioral Questions
- 2 Scenario-Based Questions

Based on this Job Description:

{jd}
"""

    try:
        response = client.models.generate_content(
            model="gemini-flash-lite-latest",
            contents=prompt
        )
        return response.text

    except Exception as e:
        return f"Error occurred: {str(e)}"