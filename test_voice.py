import pyttsx3

engine = pyttsx3.init()

while True:
    text = input("Type something: ")

    if text.lower() == "exit":
        break

    print("Speaking:", text)

    engine.say(text)
    engine.runAndWait()