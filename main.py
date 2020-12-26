import speech_recognition as sr
import pyttsx3
import pywhatkit

listener=sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[64].id)
engine.setProperty('rate', 160)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    with sr.Microphone() as source:
        listener.adjust_for_ambient_noise(source,duration=1)
        print("say anything : ")
        audio = listener.listen(source)
        try:
            command = listener.recognize_google(audio, language="vi-VN")
            command = command.lower()
            print('raw : '+command)
            if 'sunday' in command:
                command = command.replace('sunday','')
        except:
            print("sorry, could not recognise")
            talk("sorry, could not recognise")
        
        if(command != None):
            return command
        else:
            return 

def run_sunday():
    
    command = take_command()
    print(command)
    if 'youtube' in command:
        command = command.replace('youtube','')
        talk("Playing " + command)
        print("final : "+command)
        pywhatkit.playonyt(command)
    if 'google' in command:
        command = command.replace('google','')
        talk('searching '+command)
        pywhatkit.search(command)

if __name__ == "__main__":
    run_sunday()
    # talk("thằng hưng ăn cứt đi em")
    # voices = engine.getProperty('voices')
    # count = 0
    # for voice in voices:
    #     print(count)
    #     print("Voice:")
    #     print(" - ID: %s" % voice.id)
    #     print(" - Name: %s" % voice.name)
    #     print(" - Languages: %s" % voice.languages)
    #     print(" - Gender: %s" % voice.gender)
    #     print(" - Age: %s" % voice.age)
    #     count += 1
   