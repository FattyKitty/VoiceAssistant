import Modules.VoiceModule as VoiceM

Commands ={
    ('привет', 'здравствуй'): VoiceM.SayHelloToUser,
    ('подбодрить','ободри', 'ободрить', 'поддержи', 'подбодри'): VoiceM.MakeUserHappy
    }


def CommandClassificator(InputCommand, AssistantObject):
    StringByArgumentsSplit=list(InputCommand.split(' '))

    if StringByArgumentsSplit[0]==AssistantObject.GetName():
        #AssistantObject.Say('Это команда')

        for KeyPhrase in Commands.keys():
            if StringByArgumentsSplit[1] in KeyPhrase:
                Commands[KeyPhrase](AssistantObject)
        
