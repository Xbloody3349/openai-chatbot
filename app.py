import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)  # Simple web server

# ✅ Set OpenAI API Key from Railway Variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY is missing! Set it in Railway.")

openai.api_key = OPENAI_API_KEY

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")

    # ✅ Use correct OpenAI API call
    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # ✅ Ensures Railway runs this properly
