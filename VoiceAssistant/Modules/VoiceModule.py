import random as rnd
def SayHelloToUser(AssistantObject):
    AssistantObject.Say('Приветствую вас, пользователь')


def MakeUserHappy(AssistantObject):
    ListOfMotivators=list(['У вас все получится!', 
                          'Вы лучший!', 'Лучше, чем вы не бывает людей',
                         'Что бы вы не делали, помните, что ваш ассистент всегда с вами',
                         'Только скажите как я могу вам помочь, и я это сделаю',
                         'Если вам кажется, что ничего не получается, помните, что есть люди, которые готовы вам помочь'])

    NumberOfMotivationalSpeech=rnd.randrange(0, len(ListOfMotivators))
    AssistantObject.Say(ListOfMotivators[NumberOfMotivationalSpeech])
