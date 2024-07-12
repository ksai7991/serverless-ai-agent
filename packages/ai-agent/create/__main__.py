import openai
import os

# Get OpenAI API key from environment variable
openai.api_key = os.getenv('APIKEY')

def main(args):
    name = args.get("name", "stranger")
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
    
    print(full_message)
    return {"body": full_message}

# Simulate a request for testing
if __name__ == "__main__":
    test_args = {"name": "Alice"}  # Example input arguments
    response = main(test_args)
    print("Final Response:", response)
