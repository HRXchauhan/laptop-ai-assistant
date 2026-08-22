from google import genai
from dotenv import load_dotenv
import os

# Load variables from the .env file
load_dotenv()

# Get the API key from .env
api_key = os.getenv("GEMINI_API_KEY")

# Create the Gemini AI client
client = genai.Client(api_key=api_key)

print("AI Assistant started!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_input
    )

    print("Assistant:", response.text)