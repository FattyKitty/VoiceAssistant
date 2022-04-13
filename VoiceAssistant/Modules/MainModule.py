import Modules.SystemModule as SystemModule
from vosk import Model, KaldiRecognizer
from Classes.VoiceAssistant import VoiceAssistant

if __name__=='__main__':
    RecognizedSpeechCommand='' #string for speech recognized and translated to a text form

    Assistant=VoiceAssistant(Name='ассистент', Gender='male', UseLanguage='ru')
    Assistant.ConfigureAssistant()

    LocalModelConnection=SystemModule.ConnectToLocalLibrary(Assistant)
    while True:
        if SystemModule.CheckConnection():
            RecognizedSpeechCommand=SystemModule.OnlineRecognition(Assistant)
        else:
            RecognizedSpeechCommand=SystemModule.OfflineOfflineRecognition(Assistant)
        print(RecognizedSpeechCommand)
        SystemModule.CommandParser(RecognizedSpeechCommand, Assistant)