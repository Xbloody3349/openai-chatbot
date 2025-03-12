import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)  # Flask app to handle requests

# Load API key from Railway environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY is missing! Set it in Railway.")

openai.api_key = OPENAI_API_KEY

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()  # Get JSON from request
        user_message = data.get("message", "")

        response = openai.ChatCompletion.create(
            model="gpt-4o",  # Make sure your model is correct
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"response": response["choices"][0]["message"]["content"]})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # Ensure it runs on Railway
