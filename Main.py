import random
import tkinter as tk
from tkinter import *
from tkinter import messagebox, Label, Entry
import win32com.client as bot
import os
import datetime
from tkinter.messagebox import *
from random import  randint

speak = bot.Dispatch("Sapi.SpVoice")
window = tk.Tk
root = Tk()
root.title("Lazy Bot")
frame = LabelFrame(root, padx=35, pady=35)
frame.grid(row=0,column=2,padx=35, pady=35)
frame2 = LabelFrame(root, padx=35, pady=35)
frame2.grid(row=0,column=2,padx=35, pady=35)
frame4 = LabelFrame(root, text="Commands To Ask", padx=35, pady=35)
frame4.grid(row=0,column=2,padx=35, pady=35)
frame5 = LabelFrame(root, padx=35, pady=35)
frame5.grid(row=0,column=2,padx=35, pady=35)
frame6 = LabelFrame(root, padx=35, pady=35)
frame6.grid(row=1,column=2,padx=35, pady=35)
frame3 = LabelFrame(root, padx=35, pady=35)
frame3.grid(row=0,column=2,padx=35, pady=35)
frame7 = LabelFrame(root, padx=35, pady=35)
frame7.grid(row=1,column=2,padx=35, pady=35)
frame8 = LabelFrame(root, padx=35, pady=35)
frame8.grid(row=0,column=2,padx=35, pady=35)
frame9 = LabelFrame(root, padx=35, pady=35)
frame9.grid(row=0,column=2,padx=35, pady=35)
frame0 = LabelFrame(root, padx=35, pady=35)
frame0.grid(row=1,column=2,padx=35, pady=35)
frame11=LabelFrame(root,padx=35,pady=35)
frame11.grid(row=1,column=2,padx=35,pady=35)
frame12=LabelFrame(root,padx=35,pady=35)
frame12.grid(row=0,column=2,padx=35,pady=35)
frame13=LabelFrame(root,padx=35,pady=35)
frame13.grid(row=0,column=2,padx=35,pady=35)
frame14=LabelFrame(root,padx=35,pady=35)
frame14.grid(row=0,column=2,padx=35,pady=35)
frame15=LabelFrame(root,padx=35,pady=35)
frame15.grid(row=1,column=2,padx=35,pady=35)
af=["DAD: I was just listening to the radio on my way in to town, apparently an actress just killed herself.\n"
    "MOM: Oh my! Who!?\n"
    "DAD: Uh, I can't remember... I think her name was Reese something?\n"
    "MOM: WITHERSPOON!!!!!???????\n"
    "DAD: No, it was with a knife...\n",
    "Today, my son asked 'Can I have a book mark?' and I burst into tears. 11 years old and he still doesn't know my name is Brian.","How do you make holy water? You boil the hell out of it.","Did you know the first French fries weren't actually cooked in France? They were cooked in Greece.","The secret service isn't allowed to yell 'Get down!' anymore when the president is about to be attacked. Now they have to yell 'Donald, duck!'","I'm reading a book about anti-gravity. It's impossible to put down!","What do you call someone with no body and no nose? Nobody knows.","When a dad drives past a graveyard: Did you know that's a popular cemetery? Yep, people are just dying to get in there!","MOM: 'How do I look?' DAD: 'With your eyes.'","If you see a robbery at an Apple Store does that make you an iWitness?","How do lawyers say goodbye? We'll be suing ya!"
,"Don't trust atoms. They make up everything!","When does a joke become a dad joke? When it becomes apparent."
,"What do you call a fake noodle? An impasta."
,"Can February March? No, but April May!","How many tickles does it take to make an octopus laugh? Ten tickles."
]
def AAAA():
    speak.Speak("Please Enter Username")


def hl():
    frame11.grid_remove()
    frame5.grid_remove()
    frame.grid()
    frame9.grid_remove()
    global a
    global boh
    a = Entry(frame, width=35, borderwidth=5)
    a.grid(row=1, column=2)
    label = Label(frame, text="Username:")
    label.grid(row=0, column=1)
    button = Button(frame, text="Submit", command=h)
    button.grid(row=4, column=2)
    bhaa = Button(frame, text="Back", command=lambda: [frame.grid_remove(), frame5.grid()])
    bhaa.grid(row=6, column=2)
    button1111 = Button(frame, text="🔊", command=AAAA)
    button1111.grid(row=0, column=0, padx=10, pady=10)


