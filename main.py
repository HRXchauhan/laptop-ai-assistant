import os
import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
#import pyttsx3

from google import genai
from dotenv import load_dotenv


# ----------------------------
# GEMINI SETUP
# ----------------------------

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

chat = client.chats.create(
    model="gemini-3.6-flash"
)


# ----------------------------
# TEXT TO SPEECH
# ----------------------------

#engine = pyttsx3.init()


"""def speak(text):
    print("Assistant:", text)

    engine.say(text)
    engine.runAndWait()

def speak(text):
    text = str(text)

    print("Assistant:", text)

    engine.stop()
    engine.say(text)
    engine.runAndWait()
"""

import subprocess #this is windows TTS(text to speech) 

def speak(text):
    text = str(text)

    print("Assistant:", text)

    safe_text = text.replace('"', "'")

    subprocess.run([
        "powershell",
        "-Command",
        f'Add-Type -AssemblyName System.Speech; '
        f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
        f'$speak.Speak("{safe_text}")'
    ])
# ----------------------------
# VOICE TO TEXT
# ----------------------------

def listen():
    sample_rate = 44100
    duration = 5

    print("\nListening... Speak now.")

    audio = sd.rec(
        int(duration * sample_rate),
        samplerate=sample_rate,
        channels=1
    )

    sd.wait()

    sf.write("voice.wav", audio, sample_rate)

    recognizer = sr.Recognizer()

    with sr.AudioFile("voice.wav") as source:
        audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)

        print("You:", text)

        return text

    except sr.UnknownValueError:
        print("Assistant: Sorry, I could not understand that.")
        return None


# ----------------------------
# MAIN PROGRAM
# ----------------------------

print("================================")
print("     LAPTOP AI ASSISTANT")
print("================================")

speak("Hello. Your AI assistant is ready.")

while True:

    user_input = listen()

    # If speech was not understood
    if user_input is None:
        continue

    # Exit command
    if user_input.lower() == "exit":
        speak("Goodbye!")
        break

    # Send your speech to Gemini
    response = chat.send_message(user_input)

    # Get Gemini's answer
    answer = response.text

    # Print + speak answer
    speak(answer)