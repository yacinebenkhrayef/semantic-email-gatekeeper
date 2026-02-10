from google import genai
import os
from src.prompt import EMAIL_TRIAGE_PROMPT

class EmailTriageAgent:
    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def analyze_email(self, email):
        response = self.client.models.generate_content(
            model="gemini-2.5-flash",
            contents=EMAIL_TRIAGE_PROMPT.format(**email),
            config={
                "temperature": 0.2,
                "response_mime_type": "application/json"
            }
        )
        return response.text
