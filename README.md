🛡️ Semantic Email Gatekeeper

An AI-powered email triage system that classifies, analyzes, and prioritizes emails using controlled LLM reasoning.

“The model never acts directly. It reasons privately, outputs structured data, and all decisions are enforced by deterministic rules. This prevents hallucinated actions and ensures reliability.”

🚀 Features

Gmail API integration

Gemini 2.5 Pro (latest SDK)

Hidden Chain-of-Thought reasoning

Strict JSON outputs

Deterministic decision engine

No AI frameworks

🧠 Design Philosophy
```
This project treats LLMs as reasoning components, not decision-makers.
All actions are rule-based and validated
```
🏗️ Architecture
```
Gmail → Parser → Gemini (Reasoning) → JSON Validation → Decision Engine
```
▶️ Run
```
pip install -r requirements.txt
export GEMINI_API_KEY=your_key
python src/main.py

```