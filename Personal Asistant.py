import wikipedia
import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import os
import random

engine=pyttsx3.init('sapi5')
nr=135
engine.setProperty('rate',nr)

def speak(stri):
    '''
    This function will take a string as a input and speak with the default voice of your computer system
    '''
    engine.say(stri)
    engine.runAndWait()

def open_si(site):
    
    webbrowser.open(f'https://www.{site}.com')    
def wish():
    time=int(datetime.datetime.now().hour)
    if time>0 and time<12:
        speak('Good Morning, Arjun Sir! I am your personal assistant khushi.')
    elif time>12 and time<4:
        speak('Good Afternoon, Arjun Sir! I am your personal assistant khushi.')
    else:
        speak('Good Evening, Arjun Sir! I am your personal assistant khushi.')
    speak('How may I help you sir?')    
def listen():
    '''
    This function will take the command from the assistant
    '''         
    r=sr.Recognizer()
    with sr.Microphone()as source:
        print('Listning...')
        r.energy_threshold=300
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print('Recognizing...')
        ques=r.recognize_google(audio, language='en-in')
        print(f'You said: {ques}\n')
    except :
        
        print('Sorry sir, my wrong, I am not able to recognize what you said.')
        
        return 'N'
    return ques    

if __name__ == "__main__":
    wish()  
    while True:    
        
        ques=listen().lower()
        
        if 'open'in ques:
            si_name=ques.replace('open','')
            print(si_name)
            open_si(si_name)
        elif 'wikipedia'in ques:
            ques=ques.replace('wikipedia', '')
            data=wikipedia.summary(ques, sentences=3)   
            speak('According to wikipedia.')
            print(data)
            speak(data)  
        elif 'play music' in ques:
            music_dir='D:\\punjabi songs'
            songs=os.listdir(music_dir)
            lis=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
            os.startfile(os.path.join(music_dir,songs[random.choice(lis)]))
        elif 'who are you' in ques:
            speak('I am your personal assistant, Khushi. ')    
        elif 'the time' in ques:
            strtime=datetime.datetime.now().strftime('%H:%M:%S') 
            print(strtime)
            speak(f'Sir, the time is {strtime}')   
        else:
            print(wikipedia.summary(ques, sentences=3))
            speak(wikipedia.summary(ques, sentences=3))    
