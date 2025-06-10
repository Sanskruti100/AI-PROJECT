from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# actual OpenRouter API key here
openai.api_key = "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"  # <-- Replace this
openai.api_base = "https://openrouter.ai/api/v1"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ask', methods=['POST'])
def ask():
    user_input = request.form['message']
    try:
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",  # or "mistralai/mistral-7b-instruct", etc.
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_input}
            ]
        )
        ai_reply = response['choices'][0]['message']['content'].strip()
    except Exception as e:
        ai_reply = f"Error: {e}"
    
    return render_template("index.html", user_message=user_input, ai_message=ai_reply)

if __name__ == '__main__':
    app.run(debug=True)



