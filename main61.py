import requests
import json


def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("SAPI.spVoice")
    speak.speak(str)
if __name__=='__main__':
    url = requests.get("https://newsapi.org/v2/top-headlines?sources=mtv-news&apiKey=568419024cc44cbe81444234fbff3d1a")
    response=url
    text=response.text
    my=json.loads(text)
    for i in range(0,4):
     speak(my['articles'][i]['title'])