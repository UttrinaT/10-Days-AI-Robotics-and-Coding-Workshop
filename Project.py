import tkinter as tki
import pyttsx3 as ptt
import datetime as dt
from tkinter import StringVar,END
import webbrowser
import wikipedia
import os
import speech_recognition as sr 

eng = ptt.init()
voice = eng.getProperty('voices')
eng.setProperty('voices',voice[0].id)

def speak(text_a):
    eng.say(text_a)
    eng.runAndWait()

def wish_me():
    try:
        cu_hour = dt.datetime.now().hour
        if 0 <=cu_hour < 12:
            speak("Good Morning!")
        elif 12 <= cu_hour < 18:
            speak("Good Afternoon!")
        else:
            speak("Good Evening!")
        
        speak("I am JARVIS , Just A Rather Very Intelligent Robot. Please Tell me how  can I assist you today!")
        output_var.set("I am JARVIS , Just A Rather Very Intelligent Robot. Please Tell me how i can assist you today?")
    except Exception as e:
        print(f"Error in wishing: {e}")

def run_command():
    input_command = input_var.get().lower()
    if input_command == "":
        speak("No command Given.Give another Command.")
        output_var.set("Error: No command given.")
    else:
        if "open youtube" in input_command:
            webbrowser.open("https://www.youtube.com/")
            output_var.set("Opening Youtube")
        elif "open google" in input_command:
            webbrowser.open("https://www.google.com/")
            output_var.set("Opening Google")
        elif "open instagram" in input_command:
            webbrowser.open("https://www.instagram.com/")
            output_var.set("Opening Instagram")
        elif "open vs code" in input_command:
            vscode_path = r"C:\Users\Uttrina\AppData\Local\Programs\Microsoft VS Code\Code.exe"
            os.startfile(vscode_path)
            output_var.set("Opening VS Code")
        elif "open tlauncher" in input_command:
            tlauncher_path = r"C:\Users\Uttrina\AppData\Roaming\.minecraft\TLauncher.exe"
            os.startfile(tlauncher_path)
            output_var.set("Opening TLauncher")
        elif "current time" in input_command:
            time_str = dt.datetime.now().strftime("%H:%M:%S")
            speak(f"Current time is {time_str}")
        elif "open brave" in input_command:
            brave_path = r"C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe" 
            os.startfile(brave_path) 
            output_var.set("Opening Brave Browser")
        elif "open settings" in input_command:
            settings_path = r"C:\Windows\System32\control.exe"
            os.startfile(settings_path)
            output_var.set("Opening Settings")
        elif "wikipedia" in input_command:
            input_command = input_command.replace( "wikipedia", "")
            try:
                wiki_result = wikipedia.summary(input_command,sentences = 4)
                speak(f"According to wikipedia:\n {wiki_result}")
                output_var.set (f"According To wikipedia:\n {wiki_result}")
            except wikipedia.DisambiguationError:
                speak("Too vague input; please try again!")
        else:
            speak("Sorry!Input Command not Recognized.Please try Again.")

def voice_command():
    rec = sr.Recognizer()
    with sr.Microphone() as source:
        rec.adjust_for_ambient_noise(source)
        audio = rec.listen(source)
        try:
            text_audio = rec.recognize_google(audio, language='en-in')
            return text_audio.lower()
        except sr.UnknownValueError:
            return ""
        
def listen_voice():
    given_command = voice_command()
    input_var.set(given_command)
    run_command()

    
wind = tki.Tk()
wind.title("J.A.R.V.I.S")
wind.geometry("650x500")
wind.configure(bg="#04b3f8")

input_var = StringVar()
output_var = StringVar()

l1=tki.Label(wind,text ="J.A.R.V.I.S: The One who helped Tony Stark",bg = "#04b3f8",font=("dominance regular",20,"bold"))
l1.place(x=30,y=0)

l2 = tki.Label(wind,text="What would you like for me to do, Sir?",bg = "#04b3f8",font=("dominance regular",10,"bold","italic"))
l2.place(x=60,y=75)

ent = tki.Entry(wind,textvariable = input_var,width = 60,font=("bold"))
ent.place(x=50,y=100)

bu1 = tki.Button(wind,text="逃げる",command = run_command,bg = "#FDFDFD",font=("dominance regular",20,"bold","italic"))
bu1.place(x=250,y=150)

bu2 = tki.Button(wind,text="コマンドを話す",command = listen_voice, bg = "#FDFDFD",font=("dominance regular",20,"bold","italic"))
bu2.place(x=190,y=210)

out_lb = tki.Label(wind,text="OUTPUT",bg =
 "#04b3f8",font=("dominance regular",20,"bold"))
out_lb.place(x=30,y=270)

out_tex = tki.Text(wind,font=("dominance regular",10,"bold","italic"),bg = "#ffffff",width = 86,height = 11,wrap = "word",state  = tki.DISABLED)
out_tex.place(x=25, y = 310)

def update_output(*args):
    out_tex.config(state=tki.NORMAL)
    out_tex.delete(1.0, END)
    out_tex.insert(END, output_var.get())
    out_tex.config(state=tki.DISABLED )

output_var.trace_add("write", update_output)


wish_me()


wind.mainloop()