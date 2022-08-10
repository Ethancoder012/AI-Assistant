import speech_recognition as sr
import pyaudio

def Listen():
    r=sr.Recognizer()

    with sr.Microphone() as source:
        print("")
        print("Listening... ")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing..")
        query=r.recognize_google(audio,language="en-in")
        print(f"You Said:{query}")

    except Exception as e:
        print("Say that again")
        return ""
    query=str(query)
    return query.lower()
