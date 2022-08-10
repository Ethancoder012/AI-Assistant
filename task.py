import datetime
from speaker import Say
import pywhatkit
import webbrowser
import os



def Time():
    time=datetime.datetime.now().strftime("%H:%M")
    Say(time)
def Date():
    date=datetime.date.today()
    Say(date)

def Day():
    day=datetime.datetime.now().strftime("%A")
    Say(day)

def NonInputExecution(query):

    query=str(query)
    if "time" in query:
        Time()
    elif "date" in query:
        Date()
    elif "day" in query:
        Day()
dictapp={"command prompt":"cmd","word":"winword","excel":"excel","chrome":"chrome","vs code":"code","powerpoint":"powerpnt","firefox":"firefox","notepad":"notepad"}
def nputxecution(tag,query):

    


    if "google" in tag:
        query=str(query).replace("google","").replace("search","").replace("who is","").replace("what is","")
        query=query.replace("search","")
        from flask import Flask
        import wikipedia as wk
        Say("This is what I found on google")

        try:
            pywhatkit.search(query)
            result=wk.summary(query,1)
            Say(result)

        except:
            Say("no speakable output available")


    elif "youtube" in tag:
        query=str(query).replace("open youtube and play"," ").replace("from youtube play","").replace("let's watch a","")
        web="https://www.youtube.com/results?search_query=?" + query
        webbrowser.open(web)
        pywhatkit.playonyt(query)
        Say("Done sir")

    elif "wikipedia" in tag:
        name=str(query).replace("tell me about "," ").replace("information "," ").replace("about"," ").replace("information about "," ")
        import wikipedia as w
        result=w.summary(w.page(name,auto_suggest=False),sentences=2)
        Say(result)

    elif "open" in tag:
        Say("Accessing your request sir")
        if ".com" in query or ".co.in" in query or ".org" in query:
            chrome_path='C:\Program Files\Google\Chrome\Application\chrome.exe'
            res=str(query).replace("Jarvis open","").replace("open","").replace("launch","").replace("please open","").replace("please launch","")
            webbrowser.register('chrome', None,webbrowser.BackgroundBrowser(chrome_path))
            webbrowser.get('chrome').open_new_tab(res)
            

        else:
            keys=list(dictapp.keys())
            res=str(query).replace("Jarvis open","").replace("open","").replace("launch","").replace("please open","").replace("please launch","")
            Say("opening"+res)
            for app in keys:
                if app in res:
                    os.system(f"start {dictapp[app]}")


    
