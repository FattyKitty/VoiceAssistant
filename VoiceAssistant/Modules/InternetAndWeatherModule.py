from pyowm import OWM
import os
import webbrowser
import time


def SearchGoogle(AssistantObject, SearchArgs):

    URL='https://google.com/search?q='

    SearchingThings=' '.join(SearchArgs)
    URL=URL+SearchingThings

    AssistantObject.Say('Вот что удалось найти по вашему запросу')
    time.sleep(500)

    webbrowser.get().open(URL)

def SearchOnYouTube(AssistantObject, SearchArgs):

    URL='https://www.youtube.com/results?search_query='
    SearchingThings=' '.join(SearchArgs)
    URL=URL+SearchingThings

    webbrowser.get().open(URL)