# import speech_recognition as sr
# import pyttsx3 as ttx
# import pywhatkit
# import datetime

# listener = sr.Recognizer
# engine = ttx.init()
# voice = engine.getProperty("voices")
# engine.setProperty("voice","English")

# def talk(text):
#   engine.say(text)
#   engine.runAndWait()
  
# def listen():
#   try:
#       with sr.Microphone() as source:
#           print("Talk")
#           voix = listener.listen(source)
#           command = listener.recognize_google(voix,language = "en-En")
          
#   except:
#     pass
#   return command

# def assistant():
#   command = ecoute()
#   print(command)
#   if 'Hi' in command:
#     talk("hi how are you?")
    
#   elif "I'm chilling how about you?" in command
#       talk('so far I can.t complain,how can i help you')
  
#   elif 'put the song' in command:
#     Artist = command.replace("put the song"," ")
#     print(Artist)
#     pywhatkit.playonyt(Artist)
    
#   elif  'Hour' in command:
#     Hour = datetime.datetime.now().strftime('%H:%M')
#     print("its" + Hour)
    
#   elif 'your name' in command:
#     talk('My name is Spencer Delisma Assitance')
    
# while True:
#   assistant()


import speech_recognition as sr
from gtts import gTTS
import pygame

listener = sr.Recognizer()
pygame.init()

def talk(text):
    tts = gTTS(text=text, lang='en')
    tts.save('output.mp3')
    pygame.mixer.music.load('output.mp3')
    pygame.mixer.music.play()

def listen():
    with sr.Microphone() as source:
        print("Listening...")
        voice = listener.listen(source)
        try:
            command = listener.recognize_google(voice)
            print("User:", command)
            return command.lower()
        except sr.UnknownValueError:
            return "Sorry, I didn't catch that."
        except sr.RequestError:
            return "Sorry, my speech service is currently down."

def assistant():
    command = listen()
    has_spoken_prompt = False

    while True:
        if 'what is my name' in command.lower():
            if not has_spoken_prompt:
                talk("Hi Spencer! How can I assist you?")
                has_spoken_prompt = True
        elif 'bye' in command:
            talk("Goodbye!")
            exit()
        elif 'how are you' in command:
            talk("I'm doing great, thank you!")
        elif 'who do you love the most' in command:
            talk("I love Spencer! He is about to be the best software engineer in the world!")
        else:
            if not has_spoken_prompt:
                talk("I am listening to you, Spencer. Please say something")
                has_spoken_prompt = True

        command = listen()


while True:
    assistant()