import speech_recognition as sr
import pyttsx3
import pywhatkit
import poe
import datetime
import wikipedia
import requests
import json
import pyaudio

# Insert your POE api_key here
API_KEY = poe.Client("H0tHBzAj0KkcP41OvZI7bw%3D%3D")

# this code block initializes the speech recognition and text-to-speech engines
# using the libraries SpeechRecognition and pyttsx3
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


# function to greet the user based on the time of day
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


# function to speak a given text using the text-to-speech engine
def talk(text):
    engine.say(text)
    engine.runAndWait()


# function to recognize user's voice command using microphone input
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


# function to ask the user if there are more commands to be processed
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


# This function plays the requested music on YouTube using the PyWhatKit library.
def command_play_music(command):
    song = command.replace('play', '')
    talk('Playing ' + song)
    pywhatkit.playonyt('playing ' + song)


# This function gets the current time and prints it to the console and speaks it using text-to-speech.
def command_get_current_time(command):
    time = datetime.datetime.now().strftime('%I:%M %p')
    talk('The time is ' + time)
    print('The time is ' + time)


# This function searches Wikipedia for information on a given person and returns a summary of the first two sentences
def command_search_wikipedia(command):
    person = command.replace('who is', '')
    info = wikipedia.summary(person, 2)
    print(info)
    talk(info)


# This function fetches a random dad joke from an API and prints it.
def command_tell_joke():
    # Set the API endpoint URL
    url = "https://icanhazdadjoke.com/"

    # Set the headers for the HTTP GET request
    headers = {
        "Accept": "application/json"
    }

    # Make an HTTP GET request to the API endpoint
    response = requests.get(url, headers=headers)

    # Parse the JSON response
    data = json.loads(response.text)

    # Print the joke
    joke = data['joke']
    print(joke)
    talk(joke)


# This function called command_tell_news() which uses the NewsAPI to retrieve the top
# headlines from the US and read them out loud using text-to-speech.
def command_tell_news():
    # Set the API endpoint URL and parameters
    url = "https://newsapi.org/v2/top-headlines"
    params = {
        "country": "us",
        # Insert your api_key here
        "apiKey": "ba1685589f294a28b15df670917523e1"
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


# function to process the user's voice command
def process_command(command):
    if 'play' in command:
        command_play_music(command)

    elif 'time' in command:
        command_get_current_time(command)

    elif 'who is' in command:
        command_search_wikipedia(command)

    elif 'joke' in command:
        command_tell_joke()

    elif 'news' in command:
        command_tell_news()

    elif 'how are you' in command:
        talk('I am doing great')
        print('I am doing great')

    else:
        message = command
        print(message)
        for chunk in API_KEY.send_message("capybara", message):
            pass
            response = chunk["text"]
        engine.say(response)


# function to run the virtual assistant
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
