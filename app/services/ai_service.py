import requests

from config import GROQ_API_KEY, GROQ_MODEL, BUSINESS_CONTEXT


GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


class AIServiceError(Exception):
    """Yapay zeka servisiyle ilgili hatalar."""
    pass


class AIService:

    def _get_system_prompt(self):
        return BUSINESS_CONTEXT

    def yanit_uret(self, mesaj, gecmis=None):
        # API anahtarı yoksa uygulama çökmek yerine demo modunda çalışır.
        if not GROQ_API_KEY:
            return "Demo modu aktif. Yapay zeka servisi şu anda kullanılamıyor."

        messages = [
            {
                "role": "system",
                "content": self._get_system_prompt()
            }
        ]

        # Önceki sohbet mesajlarını ekle.
        if gecmis:
            messages.extend(gecmis)

        # Yeni kullanıcı mesajını en sona ekle.
        messages.append({
            "role": "user",
            "content": mesaj
        })

        try:
            response = requests.post(
                GROQ_URL,
                headers={
                    "Authorization": f"Bearer {GROQ_API_KEY}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": GROQ_MODEL,
                    "messages": messages
                },
                timeout=30
            )

            response.raise_for_status()

        except requests.RequestException as error:
            print("Groq API hatası:", error)
            raise AIServiceError(
                "Yapay zeka servisine şu anda ulaşılamıyor."
            ) from error

        try:
            data = response.json()
            return data["choices"][0]["message"]["content"].strip()

        except (KeyError, IndexError, TypeError) as error:
            print("Groq cevap okuma hatası:", error)
            raise AIServiceError(
                "Yapay zeka cevabı okunamadı."
            ) from error


ai_service = AIService()


