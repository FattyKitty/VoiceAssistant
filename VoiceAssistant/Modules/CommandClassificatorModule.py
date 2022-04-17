import Modules.VoiceModule as VoiceM
import Modules.InternetAndWeatherModule as IOT

Commands ={
    ('привет', 'здравствуй'): VoiceM.SayHelloToUser,
    ('поддержи','ободри', 'ободрить', 'поддержи', 'подбодри'): VoiceM.MakeUserHappy,
    #('погода', 'прогноз', 'температура'): IOT.WeatherForecast,
    ('загугли', 'найди', 'поищи', 'поиск', 'гугл', 'google'): IOT.SearchGoogle,
    ('видео', 'youtube'): IOT.SearchOnYouTube
    ('пока', 'увидимся', 'прощай' VoiceM.SayGoodbyeToUser)
    }


def CommandClassificator(InputCommand, AssistantObject):
    StringByArgumentsSplit=list(InputCommand.split(' '))

    if StringByArgumentsSplit[0]==AssistantObject.GetName():
        for KeyPhrase in Commands.keys():
            if StringByArgumentsSplit[1] in KeyPhrase:
                Commands[KeyPhrase](AssistantObject, StringByArgumentsSplit[2::])
        
