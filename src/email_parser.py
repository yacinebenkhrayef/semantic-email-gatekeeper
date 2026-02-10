import base64

def parse_email(service, message_id):
    message = service.users().messages().get(
        userId="me",
        id=message_id,
        format="full"
    ).execute()

    headers = message["payload"]["headers"]
    subject, sender = "", ""

    for h in headers:
        if h["name"] == "Subject":
            subject = h["value"]
        elif h["name"] == "From":
            sender = h["value"]

    body = ""
    parts = message["payload"].get("parts", [])

    for part in parts:
        if part["mimeType"] == "text/plain":
            data = part["body"]["data"]
            body = base64.urlsafe_b64decode(data).decode("utf-8")

    return {
        "sender": sender,
        "subject": subject,
        "body": body.strip()
    }
