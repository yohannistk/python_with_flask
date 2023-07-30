
from flask import Flask, request

app = Flask(__name__)

@app.route('/process_string', methods=['GET'])
def process_string():
    string_param = request.args.get('string')
    
    if string_param:
        # Process the string here
        processed_string = string_param.upper()  # Example: convert to uppercase
        return f"Processed string: {processed_string}"
    else:
        return "No string parameter provided."

if __name__ == '__main__':
    app.run()