def h():

    with open("Usernames.txt")as p:

        if a.get() in p.read():
            global laee
            messagebox.showinfo("Check", "Checking Username...\n Please Press Ok")
            global label2
            global button2
            global button5
            label2 = Label(frame, text="Welcome Back " + a.get() + "")
            label2.grid(row=5, column=2)
            button2 = Button(frame, text="Start", command=my)
            button2.grid(row=6, column=2)
            button5 = Button(frame, text="Help", command=kkk)
            button5.grid(row=7, column=2)

            laee.grid_remove()
        else:



            laee = Label(frame, text="There Is No such A Username")
            laee.grid(row=5, column=2)


def hj():
    frame8.grid()
    with open("Usernames.txt")as p:
        if g.get() not in p.read():
            f = open("Usernames.txt", "a+")
            f.write(g.get() + "\n")
            f.close()
            global label4
            messagebox.showinfo("Check", "Checking Username...\n Please Press Ok")
            label4 = Label(frame8, text="Sign Up Completed\nPlease Press Back And Then Login")
            label4.grid(row=4, column=2)

        else:

            global LASS
            LASS = Label(frame8, text="Username is Used")
            LASS.grid(row=4, column=2)


def zz():
    with open("The Path.txt"):
        e = open("The Path.txt", "w+")
        e.write(o.get() + "")
        e.close()


def asd():
    global L
    global g
    frame8.grid()
    frame5.grid_remove()
    g = Entry(frame8, width=35, borderwidth=5)
    g.grid(row=0, column=2)
    label123456 = Label(frame8, text="Please Write Your App Or Song Path\nFor Further Use.")
    label123456.grid(row=2, column=2)
    b55 = Button(frame8, text="submit", command=hj)
    b55.grid(row=1, column=2)
    b56 = Button(frame8, text="Change Path", command=zz)
    b56.grid(row=5, column=2)
    b44 = Button(frame8, text="back", command=lambda: [frame8.grid_remove(), frame5.grid()])
    b44.grid(row=6, column=2)
    global o
    o = Entry(frame8, width=35, borderwidth=5)
    o.grid(row=3, column=2)
def art():
    USER_SCORE = 0
    COMP_SCORE = 0
    USER_CHOICE = ""
    COMP_CHOICE = ""

    def choice_to_number(choice):
        rps = {'rock': 0 , 'paper': 1 , 'scissor': 2}
        return rps[choice]

    def number_to_choice(number):
        rps = {0: 'rock' , 1: 'paper' , 2: 'scissor'}
        return rps[number]

    def random_computer_choice():
        return random.choice(['rock' , 'paper' , 'scissor'])

    def result(human_choice , comp_choice):
        global USER_SCORE
        global COMP_SCORE
        user = choice_to_number(human_choice)
        comp = choice_to_number(comp_choice)
        if (user == comp):
            lj3 = tk.Label(master=window , text="Tie")
            lj3.grid(row=5 , column=0)
        elif ((user - comp) % 3 == 1):
            lj2 = tk.Label(master=window , text="You win")
            lj2.grid(row=5 , column=0)
            USER_SCORE += 1
        else:
            lj = tk.Label(master=window , text="Comp wins")
            lj.grid(row=5 , column=0)
            COMP_SCORE += 1
        text_area = tk.Text(master=window , height=12 , width=30 , bg="#FFFF99")
        text_area.grid(column=0 , row=4)
        answer = "Your Choice: {uc} \nComputer's Choice : {cc} \n Your Score : {u} \n Computer Score : {c} ".format(
            uc=USER_CHOICE , cc=COMP_CHOICE , u=USER_SCORE , c=COMP_SCORE)
        text_area.insert(tk.END , answer)

    def rock():
        global USER_CHOICE
        global COMP_CHOICE
        USER_CHOICE = 'rock'
        COMP_CHOICE = random_computer_choice()
        result(USER_CHOICE , COMP_CHOICE)

    def paper():
        global USER_CHOICE
        global COMP_CHOICE
        USER_CHOICE = 'paper'
        COMP_CHOICE = random_computer_choice()
        result(USER_CHOICE , COMP_CHOICE)

    def scissor():
        global USER_CHOICE
        global COMP_CHOICE
        USER_CHOICE = 'scissor'
        COMP_CHOICE = random_computer_choice()
        result(USER_CHOICE , COMP_CHOICE)

    button1 = tk.Button(text="       Rock       " , bg="skyblue" , command=rock)
    button1.grid(column=0 , row=1)
    button2 = tk.Button(text="       Paper      " , bg="pink" , command=paper)
    button2.grid(column=0 , row=2)
    button3 = tk.Button(text="      Scissor     " , bg="lightgreen" , command=scissor)
    button3.grid(column=0 , row=3)
