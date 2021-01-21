import speech_recognition as sr
import pyttsx3
import pywhatkit

listener=sr.Recognizer() # tao ra de lang nghe am thanh tu nguoi dung
engine = pyttsx3.init() # khoi tao giong noi
voices = engine.getProperty('voices') # lay thong tin cac giong noi 
engine.setProperty('voice',voices[64].id) 
engine.setProperty('rate', 160)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# de noi
def talk(text):
    engine.say(text)
    engine.runAndWait()

# lay lenh tu cau noi
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
        talk("Open " + command)
        print("final : "+command)
        pywhatkit.playonyt(command)
    if 'google' in command:
        command = command.replace('google','')
        talk('searching '+command)
        pywhatkit.search(command)

if __name__ == "__main__":
    run_sunday()
    # engine.say("xin chào huy con cho")
    # engine.runAndWait()
    
    
   