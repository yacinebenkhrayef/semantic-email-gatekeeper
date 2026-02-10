import json

def validate_output(text):
    try:
        return json.loads(text)
    except Exception:
        return None
