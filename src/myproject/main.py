from litellm import completion
from dotenv import load_dotenv
import os
from pprint import pprint

# Load environment variables from .env file
load_dotenv()

# Access the API key from the environment
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is not set in the environment or .env file")

os.environ["GEMINI_API_KEY"] = api_key  # Set the key explicitly for the library


def gemini():
    try:    
        response = completion(
            model="gemini/gemini-1.5-flash",
            messages=[{ "content": "Hello, how are you gemini 1.5 flash?","role": "user"}]
        )
        print("\n--- Response from Gemini 1.5 Flash ---")
        pprint(response)  # Pretty print the entire response
        print("\nMessage Content:", response.choices[0].message.content)  # Print the assistant's reply
    except Exception as e:
        print("Error with Gemini 1.5 Flash:", str(e))


def gemini2():
    try:
        response = completion(
            model="gemini/gemini-2.0-flash-exp",
            messages=[{"content": "Hello, how are you gemini 2?", "role": "user"}],
        )
        print("\n--- Response from Gemini 2.0 Flash ---")
        pprint(response)  # Pretty print the entire response
        print("\nMessage Content:", response.choices[0].message.content)  # Print the assistant's reply
    except Exception as e:
        print("Error with Gemini 2.0 Flash:", str(e))

if __name__ == "__main__":
    # response_gemini_1_5=gemini()
    response_gemini_1_5=gemini2()
    # print(response_gemini_1_5.choices[0][messages].content)