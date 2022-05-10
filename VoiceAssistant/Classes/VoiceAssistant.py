import speech_recognition
import pyttsx3

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

        if self._UseLanguage=='en':
            if self._Gender=='male':
                self.engine.setProperty('voice', voices[1].id)
            else:
                self.engine.setProperty('voice', voices[2].id)
        elif self._UseLanguage=='ru':
            if self._Gender=='female':
                self.engine.setProperty('voice', voices[0].id)
            else:
                self.engine.setProperty('voice', voices[3].id)


    def Say(self, StringToSpeech):
        self.engine.say(str(StringToSpeech))
        self.engine.runAndWait()