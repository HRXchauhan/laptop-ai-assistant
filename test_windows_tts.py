import subprocess

text = "Hello. This is the first sentence."
subprocess.run([
    "powershell",
    "-Command",
    f'Add-Type -AssemblyName System.Speech; '
    f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
    f'$speak.Speak("{text}")'
])

text = "This is the second sentence."
subprocess.run([
    "powershell",
    "-Command",
    f'Add-Type -AssemblyName System.Speech; '
    f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; '
    f'$speak.Speak("{text}")'
])