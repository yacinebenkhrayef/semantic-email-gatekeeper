import sys
import os

# Adds the current directory to the search path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.llm_agent import EmailTriageAgent

fake_email = {
    "sender": "boss@company.com",
    "subject": "Urgent meeting tomorrow",
    "body": "Please confirm before 5pm today."
}

agent = EmailTriageAgent()
result = agent.analyze_email(fake_email)

print(result)
