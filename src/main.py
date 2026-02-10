# Change these in src/main.py
from src.gmail_client import get_gmail_service, fetch_latest_emails
from src.email_parser import parse_email
from src.llm_agent import EmailTriageAgent
from src.validator import validate_output
from src.decision_engine import decide_action
from config.settings import MAX_EMAILS

def main():
    service = get_gmail_service()
    agent = EmailTriageAgent()

    message_ids = fetch_latest_emails(service, MAX_EMAILS)

    for msg_id in message_ids:
        email = parse_email(service, msg_id)

        raw = agent.analyze_email(email)
        parsed = validate_output(raw)

        if not parsed:
            print("❌ Invalid LLM output")
            continue

        action = decide_action(parsed)

        print("EMAIL:", email["subject"])
        print("AI OUTPUT:", parsed)
        print("ACTION:", action)
        print("-" * 50)

if __name__ == "__main__":
    main()
