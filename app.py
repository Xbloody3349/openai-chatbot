import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Ensure OpenAI API Key is loaded
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY is missing! Set it in Railway.")

openai.api_key = OPENAI_API_KEY  # ✅ Correct OpenAI initialization

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        response = openai.client.chat.completions.create(  # ✅ FIXED OpenAI Method
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # ✅ Returns a JSON error

# ✅ Ensure the app runs properly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
