# ollama_client.py

import ollama
from config import OLLAMA_MODEL


def chat(prompt: str) -> str:
    """
    Send prompt to Ollama and return response.
    """

    try:
        response = ollama.chat(
            model=OLLAMA_MODEL,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response["message"]["content"]

    except Exception as e:
        return f"OLLAMA ERROR: {e}"