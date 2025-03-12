import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")

response = openai.client().chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello, chatbot!"}]
)
print(response)
