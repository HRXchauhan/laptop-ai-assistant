from google import genai
from dotenv import load_dotenv
import os

# Load API key from .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

# Create a chat session
chat = client.chats.create(
    model="gemini-3.6-flash"
)

print("AI Assistant started!")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Assistant: Goodbye!")
        break

    # Send message while remembering previous messages
    response = chat.send_message(user_input)

    print("Assistant:", response.text)