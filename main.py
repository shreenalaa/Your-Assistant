import os
import winsound
import pyttsx3
from tkinter import *
import speech_recognition as sr
from tkinter import messagebox
import speech_recognition as sr


def initTTS():
    tts = pyttsx3.init()
    voices = tts.getProperty('voices')
    tts.setProperty('voice',  voices[0])
    return tts
def openGoogle():
    os.system('cmd /k "start chrome www.google.com')
def openFacebook():
    os.system('cmd /k "start chrome www.facebook.com')
def speak (audio):
    global tts
    tts.say(audio)
    tts.runAndWait()
def action(command):
    command = command.lower()
    if "google" in command:
        s = "openning google. write now..."
        import winsound
        winsound.PlaySound('OPen-Google.wav', winsound.SND_FILENAME)

        speak(s)
        output_text.set(s)
        openGoogle()
    elif "facebook" in command:
        s = "openning facebook. write now..."
        speak(s)
        output_text.set(s)
        openFacebook()
    else:
        if "welcome" in command:
            s = "welcome sir. how are you today"
            import winsound
            winsound.PlaySound('Welcome.wav', winsound.SND_FILENAME)

            
        elif "morning" in command:
            s = "good morning sir."
            import winsound
            winsound.PlaySound('Good-Morning.wav', winsound.SND_FILENAME)

            
        elif "evening" in command:
            s = "good evining sir."
            import winsound
            winsound.PlaySound('Good-Evening.wav', winsound.SND_FILENAME)
            
        elif "help" in command:
            s = "How can i help you,sir ?"
            import winsound
            winsound.PlaySound('Help.wav', winsound.SND_FILENAME)
        else : 
            s = "I can not understand. Can you repeat"
        speak(s)
        output_text.set(s)
def takeCommands():
    command = sr.Recognizer()
    with sr.Microphone() as mic:
        command.adjust_for_ambient_noise(mic, duration=2)
        command.phrase_threshold = 0.1
        audio = command.listen(mic)
        try :
            query = command.recognize_google(audio)
            return query.lower()   
        except Exception as Error :
            return "Try again "
def micClick () :
    command =  takeCommands()
    input_text.set(command)
    action(command);
    
tts = initTTS()

root = Tk()
root.title("assistant")
root.geometry('350x150+500+100')
root.resizable(False,False)

input_text = StringVar()
label = Label(root,width = 30, font = ('Times New Roman' , 14 ),textvariable = input_text)
label.place(x = 20 , y=50)

output_text = StringVar()
label = Label(root,width = 30, font = ('Times New Roman' , 14 ),textvariable = output_text)
label.place(x = 20 , y=100)


btn = Button(root, text= '🎤',bg = 'black', fg = 'white' , font = ('Times New Roman' ,9),command = micClick)    
btn.place(x= 300 , y = 50) 
    
root.mainloop()



exe.
C:\Users\SkyTop\python\dist