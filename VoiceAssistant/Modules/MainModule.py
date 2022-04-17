import Modules.SpeechRecognitionModule as SystemModule
import Modules.CommandClassificatorModule as Classificator
from vosk import Model, KaldiRecognizer
from Classes.VoiceAssistant import VoiceAssistant

if __name__=='__main__':
    RecognizedSpeechCommand='' #string for speech recognized and translated to a text form

    Assistant=VoiceAssistant(Name='помощник', Gender='male', UseLanguage='ru')
    Assistant.ConfigureAssistant()

    LocalModelConnection=SystemModule.ConnectToLocalLibrary(Assistant)
    while True:
        if SystemModule.CheckConnection():
            RecognizedSpeechCommand=SystemModule.OnlineRecognition(Assistant)
        else:
            RecognizedSpeechCommand=SystemModule.OfflineOfflineRecognition(Assistant)
        print(RecognizedSpeechCommand)
        Classificator.CommandClassificator(RecognizedSpeechCommand, Assistant)