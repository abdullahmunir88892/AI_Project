import speech_recognition as sr
import pyttsx3
import os
from time import datetime

# Set the Google Cloud credentials path
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'C:/Users/Abdullah/Desktop/Study Material Uni/4th Semester/AI/project jarvis/GCAPI/reference-ether-423800-t2-294e285ea72b.json'

engine = pyttsx3.init()  # Initialize the pyttsx3 engine

def say(text):
    """Function to make the text-to-speech engine say the given text."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen to the user's voice and return the recognized text."""
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        r.pause_threshold = 1  # Set the pause threshold
        print("Listening...")
        try:
            # Listen to the source with a longer phrase_time_limit
            audio = r.listen(source, timeout=10, phrase_time_limit=30)  
            print("Recognizing...")
            query = r.recognize_google_cloud(audio, language="en-US")  # Use Google Cloud Speech-to-Text
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand the audio.")
            return "Sorry, I could not understand the audio."
        except sr.RequestError as e:
            print(f"Could not request results from Google Cloud Speech-to-Text service; {e}")
            return f"Could not request results from Google Cloud Speech-to-Text service; {e}"
        except Exception as e:
            print(f"An error occurred: {e}")
            return f"An error occurred: {e}"
def greet():
    """Function to greet the user based on the current time."""
    hour = datetime.now().hour
    if 5 <= hour < 12:
        say("Good morning Sir")
    elif 12 <= hour < 18:
        say("Good afternoon Sir")
    elif 18 <= hour < 22:
        say("Good evening Sir")
    else:
        say("Good night Sir")

if __name__ == "__main__":
    print("Hello World")
    greet()
    say("I am Jarvis AI and I am here to assist you")
    while True:
        text = listen()
        if text:
            print(f"You said: {text}")
            say(text)
