import pyttsx3


def Say(Text):
    engine=pyttsx3.init()
    voices=engine.getProperty('voices')
    engine.setProperty('voices',voices[0].id)
    engine.setProperty('rate',130)
    print("   ")
    print(f"A.I: {Text}")
    engine.say(text=Text)
    engine.runAndWait()
    print("  ")


