import openai
import os

# Get OpenAI API key from environment variable
openai.api_key = os.getenv('APIKEY')
if not openai.api_key:
    raise ValueError("APIKEY environment variable not set")

def main():
    # Define a prompt
    prompt = "Once upon a time"

    # Use OpenAI API to generate a completion
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=50
    )

    # Get the generated text
    generated_text = response.choices[0].text.strip()

    # Print the generated text
    print("Generated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
