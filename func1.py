import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime
import time
import random
import smtplib

# Set the Google Cloud credentials path using a raw string
credentials_path = r'C:\Users\Abdullah\OneDrive - National University of Sciences & Technology\Desktop\Study Material Uni\4th Semester\AI\project jarvis\GCAPI\reference-ether-423800-t2-16c20d2ef8f3.json'

# Check if the credentials file exists
if not os.path.exists(credentials_path):
    raise FileNotFoundError(f"Credentials file not found: {credentials_path}")

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credentials_path

engine = pyttsx3.init()  # Initialize the pyttsx3 engine

def say(text):
    """Function to make the text-to-speech engine say the given text."""
    print(f"Saying: {text}")  # Debug statement
    engine.say(text)
    engine.runAndWait()

def listen():
    """Function to listen to the user's voice and return the recognized text."""
    r = sr.Recognizer()  # Initialize the recognizer
    with sr.Microphone() as source:
        print("Adjusting for ambient noise...")  # Debug statement
        r.adjust_for_ambient_noise(source, duration=0.5)  # Adjust for ambient noise
        r.pause_threshold = 1  # Set the pause threshold
        print("Listening...")  # Debug statement
        try:
            # Listen to the source with a longer phrase_time_limit
            audio = r.listen(source, timeout=10, phrase_time_limit=30)
            print("Recognizing...")  # Debug statement
            query = r.recognize_google_cloud(audio, language="en-in")  # Use Google Cloud Speech-to-Text
            print(f"Recognized: {query}")  # Debug statement
            return query.lower()
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
        say("Good morning Sir wishing you a great day ahead")
    elif 12 <= hour < 18:
        say("Good afternoon Sir may you be enjoying the splashes of heat from sun")
    elif 18 <= hour < 22:
        say("Good evening Sir hoping for one of the best evenings to happen for you")
    else:
        say("May you have a peaceful night ahead Sir")

def greet_friend(name):
    """Function to greet a specific person."""
    say(f"Hello {name}, Sir May you have a great day ahead")

def tell_time():
    """Function to tell the current time."""
    now = datetime.now().strftime("%H:%M")
    say(f"The time is {now}")

def tell_date():
    """Function to tell the current date."""
    today = datetime.now().strftime("%B %d, %Y")
    say(f"Today's date is {today}")

def open_website(site):
    """Function to open a specified website."""
    say(f"Opening {site}")
    webbrowser.open(site)
    time.sleep(10)

def search_google(query):
    """Function to search Google for a query."""
    say(f"Searching Google for {query}")
    webbrowser.open(f"https://www.google.com/search?q={query}")
    time.sleep(10)

def play_music():
    """Function to play music."""
    music_dir = r'C:\Users\Abdullah\OneDrive - National University of Sciences & Technology\Desktop\Study Material Uni\4th Semester\AI\Songs'  # Update this path to your music directory
    songs = os.listdir(music_dir)
    if songs:
        random_song = random.choice(songs)
        os.startfile(os.path.join(music_dir, random_song))
        say(f"Playing {random_song}")
    else:
        say("No music found in your directory")
    
def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('youremail@gmail.com', 'your-password')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()

def process_command(command):
    """Function to process the recognized command."""
    if 'open youtube' in command:
        say("Opening YouTube")
        webbrowser.open("https://www.youtube.com")
        time.sleep(10)  # Wait for 10 seconds before resuming listening
    elif 'open google' in command:
        say("Opening Google")
        webbrowser.open("https://www.google.com")
        time.sleep(10)  # Wait for 10 seconds before resuming listening
    elif 'open wikipedia' in command:
        say("Opening Wikipedia")
        webbrowser.open("https://www.wikipedia.org")
        time.sleep(10)  # Wait for 10 seconds before resuming listening
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")   
        time.sleep(10)
    elif 'open code' in query:
            codePath = r"C:\Users\Abdullah\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Visual Studio Code"
            os.startfile(codePath)
    elif command.startswith('greet '):
        name = command[len('greet '):].strip()
        greet_friend(name)
    elif 'time' in command:
        tell_time()
    elif 'date' in command:
        tell_date()
    elif 'open website' in command:
        site = command.split('open website ')[1].strip()
        open_website(site)
    elif 'open ' in command:
        site = command.split('open ')[1].strip()
        if not site.startswith("https://") and not site.startswith("http://"):
            site = f"https://{site}"
        open_website(site)
    elif 'search google for' in command:
        query = command.split('search google for ')[1].strip()
        search_google(query)
    elif 'play music' in command:
        play_music()
    elif 'jarvis stop' in command:
        say("Okay Sir, Jarvis signing off")
        exit()  # Terminate the program
    elif 'email to harry' in query:
            try:
                say("What should I say?")
                content = listen()
                to = "harryyourEmail@gmail.com"    
                sendEmail(to, content)
                say("Email has been sent!")
            except Exception as e:
                print(e)
                say("Sorry my friend harry bhai. I am not able to send this email") 
    else:
        say("Sorry, I didn't understand that command.")

if __name__ == "__main__":
    greet()
    say("Hello, I am Jarvis AI and I am here to assist you")
    while True:
        print("Waiting for command...")  # Debug statement
        command = listen()
        if command:
            print(f"You said: {command}")
            process_command(command)
        else:
            print("No command recognized.")  # Debug statement
