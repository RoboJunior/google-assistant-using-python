import pywhatkit
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import pyjokes
import webbrowser




listener = sr.Recognizer()
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate', 150)

def talk(text):
        engine.say(text)
        engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening....")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'junior' in command:
                command = command.replace('junior','')
                print(command)
    except:
            pass
    return command

def run_junior():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing '+ song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk("Current time is"+time)
    elif 'find' in command:
        person = command.replace('find','')
        info = wikipedia.summary(person, 2)
        print(info)
        talk(info)
    elif 'hello' in command:
        talk('Hello jeyaraman')
        talk('How are you')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are u mad' in command:
        talk('I wont respond to that')
    elif 'fine' in command:
        talk('Thats great happy to see you like this')
    elif 'youtube' in command:
        talk('opening youtube')
        webbrowser.open_new_tab('https://www.youtube.com/')
    elif 'mail' in command:
        talk('opening mail')
        webbrowser.open_new_tab('https://mail.google.com/mail/u/1/#inbox')
    elif 'about' in command:
        talk('I am a robot i dont get ill hahahaha')
    elif 'your name' in command:
        talk('My name is Junior')
    elif 'my name' in command:
        talk('Your name is jeyaraman')
    elif 'message' in command:
        pywhatkit.sendwhatmsg('+919843958263','i love u paapa',19,58)
        talk("message sent successfully")
    elif 'search' in command:
        src = command.replace('search', '')
        talk(f'searching {src}')
        pywhatkit.search(src)
        talk('here are the results')
    else:
        talk("Can u please repeat i cant understand you")







while True:
    run_junior()
