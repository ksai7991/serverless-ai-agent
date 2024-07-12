import logging
import openai

# Configure logging
logging.basicConfig(level=logging.INFO)

# Set your OpenAI API key
openai.api_key = 'sk-proj-SKDj26jUcChRCiG4O5bKT3BlbkFJbA3rWtdkV6oOpe6abBnJ'

def main(args):
    try:
        # Log the received arguments
        logging.info("Received arguments: %s", args)

        # Get the name from arguments or default to 'stranger'
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

        # Log the response
        logging.info("Response: %s", full_message)
        print(full_message)

        return {"body": full_message}

    except Exception as e:
        logging.error("Error occurred: %s", str(e))
        return {"body": "An error occurred."}

# Simulate a request for testing
if __name__ == "__main__":
    test_args = {"name": "Alice"}  # Example input arguments
    response = main(test_args)
    print("Final Response:", response)
