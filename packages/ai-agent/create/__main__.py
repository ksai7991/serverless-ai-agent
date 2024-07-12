import openai
import os

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

        # Extract the generated text from the response
        generated_text = response['choices'][0]['text'].strip()
        return generated_text
    
    except openai.error.AuthenticationError as e:
        # Handle authentication error (e.g., invalid API key)
        return f"Authentication error: {str(e)}"
    
    except openai.error.APIError as e:
        # Handle other API errors
        return f"API error: {str(e)}"
    
    except openai.error.RateLimitError as e:
        # Handle rate limit error
        return f"Rate limit exceeded: {str(e)}"

def main():
    prompt = "Translate the following English text into French: 'Hello, how are you?'"

    generated_text = generate_text(prompt)
    
    print("Generated Text:")
    print(generated_text)

if __name__ == "__main__":
    main()
