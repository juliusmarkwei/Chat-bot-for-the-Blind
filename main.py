import speech_recognition as sr
import pyttsx3
import pywhatkit
import poe
import datetime
import wikipedia
import pyjokes
import requests
import json
import pyaudio

# Insert your api_key here
API_KEY = poe.Client("-")

# this code block initializes the speech recognition and text-to-speech engines
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def greeting_message():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        engine.say("Good Morning Sir or Madam !")

    elif hour >= 12 and hour < 18:
        engine.say("Good Afternoon Sir or Madam !")

    else:
        engine.say("Good Evening Sir or Madam!")
    engine.say('I am your virtual assistant')
    engine.say('How can I assist you')
    engine.runAndWait()


def talk(text):
    engine.say(text)
    engine.runAndWait()


def accept_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            if command is not None:
                command = command.lower()
            if '' in command:
                command = command.replace('', '')
                print(command)

    except sr.UnknownValueError:
        print("Sorry, I could not understand what you said.")
        return None

    except sr.RequestError as e:
        print(f"Sorry, there was a problem with the speech recognition service: {e}")
        return None

    return command


def ask_more():
    engine.say('Is there anything you want me to help you with?')
    engine.runAndWait()
    command = accept_command()
    command = command.lower()
    if 'yes' in command:
        return True
    else:
        engine.say('Okay. Goodbye.')
        engine.runAndWait()
        return False


def command_play_music(command):
    song = command.replace('play', '')
    talk('Playing ' + song)
    pywhatkit.playonyt('playing ' + song)


def command_get_current_time(command):
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('The time is ' + time)
    print('The time is ' + time)


def command_search_wikipedia(command):
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 2)
    print(info)
    talk(info)


def command_tell_joke():
    joke = pyjokes.get_joke()
    talk(joke)
    print(joke)


def command_tell_news():
    # Set the API endpoint URL and parameters
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        # Insert your api_key here
        "apiKey": "-"
    }

    # Make an HTTP GET request to the API endpoint
    response = requests.get(url, params=params)

    # Parse the JSON response
    data = json.loads(response.text)

    # Print the news headlines
    articles = data['articles']
    for article in articles:
        title = article['title']
        print(title)
        engine.say(title)


def process_command(command):
    if 'play' in command:
        command_play_music(command)

    if 'time' in command:
        command_get_current_time(command)

    if 'who is' in command:
        command_search_wikipedia(command)

    if 'joke' in command:
        command_tell_joke

    if 'news' in command:
        command_tell_news()

    if 'how are you' in command:
        talk('I am doing great')
        print('I am doing great')

    else:
        message = command
        print(message)
        for chunk in API_KEY.send_message("capybara", message):
            pass
            response = chunk["text"]
        engine.say(response)


def run_voice_assitance():
    greeting_message()
    while True:
        command = accept_command()
        if command:
            process_command(command)
            if not ask_more():
                break
        else:
            talk('Sorry, I could not understand what you said. Can you repeat that?')


run_voice_assitance()
