# Chat Bot for the Blind

## Overview

Chat Bot for the Blind is a virtual assistant application built using Python programming language. The goal of the application is to assist visually impaired individuals with various tasks such as playing music, telling jokes, searching Wikipedia, fetching news headlines, and more. The application is designed to be easy to use and accessible to users with varying levels of technical experience.

## Features

- Play music: The virtual assistant can play music from popular streaming platforms like YouTube and Spotify.
- Tell me the time: The virtual assistant can tell the current time and date.
- Who is <person name>: The virtual assistant can provide information on a person from Wikipedia.
- Tell me a joke: The virtual assistant can tell a random joke to lighten the mood.
- Tell me the news: The virtual assistant can fetch and read the latest news headlines.

## Requirements

Before running the application, the following Python modules need to be installed:
```
- speech_recognition
- pyttsx3
- pywhatkit
- poe
- datetime
- wikipedia
- pyjokes
- requests
```

Use the code below to install the dependencies needed for running the software:
```
pip install -r requirements.txt
```

## Usage

To start the virtual assistant, simply run the `run_voice_assitance()` function in the code. The assistant will greet you and ask for your command. You can speak any of the following commands:

- Play music
- Tell me the time
- Who is <person name>
- Tell me a joke
- Tell me the news

The assistant will perform the respective task and ask if you want to perform any other task. If you say "yes", it will continue taking commands, else it will terminate.

## Contributing

Contributions are welcome! If you have any suggestions or feature requests, please create an issue in the repository. We welcome contributions from all levels of experience, and appreciate any feedback you may have on the application.
