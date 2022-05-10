from pyowm import OWM
import os
import webbrowser
import time
import wikipediaapi


def SearchGoogle(AssistantObject, *args: tuple):

    URL='https://google.com/search?q='

    SearchingThings=' '.join(args[0])
    URL=URL+SearchingThings

    AssistantObject.Say('Вот что удалось найти по вашему запросу в интернете')

    webbrowser.get().open(URL)

def SearchOnYouTube(AssistantObject, *args: tuple):

    URL='https://www.youtube.com/results?search_query='
    SearchingThings=' '.join(args[0])
    URL=URL+SearchingThings

    webbrowser.get().open(URL)


def SearchWiki(AssistantObject, *args: tuple):

    SearchingObject=' '.join(args[0])

    Wiki=wikipediaapi.Wikipedia(AssistantObject.GetLanguage())

    WikiPage=Wiki.page(SearchingObject)

    try:
        if WikiPage.exists():
            AssistantObject.Say('Вот, что я нашел по вашему запросу на википедии')
            webbrowser.get().open(WikiPage.fullurl)
        else:
            AssistantObject.Say('По вашему запросу в Википедии ничего не найдено, но: ')
            SearchGoogle(AssistantObject, SearchingObject)
    except:
        AssistantObject.Say('Ничего не могу найти по вашему запросу')

