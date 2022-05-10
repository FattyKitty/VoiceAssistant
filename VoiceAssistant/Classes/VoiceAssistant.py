import speech_recognition
import pyttsx3
import json

class VoiceAssistant():
    """Настройки голосового ассистента"""

    def __init__(self, Name, Gender, Language):
        self._Name=Name
        self._Gender=Gender
        self._UseLanguage=Language
        self.engine=pyttsx3.init()

    def GetName(self):
        return self._Name

    def GetGender(self):
        return self._Gender

    def GetLanguage(self):
        return self._UseLanguage

    def SetName(self, Name):
        self._Name=Name
    
    def SetLanguage(self, Language):
        self._UseLanguage=Language

    def SetGender(self, Gender):
        self._Gender=Gender

    def ConfigureAssistant(self):

        voices=self.engine.getProperty('voices')
        self.engine.setProperty('rate', 140)

        if self.GetLanguage()=='en':
            if self.GetGender()=='male':
                self.engine.setProperty('voice', voices[1].id)
            else:
                self.engine.setProperty('voice', voices[2].id)
        elif self.GetLanguage()=='ru':
            if self.GetGender()=='female':
                self.engine.setProperty('voice', voices[0].id)
            else:
                self.engine.setProperty('voice', voices[3].id)

        ToJsonSettings={'AssistantName':self._Name, "AssistantGender:":self._Gender, "AssistantLanguage": self._UseLanguage}

        with open('Json/AssistantSettings.json', 'w', encoding='utf-8') as file:
            file.write(json.dumps(ToJsonSettings, ensure_ascii=False))


    def Say(self, StringToSpeech):
        self.engine.say(str(StringToSpeech))
        self.engine.runAndWait()