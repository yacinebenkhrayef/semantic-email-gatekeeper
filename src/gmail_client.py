import os, pickle
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from google.auth.transport.requests import Request
from config.settings import GMAIL_SCOPES

def get_gmail_service():
    creds = None

    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as f:
            creds = pickle.load(f)

    if not creds or not creds.valid:
        flow = InstalledAppFlow.from_client_secrets_file(
            "credentials.json", GMAIL_SCOPES
        )
        creds = flow.run_local_server(port=0)

        with open("token.pickle", "wb") as f:
            pickle.dump(creds, f)

    return build("gmail", "v1", credentials=creds)

def fetch_latest_emails(service, limit):
    results = service.users().messages().list(
        userId="me",
        maxResults=limit
    ).execute()

    return [msg["id"] for msg in results.get("messages", [])]
