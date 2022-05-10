import speech_recognition
import pyttsx3
import os
import pyaudio
import urllib.request
from vosk import Model, KaldiRecognizer
from Classes.VoiceAssistant import VoiceAssistant


def OnlineRecognition(AssistantObject):
    StringCommand=None

    Recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        Recognizer.pause_threshold=1

        Recognizer.adjust_for_ambient_noise(mic, duration=1)

        AudioVoice=Recognizer.listen(mic)

        try:
            StringCommand=Recognizer.recognize_google(AudioVoice, language=AssistantObject.GetLanguage()).lower()
        except speech_recognition.UnknownValueError:
            return ' '
    
    return StringCommand

def ConnectToLocalLibrary(AssistantObject):
       if AssistantObject.GetLanguage() == 'ru' and os.path.exists('Model/ru'):
           model=Model("Model/ru")
       elif AssistantObject.GetLanguage() == 'en' and os.path.exists('en'):
           model=Model("Model/en")
       else:
           AssistantObject.Say('Простите, но я не могу получить доступ к функционалу для работы в оффлайн режиме')
       return model


def OfflineRecognition(AssistantObject, model):
    TextData=''
    recognizer=KaldiRecognizer(model, 16000)
    capture=pyaudio.PyAudio()
    stream = capture.open(format=pyaudio.paInt16, channels=1, rate=16000,
                             input=True, frames_per_buffer=8192)
    stream.start_stream()
    while True:
        TextData=stream.read(4096)
        if len(TextData) == 0:
            break
        if recognizer.AcceptWaveform(TextData):
            TextData=recognizer.Result()
            TextData=TextData.partition(': "')[2]
            TextData=TextData.partition('"')[0]
            return TextData
  
def CheckConnection():
    try:
        urllib.request.urlopen('http://mai.ru')
        return True
    except:
        return False
