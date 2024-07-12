import openai
import os
import json

# Set your OpenAI API key
openai.api_key = os.getenv('APIKEY')  # Replace with your actual API key

def generate_text(prompt):
    try:
        # Use OpenAI API to generate text based on the prompt
        response = openai.Completion.create(
            engine="davinci-002",
            prompt=prompt,
            max_tokens=150
        )

        # Ensure the response is in JSON format
        if 'Content-Type' in response.headers and 'application/json' in response.headers['Content-Type']:
            response_json = response.json()
            return json.dumps(response_json, indent=2)
        else:
            return json.dumps({"error": "Unexpected content type"}, indent=2)
    
    except openai.error.AuthenticationError as e:
        # Handle authentication error (e.g., invalid API key)
        return json.dumps({"error": str(e)}, indent=2)
    
    except openai.error.APIError as e:
        # Handle other API errors
        return json.dumps({"error": str(e)}, indent=2)
    
    except openai.error.RateLimitError as e:
        # Handle rate limit error
        return json.dumps({"error": str(e)}, indent=2)

def main():
    prompt = "Translate the following English text into French: 'Hello, how are you?'"
    response_json = generate_text(prompt)
    print(f"Response JSON: {response_json}")

if __name__ == "__main__":
    main()
