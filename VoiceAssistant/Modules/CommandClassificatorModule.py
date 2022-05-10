import Modules.VoiceModule as VoiceM
import Modules.InternetAndWeatherModule as IOT

Commands ={
    ('привет', 'здравствуй'): VoiceM.SayHelloToUser,
    ('поддержи','ободри', 'ободрить', 'поддержи', 'подбодри'): VoiceM.MakeUserHappy,
    ('загугли', 'найди', 'поищи', 'поиск', 'гугл', 'google'): IOT.SearchGoogle,
    ('видео', 'youtube'): IOT.SearchOnYouTube,
    ('пока', 'увидимся', 'прощай'): VoiceM.SayGoodbyeToUser,
    ('конфигурация'): VoiceM.SetNewProfile

    }


def CommandClassificator(InputCommand, AssistantObject):
    StringByArgumentsSplit=list(InputCommand.split(' '))

    if StringByArgumentsSplit[0]==AssistantObject.GetName():
        for KeyPhrase in Commands.keys():
            if StringByArgumentsSplit[1] in KeyPhrase:
                Arguments=list(StringByArgumentsSplit[2::])
                Commands[KeyPhrase](AssistantObject, Arguments)
        
