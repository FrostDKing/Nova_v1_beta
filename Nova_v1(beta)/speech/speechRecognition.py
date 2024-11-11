import speech_recognition as sr
import pyttsx3 as p3

engine=p3.init()
recognizer = sr.Recognizer()

def speak(text):
    engine.setProperty('rate',170)
    engine.setProperty('volume', 0.9)
    voices = engine.getProperty('voices')
    voices = engine.setProperty('voice', voices[5].id)
    engine.say(text) , print(f"Nova:{text}")
    engine.runAndWait()

def listen():
    """Capture audio and convert it to text."""
    with sr.Microphone() as source:
        audio = recognizer.listen(source)
        try:
            text = recognizer.recognize_google(audio)
            print(f"User: {text}")
            return text
        except sr.UnknownValueError:
            speak("Some error occured")
            return None
        except sr.RequestError:
            speak("Could not request results; check your network connection.")
            return None