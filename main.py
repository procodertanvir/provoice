import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes


listener = sr.Recognizer()
bro = pyttsx3.init()
voices = bro.getProperty('voices')
bro.setProperty('voice', voices[1].id)

def talk(text):
    bro.say(text)
    bro.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if 'bro' in command:
                name = command.replace('bro', '')
    except:
        pass
    return  command

def run_bro():
    command = take_command()
    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('The time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        look_for = command.replace('tell me about', '')
        info = wikipedia.summary(look_for, 1)
        print(info)
        talk(info)
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('sorry year, I am in another relationship')
    elif 'single' in command:
        talk('I am not single')
    elif 'thanks' in command:
        talk('Yes, I deserve it')
    elif 'your name' in command:
        talk('I dont know whats my name')
    elif 'my name' in command:
        talk('Tanvir')
    elif 'boss' in command:
        talk('My boss is Mohammad Tanvir Hossain')
    elif 'love' in command:
        talk('Dont be shy, Love is pure')
    elif 'bathroom' in command:
        talk('Yes, you can go')
    elif 'can I help you' in command:
        talk(' You can talk with me')
    else:
        talk('I did not get it but I am going to search it for you')
        pywhatkit.search(command)

while True:
    run_bro()