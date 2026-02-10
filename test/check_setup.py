import os

files = ["credentials.json", ".env", "venv"]
for f in files:
    if os.path.exists(f):
        print(f"✔ {f} found.")
    else:
        print(f"✘ {f} MISSING!")

if os.getenv("GEMINI_API_KEY"):
    print("✔ Gemini API Key is set in environment.")
else:
    print("✘ Gemini API Key NOT found. Run: $env:GEMINI_API_KEY='your_key'")