from flask import Flask, render_template, request
import requests

app = Flask(__name__)

OPENROUTER_API_KEY = "sk-or-..........."
API_URL = "https://openrouter.ai/api/v1/chat/completions"
HEADERS = {
    "Authorization": f"Bearer {OPENROUTER_API_KEY}",
    "Content-Type": "application/json"
}

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    payload = {
        "model": "meta-llama/llama-3-8b-instruct",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_input}
        ]
    }

    try:
        response = requests.post(API_URL, headers=HEADERS, json=payload)
        response.raise_for_status()
        ai_reply = response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        ai_reply = f"Error: {e}"

    return render_template("index.html", user_message=user_input, ai_message=ai_reply)

if __name__ == '__main__':
    app.run(debug=True)
