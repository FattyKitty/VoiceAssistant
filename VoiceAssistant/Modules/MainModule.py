import Modules.SpeechRecognitionModule as SRM
import Modules.CommandClassificatorModule as Classificator
from vosk import Model, KaldiRecognizer
from Classes.VoiceAssistant import VoiceAssistant

if __name__=='__main__':
    RecognizedSpeechCommand='' #string for speech recognized and translated to a text form

    Assistant=VoiceAssistant(Name='ассистент', Gender='male', Language='ru')
    Assistant.ConfigureAssistant()

    LocalModelConnection=SRM.ConnectToLocalLibrary(Assistant)
    while True:
        if SRM.CheckConnection():
            RecognizedSpeechCommand=SRM.OnlineRecognition(Assistant)
        else:
            RecognizedSpeechCommand=SRM.OfflineRecognition(Assistant, LocalModelConnection)
        print(RecognizedSpeechCommand)
        Classificator.CommandClassificator(RecognizedSpeechCommand, Assistant)