import random as rnd
import Modules.SpeechRecognitionModule as SRM

def SayHelloToUser(AssistantObject, *args: tuple):
    AssistantObject.Say('Приветствую вас, пользователь')


def MakeUserHappy(AssistantObject, *args: tuple):
    ListOfMotivators=list(['У вас все получится!', 
                          'Вы лучший!', 'Лучше, чем вы не бывает людей',
                         'Что бы вы не делали, помните, что ваш ассистент всегда с вами',
                         'Только скажите как я могу вам помочь, и я это сделаю',
                         'Если вам кажется, что ничего не получается, помните, что есть люди, которые готовы вам помочь'])

    NumberOfMotivationalSpeech=rnd.randrange(0, len(ListOfMotivators))
    AssistantObject.Say(ListOfMotivators[NumberOfMotivationalSpeech])

def SayGoodbyeToUser(AssitantObject, AdditionalArgs):
    AssitantObject.Say('До свидания пользователь')
    exit()


def SetNewProfile(AssistantObject, *args: tuple):
    AssistantObject.Say('Какие параметры конфигурации вы хотите изменить? Если параметров несколько, называйте их без использования союза и')

    LocalModelConnection=SRM.ConnectToLocalLibrary(AssistantObject)
    AnswerFromUser=SRM.OfflineRecognition(AssistantObject, LocalModelConnection)
    print(AnswerFromUser)

    AnswerFromUser=AnswerFromUser.split(' ')

    NewName=AssistantObject.GetName()
    NewGender=AssistantObject.GetGender()
    NewLang=AssistantObject.GetLanguage()

    for Parameter in AnswerFromUser:
        if Parameter=='имя':
            AssistantObject.Say('Дайте мне новое имя')
            NewName=SRM.OfflineRecognition(AssistantObject, LocalModelConnection)
            AssistantObject.SetName(NewName)
        elif Parameter=='пол':
            AssistantObject.Say('Готов сменить голос')
            NewGender=SRM.OfflineRecognition(AssistantObject, LocalModelConnection)
            if NewGender=='женский':
                NewGender='female'
            else:
                NewGender='male'
            AssistantObject.SetGender(NewGender)
        else:
            AssistantObject.Say('Какой язык вы хотите использовать? Русский или Английский?')
            NewLang=SRM.OfflineRecognition(AssistantObject, LocalModelConnection)
            if NewLang=='русский':
                NewLang='ru'
            else:
                NewLang='en'
            AssistantObject.SetLanguage(NewLang)

    AssistantObject.ConfigureAssistant()
    print(AssistantObject.GetName())

def SayName(AssistantObject, *args: tuple):
    AssistantObject.Say('Меня зовут ' + AssistantObject.GetName())