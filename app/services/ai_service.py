import requests

from config import GROQ_API_KEY, GROQ_MODEL, BUSINESS_CONTEXT

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def ask_ai(user_message):
    if not GROQ_API_KEY:
        raise RuntimeError("Groq API anahtari bulunamadi.")

    try:
        response = requests.post(
            GROQ_URL,
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": GROQ_MODEL,
                "messages": [
                    {
                        "role": "system",
                        "content": BUSINESS_CONTEXT
                    },
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            },
            timeout=30
        )

        response.raise_for_status()

        data = response.json()
        return data["choices"][0]["message"]["content"].strip()

    except requests.RequestException as error:
        print("Groq API hatasi:", error)
        raise RuntimeError("Yapay zeka servisine ulasilamadi.") from error

    except (KeyError, IndexError, TypeError) as error:
        print("Groq cevap okuma hatasi:", error)
        raise RuntimeError("Yapay zeka cevabi okunamadi.") from error