def art2():
 os.startfile("Tic.exe")
def art1():
 os.startfile("Mind.exe")
def ll():
    speak.Speak(e55.get())


def myu():

    if LastEntry.get()=="Play"or LastEntry.get()=="play":
        frame2.grid_remove()
        BTN4=Button(frame13,text="Rock,Paper,Scissors",command=art)
        BTN4.grid(row=1,column=1)
        BTN5=Button(frame13,text="Tic Tac Toe",command=art2)
        BTN5.grid(row=2,column=1)
        BTN6=Button(frame13,text="Mind Reading",command=art1)
        BTN6.grid(row=3,column=1)
        BTN7=Button(frame13,text="Back",command=lambda :[frame13.grid_remove(),frame2.grid()])
        BTN7.grid(row=4,column=1)

    elif LastEntry.get() == "Speak"or LastEntry.get()=="speak":
        frame11.grid_remove()
        frame2.grid_remove()
        frame2.grid()
        global e55
        e55=Entry(frame12,width=35)
        e55.grid(row=1,column=1)
        BP=Button(frame12,text="Speak",command=ll)
        BP.grid(row=2,column=1)
        BTN7=Button(frame13,text="Back",command=lambda :[frame12.grid_remove(),frame2.grid()])
        BTN7.grid(row=4,column=1)
    elif LastEntry.get() == "Who Are You?" or LastEntry.get()=="who are you?":
        frame6.grid()
        frame0.grid_remove()
        frame7.grid_remove()
        label7 = Label(frame6, text="My Name Is BOT My Programmer Zh32 Programmed Me To Assist You.")
        label7.grid(row=13, column=2)
        speak.Speak("My Name Is BOT  And  My  Programmer Zh32 Programmed Me To Assist You.")
    elif LastEntry.get() == "Who Am I?"or LastEntry.get()=="who am i?":
        frame0.grid()
        frame9.grid_remove()
        LASD3 = Label(frame0, text="You Are " + a.get() + " And You Are My Master")
        LASD3.grid(row=4, column=2)
        button1111 = Button(frame0, text="🔊", command=AH)
        button1111.grid(row=0, column=0, padx=10, pady=10)
    elif LastEntry.get()=="Tell Me A Joke"or LastEntry.get()=="tell me a joke":
        def ddsa():
            l9909.grid_remove()
        frame9.grid_remove()
        frame11.grid()
        x=(af[randint(0, len(af)-1)])
        l9909=Label(frame11,text=x)
        l9909.grid(row=7,column=2)
        b7272=Button(frame11,text="Clear",command=ddsa)
        b7272.grid(row=8,column=2)
    elif LastEntry.get() == "Hi"or LastEntry.get()=="hi":
        frame0.grid_remove()
        frame7.grid()
        frame6.grid_remove()
        frame15.grid_remove()
        l = Label(frame7, text="hi " + a.get() + "")
        speak.Speak("hi " + a.get() + "")
        l.grid(row=13, column=2)
    elif LastEntry.get() == "Open"or LastEntry.get()=="open":
        frame2.grid_remove()
        frame7.grid_remove()
        frame.grid_remove()
        frame6.grid_remove()
        frame3.grid()
        frame0.grid_remove()
        frame11.grid_remove()
        frame15.grid_remove()
        global entry6
        entry6 = Entry(frame3, width=35, borderwidth=10)
        entry6.grid(row=12, column=2)
        entry6.insert(1, "Type The Name Of The App")
        global exe
        exe = Entry(frame3, width=35, borderwidth=5)
        exe.grid(row=13, column=2)
        exe.insert(1, "The Type Of The File")
        button8 = Button(frame3, text="Open", command=asr)
        button8.grid(row=14, column=2)
        b98 = Button(frame3, text="Back", command=lambda: [frame3.grid_remove(), frame2.grid()])
        b98.grid(row=15, column=2)
    elif LastEntry.get() == "Set Alarm"or LastEntry.get()=="set alarm":
        frame2.grid_remove()
        frame7.grid_remove()
        frame3.grid_remove()
        frame6.grid_remove()
        frame9.grid()
        frame0.grid_remove()
        frame11.grid_remove()
        frame15.grid_remove()
