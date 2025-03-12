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
    import openai
import os
from flask import Flask, request, jsonify

app = Flask(__name__)

# ✅ Ensure OpenAI API Key is loaded
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
if not OPENAI_API_KEY:
    raise ValueError("🚨 OPENAI_API_KEY is missing! Set it in Railway.")

client = openai.OpenAI(api_key=OPENAI_API_KEY)  # ✅ NEW CLIENT METHOD

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json()
        user_message = data.get("message", "")

        response = client.chat.completions.create(  # ✅ UPDATED OPENAI METHOD
            model="gpt-4o",
            messages=[{"role": "user", "content": user_message}]
        )

        return jsonify({"response": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"error": str(e)}), 500  # ✅ Return error message

# ✅ Ensure the app runs properly
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

        model="gpt-4o",
        messages=[{"role": "user", "content": user_message}]
    )

    return jsonify({"response": response["choices"][0]["message"]["content"]})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # ✅ Ensures Railway runs this properly
