from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import pyttsx3
import speech_recognition
import spacy.cli
import platform
import subprocess

CONFIDENCE_THRESHOLD = 0.7

spacy.cli.download('en_core_web_sm')  # Ensure the model is downloaded

def assistant(audio):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voices', voices[1].id)
    engine.say(audio)
    engine.runAndWait()

def SpeakText(command):
    engine = pyttsx3.init()
    engine.say(command)
    print(command)
    engine.runAndWait()

class VoiceChatBot(ChatBot):
    def speak(self, text):
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        engine.setProperty('voices', voices[1].id)
        engine.say(text)
        engine.runAndWait()

    def get_response(self, statement=None, **kwargs):
        response = super().get_response(statement, **kwargs)
        if response.confidence >= CONFIDENCE_THRESHOLD:
            SpeakText(response.text)
        else:
            bot.speak("I'm not sure about that.")
class Tagger:
    def __init__(self, language=None):
        self.nlp = spacy.load('en_core_web_sm')

# Rest of your code...



bot = VoiceChatBot('Example ChatBot')

trainer = ChatterBotCorpusTrainer(bot)

# Train the chat bot with the entire English corpus
# Uncomment the line below if you want to use the English corpus
# trainer.train('chatterbot.corpus.english')

trainer.train('./data/english/')

recognizer = speech_recognition.Recognizer()

while True:
    try:
        with speech_recognition.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source)
            recognizer_function = recognizer.recognize_google
            result = recognizer_function(audio)
            bot.get_response(text=result)
    except speech_recognition.UnknownValueError:
        bot.speak('I am sorry, I could not understand that.')
    except speech_recognition.RequestError as e:
        message = 'My speech recognition service has failed. {0}'
        bot.speak(message.format(e))
    except (KeyboardInterrupt, EOFError, SystemExit):
        # Press ctrl-c or ctrl-d on the keyboard to exit
        break
