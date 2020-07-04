
# coding: utf-8

# In[1]:

import speech_recognition as spec
import win32com.client as wincl
import wikipedia
from tkinter import *
master=Tk()
speak = wincl.Dispatch("SAPI.SpVoice")
def bot():
    x=spec.Recognizer() 
    with spec.Microphone() as source:
        audio=x.listen(source)
    y=x.recognize_google(audio)
    y=y.encode("ascii")
    return y


# In[2]:

def calculate():
    speak.Speak("Tell me the expression. Please use numbers and symbols only. to add, use plus. to subtract, use minus. to multiply use astereik. to divide, use slash")
    y=bot()
    try:
        sol=eval(y)
    except:
        speak.Speak("I can't understand, Sorry, Tell it again")
        calculate(y)
    else:
        speak.Speak("the answer is")
        text.insert(0,str(y)+"="+str(sol))
        speak.Speak(sol)


# In[3]:

def start():
    elements=["Getting Started","Hey Dood! I am your matkibot","I can calculate mathematical expressions and I can also search something in wikipedia","That's y mask named me Matkibot","now,ask me"]
    for i in elements:
        speak.Speak(i)


# In[4]:

def search():
    speak.Speak("Tell me something which you want to search! Note:The thing alone!")
    y=bot()
    z=wikipedia.summary((y),sentences=3)
    text.insert(0,z)
    speak.Speak(z)


# In[5]:

def clear():
    text.delete(0,END)


# In[ ]:




# In[ ]:




# In[6]:

b1=Button(master,text="Start!",command=start,padx=30,pady=20,font=15)
b2=Button(master,text="Calculate",command=calculate,padx=30,pady=20,font=15)
b3=Button(master,text="Search in Wikipedia",command=search,padx=30,pady=20,font=15)
b4=Button(master,text="Exit",command=master.quit,padx=30,pady=20,font=15)
b5=Button(master,text="Clear",command=clear,padx=30,pady=20,font=15)
text=Entry(master,width=35,font=13,borderwidth=5)


# In[7]:

master.title("Matkibot")


# In[8]:

text.grid(row=0,column=0,ipadx=40,ipady=60)
b1.grid(row=1)
b2.grid(row=2)
b3.grid(row=3)
b4.grid(row=4)
b5.grid(row=5)


# In[9]:

master.mainloop()


# In[ ]:



