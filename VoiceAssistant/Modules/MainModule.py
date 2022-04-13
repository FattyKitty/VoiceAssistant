import speech_recognition
import pyttsx3
import os
import pyaudio
import urllib.request
from vosk import Model, KaldiRecognizer
from Classes.VoiceAssistant import VoiceAssistant


def OnlineRecognition(ClassObject):
    StringCommand=None

    Recognizer = speech_recognition.Recognizer()

    with speech_recognition.Microphone() as mic:
        Recognizer.pause_threshold=1

        Recognizer.adjust_for_ambient_noise(mic, duration=1)

        AudioVoice=Recognizer.listen(mic)

        try:
            StringCommand=Recognizer.recognize_google(AudioVoice, language="ru")
            ClassObject.Say(StringCommand)
        except speech_recognition.UnknownValueError:
            ClassObject.Say('Не понимаю, что вы сказали, повторите, пожалуйста')
            OnlineRecognition(ClassObject)
            StringCommand=OnlineRecognition(ClassObject)
    
    return StringCommand

def ConnectToLocalLibrary(ClassObject):
       if ClassObject.GetLanguage() == 'ru' and os.path.exists('Model/ru'):
           model=Model("Model/ru")
       elif ClassObject.GetLanguage() == 'en' and os.path.exists('en'):
           model=Model("Model/en")
       else:
           ClassObject.Say('Простите, но я не могу получить доступ к функционалу для работы в оффлайн режиме')
       return model


def OfflineRecognition(ClassObject, model):
       TextData=None

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
               print(TextData)
def CheckConnection():
    try:
        urllib.request.urlopen('http://mai.ru')
        return True
    except:
        return False
     

if __name__=='__main__':
  
    Assistant=VoiceAssistant(Name='Ассистент', Gender='male', UseLanguage='ru')
    Assistant.ConfigureAssistant()

    LocalModelConnection=ConnectToLocalLibrary(Assistant)

    while CheckConnection():
        OnlineRecognition(Assistant)
    else:
        OfflineRecognition(Assistant, LocalModelConnection)