import httpx
import os
from dotenv import load_dotenv
load_dotenv()


headers = {
    "Authorization": f"Bearer {os.getenv("OPENROUTER_API_KEY")}",
    "HTTP-Referer": "http://localhost:3000",
    "Content-Type": "application/json"
}

def ask_llm(context, question, model="mistralai/mistral-7b-instruct"):
    prompt = f"""Use the context below to answer the question clearly.

Context:
{context}

Question:
{question}
"""

    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    try:
        response = httpx.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers=headers,
            json=data,
            timeout=30
        )

        result = response.json()
        return result.get("choices", [{}])[0].get("message", {}).get("content", "❌ No answer returned.")
    except Exception as e:
        return f"LLM error: {e}"
