from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Rule-based response generator
def generate_reply(message):
    message = message.lower()
    if "resume" in message:
        return "Sure! Please upload your resume to get instant feedback."
    elif "job" in message:
        return "I can help you find jobs. What kind of job are you looking for?"
    elif "career" in message or "advice" in message:
        return "Based on your skills, I'd suggest looking into Data Science, Web Dev, or Cloud Computing."
    elif "hello" in message or "hi" in message:
        return "Hi there! I'm JobBot. Ask me about resumes, jobs, or careers!"
    else:
        return "Sorry, I didn’t understand that. Try asking about jobs, resumes, or careers!"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json['message']
    reply = generate_reply(user_message)
    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)
