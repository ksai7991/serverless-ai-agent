import os
import openai
from flask import Flask, request, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Get OpenAI API key from environment variable
openai.api_key = os.getenv('APIKEY')
if not openai.api_key:
    raise ValueError("APIKEY environment variable not set")

@app.route('/greet', methods=['POST'])
def greet():
    try:
        # Get JSON data from the request
        data = request.get_json()
        name = data.get("name", "stranger")
        greeting = f"Hello {name}!"

        # Use OpenAI API to generate a creative continuation
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{greeting} How are you doing today?",
            max_tokens=50
        )

        # Get the generated text
        ai_response = response.choices[0].text.strip()
        full_message = f"{greeting} How are you doing today? {ai_response}"

        # Return the response as JSON
        return jsonify({"body": full_message})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
