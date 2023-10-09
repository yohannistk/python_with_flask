from transformers import pipeline
from flask import Flask, request, jsonify

app = Flask(__name__)

pipe = pipeline("text-classification", model="Hello-SimpleAI/chatgpt-detector-roberta")

@app.route('/api/detect-gpt-content', methods=['POST'])
def process_data():
    prompt = request.get_json()['prompt']  # Get JSON data from the request
    return jsonify(pipe(prompt))

if __name__ == '__main__':
    app.run()