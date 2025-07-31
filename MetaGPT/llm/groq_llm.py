import os
import requests
from dotenv import load_dotenv
from .base_llm import BaseLLM

load_dotenv()

class GroqLLM(BaseLLM):
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        #self.api_url = "https://api.groq.com/v1/chat/completions"
        self.api_url = "https://api.groq.com/openai/v1/chat/completions" 

    def generate(self, prompt: str) -> str:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }
        data = {
            "model": "llama-3.3-70b-versatile",
            "messages": [{"role": "user", "content": prompt}],
            "max_tokens": 1024,
        }
        response = requests.post(self.api_url, headers=headers, json=data)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"Groq API error: {response.status_code} {response.text}"
