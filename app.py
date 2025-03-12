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

        # ✅ Use the new method for OpenAI v1.0+
        response = openai.Completion.create(  # ✅ New method for v1.0+ API
            model="gpt-4o",
            prompt=user_message,
            max_tokens=100
        )

        return jsonify({"response": response['choices'][0]['text']})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # ✅ Return a JSON error instead of crashing

# ✅ Ensure the app runs properly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