def alarm():
    frame2.grid_remove()
    frame6.grid_remove()
    x=int(e1.get())
    y=int(e2.get())
    z=str(c1.get())
    showinfo("Notification","Alaram Has Been Set")
    if z =="pm":
        x=x+12
    while True:
        if x==datetime.datetime.now().hour and y==datetime.datetime.now().minute:
            for i in range(0,int(e5.get())):
                speak.Speak(e4.get())
            break

l1=Label(frame9,text="Hours:")
l1.grid(row=0,column=0)
l2=Label(frame9,text="Minutes:")
l2.grid(row=1,column=0)
l3=Label(frame9,text="pm or am:")
l3.grid(row=4,column=0)
e1=Entry(frame9,width=35)
e1.grid(row=0,column=1)
e2=Entry(frame9,width=35)
e2.grid(row=1,column=1)
e4=Entry(frame9,width=35)
e4.grid(row=3,column=1)
c1=Entry(frame9,width=35)
l4=Label(frame9,text="The Alarm Text:")
l4.grid(row=3,column=0)
c1.grid(row=4,column=1)
b1=Button(frame9,text="Set Alarm",command=alarm)
b1.grid(row=6,column=1)
e5=Entry(frame9,width=35)
e5.grid(row=5,column=1)
b708=Button(frame9,text="Back",command=lambda :[frame9.grid_remove(),frame2.grid()])
b708.grid(row=7,column=1)
l5=Label(frame9,text="How Many Seconds Do You Want The Alarm To Go Off:")
l5.grid(row=5,column=0)
def my(self=frame):
    frame2.grid()
    frame.grid_remove()

    global LastEntry
    LastEntry = Entry(frame2, width=35, borderwidth=5)
    LastEntry.insert(0, "Enter the Command")
    LastEntry.grid(row=10, column=2)
    global button7
    button7 = Button(frame2, text="Enter", command=myu)
    button7.grid(row=11, column=2)
    B123 = Button(frame2, text="Back",
                  command=lambda: [self.grid(), frame2.grid_remove(), label2.grid_remove(), button2.grid_remove(),
                                   button5.grid_remove(), frame6.grid_remove(), frame7.grid_remove(),
                                   frame0.grid_remove(),frame11.grid_remove()])
    B123.grid(row=12, column=2)


def asr():
    with open("The Path.txt")as ds:
        A = ds.read()
        os.startfile(A + entry6.get() + exe.get())


def AAA():
    speak.Speak("Commands To Ask. 1)hi. 2)who are you? 3)Open.4) And Also If You Want To Hear The Text Please Press This Button. 5)Who Am I. 6)Tell Me A Joke.7)Play.8)Set Alarm.9)Speak")

def AH():
    speak.Speak("You Are " + a.get() + " And You Are My Master")
def kkk(self=frame4):
    frame.grid_remove()

    label5 = Label(frame4, text=" 1)Hi")
    label5.grid(row=6, column=2)
    label123 = Label(frame4, text="2)Who Are You?")
    label123.grid(row=7, column=2)
    label1234 = Label(frame4, text="3)Open\n4) If You Want To Hear The Text Please Press That Button '🔊' \n5)Whoami\n6)Tell Me A Joke\n7)Play\n8)Set Alarm\n9)Speak")
    label1234.grid(row=8, column=2)
    b12345 = Button(frame4, text="Back", command=lambda: [self.grid_remove(), frame.grid()])
    b12345.grid(row=9, column=2)
    button1111 = Button(frame4, text="🔊", command=AAA)
    button1111.grid(row=0, column=0, padx=10, pady=10)
frame9.grid_remove()

BTN = Button(frame5, text="Login", command=hl)
BTN.grid(row=0, column=2)
Login = Button(frame5, text="Sign up ", command=asd)
Login.grid(row=1, column=2)
root.mainloop()
