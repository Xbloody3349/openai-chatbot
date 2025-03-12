import openai
import os

openai.api_key = os.getenv("OPENAI_API_KEY")  # Ensure API key is loaded

client = openai.Client()  # Use the latest client

response = client.chat.completions.create(
    model="gpt-4o",  # Make sure you're using a valid model
    messages=[{"role": "user", "content": "Hello, chatbot!"}]
)

print(response)
