import sounddevice as sd
import soundfile as sf
import speech_recognition as sr
import pyttsx3

# Speaker test
engine = pyttsx3.init()
engine.say("Hello. Your AI assistant voice system is working.")
engine.runAndWait()

# Record audio
print("Testing microphone...")
print("Speak now for 5 seconds...")

sample_rate = 44100
duration = 5

audio = sd.rec(
    int(duration * sample_rate),
    samplerate=sample_rate,
    channels=1
)

sd.wait()

# Save recorded audio temporarily
sf.write("voice.wav", audio, sample_rate)

# Convert speech to text
recognizer = sr.Recognizer()

with sr.AudioFile("voice.wav") as source:
    audio_data = recognizer.record(source)

try:
    text = recognizer.recognize_google(audio_data)
    print("You said:", text)

except sr.UnknownValueError:
    print("Sorry, I could not understand you.")