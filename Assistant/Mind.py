from tkinter import *
import os
root=Tk()
root.title("Mind Reader")

l=Label(root,text="Choose Any Number You Think Of.")
l.grid(row=0,column=1)

def Hey():
    os.startfile("Calc.py")
    l1 = Label(root , text="Multiply it By 2.")
    l1.grid(row=2,  column=1)
    b1 = Button(root , text="Next" , command=Hey12)
    b1.grid(row=3 , column=1)
b=Button(root,text="Next",command=Hey)
b.grid(row=1,column=1)
def Hey123():

    l3 = Label(root , text="Divide The Number You Have By 2")
    l3.grid(row=6 , column=1)
    b1 = Button(root , text="Next" , command=Hey1234)
    b1.grid(row=7, column=1)
def Hey1234():
    l3 = Label(root , text="Subtract Your original Number From The Number In Your Head")
    l3.grid(row=8 , column=1)
    b1 = Button(root , text="Next" , command=Hey12345)
    b1.grid(row=9, column=1)
def Hey12345():
 l4=Label(root,text="Hmmmm Let Me Think.....",)
 l4.grid(row=10,column=1)
 l4.after(5000, lambda: [l4.destroy() , l5.grid(row=11 , column=1), b4.grid(row=12,column=1)])
 l5=Label(root,text="I Think The Number In Your Head Is 5!!!!!")
 b4=Button(root,text="Exit",command=h)

def h():
    root.quit()
def Hey12():
    l2 = Label(root , text="add 10 to it")
    l2.grid(row=4 , column=1)
    b1 = Button(root , text="Next" , command=Hey123)
    b1.grid(row=5 , column=1)


root.mainloop()