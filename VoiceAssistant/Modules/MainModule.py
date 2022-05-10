import Modules.SpeechRecognitionModule as SRM
import Modules.CommandClassificatorModule as Classificator
from vosk import Model, KaldiRecognizer
from Classes.VoiceAssistant import VoiceAssistant
import json

if __name__=='__main__':
    RecognizedSpeechCommand='' #string for speech recognized and translated to a text form

    with open('Json/AssistantSettings.json', 'r', encoding='utf-8') as file:
        FileContent=file.read()
        Template=json.loads(FileContent)
        
    AssistantName, AssistantGender, AssistantLanguage=Template.values()

    Assistant=VoiceAssistant(Name=AssistantName, Gender=AssistantGender, Language=AssistantLanguage)
    Assistant.ConfigureAssistant()


    LocalModelConnection=SRM.ConnectToLocalLibrary(Assistant)
    Assistant.Say('Голосовой ассистент {} готов к работе' .format(Assistant.GetName()))
    while True:
        if SRM.CheckConnection():
            RecognizedSpeechCommand=SRM.OnlineRecognition(Assistant)
        else:
            RecognizedSpeechCommand=SRM.OfflineRecognition(Assistant, LocalModelConnection)
        print(RecognizedSpeechCommand)
        Classificator.CommandClassificator(RecognizedSpeechCommand, Assistant)