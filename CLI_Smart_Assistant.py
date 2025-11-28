import speech_recognition as sr
import pyttsx3
import os
import webbrowser
import datetime

# Initialize the speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# Voice output function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    print(f"Assistant: {audio}")

# Listens to mic and returns string
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1 # Waits 1 sec before considering a phrase complete
        audio = r.listen(source)

    try:
        print("Recognizing...")
        # language='en-in' interprets English with an Indian accent preference
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()

def main():
    speak("System is online. How can I help you?")
    
    while True:
        query = take_command()

        # Logic for executing tasks based on query
        if 'open notepad' in query:
            speak("Opening Notepad")
            os.system('notepad.exe')

        elif 'open command prompt' in query:
            speak("Opening Command Prompt")
            os.system('start cmd')

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'play music' in query:
            music_dir = 'C:\\Users\\Public\\Music' # Change this to your path
            songs = os.listdir(music_dir)
            if songs:
                os.startfile(os.path.join(music_dir, songs[0]))
            else:
                speak("No music files found.")

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")

        elif 'shutdown system' in query:
            speak("Shutting down the system in 5 seconds")
            # Warning: This will actually shut down your PC
            os.system("shutdown /s /t 5") 

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye!")
            break

if __name__ == "__main__":
    main()