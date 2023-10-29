import speech_recognition as sr
import pyttsx3

# Initialize the recognizer
recognizer = sr.Recognizer()

# with sr.Microphone() as source:
#     print("Listening...")
#     audio = recognizer.listen(source)

# Recognize the spoken text
try:
    # print(audio, 'audio')
    # text = recognizer.recognize_google(audio)
    # print(text)
    # print(f"You said: {text}")

    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.2)
        audio = recognizer.listen(mic)

        text = recognizer.recognize_google(audio)
        text = text.lower()

        print(text)

    if "open browser" in text:
        import subprocess
        subprocess.Popen(["firefox"])
except sr.UnknownValueError:
    print("Sorry, I could not understand your audio.")
except sr.RequestError as e:
    print(f"Sorry, an error occurred: {str(e)}")
