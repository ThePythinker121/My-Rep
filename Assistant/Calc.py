from tkinter import *
root =Tk()
root.title("Feras calculator Upgraded Edition")
root.iconbitmap('c:/Users/Ahmed Yakan/Downloads/Wineass-Ios7-Redesign-Calculator.ico')




e = Entry(root, width=35,borderwidth=7,bg="cyan")
e.grid(row=2, column=0, columnspan=3, padx=7, pady=5)
e.insert(0,"Enter Your Problem")

def myclick():
  thx="Thanks For Using!"
  mylabel=Label(root,text=thx,bg="black",fg="cyan")
  mylabel.grid(row=10,column=1)

def button_click(number):
    current = e.get()
    e.delete(0,END)
    e.insert(0,str(current) + str(number))
def button_clear():
    e.delete(0, END)
def button_add():
   first_number=int(e.get())
   global f_num
   global math
   math="addition"
   f_num = int (first_number )
   e.delete(0,END)
def multiply():
    first_number=e.get()
    global fi_num
    global math
    math="multiplication"
    fi_num=int(first_number)
    e.delete(0,END)
def subtruct():
    first_number = e.get()
    global fir_num
    global math
    math="subtraction"
    fir_num = float(first_number)
    e.delete(0, END)
def divide():
    first_number = e.get()
    global firs_num
    global math
    math="division"
    firs_num = int(first_number)
    e.delete(0, END)
def mod():
    first_number = e.get()
    global firstt_num
    global math
    math = "mod"
    firstt_num = int(first_number)
    e.delete(0, END)
global b
def equal():
      secondnumber = e.get()
      e.delete(0,END)
      if math == "addition":
          e.insert(0, int(f_num )+ int(secondnumber))
      if math == "subtraction":
          e.insert(0, int(fir_num )- int(secondnumber))
      if math == "division":
       e.insert(0, int (firs_num )/ int(secondnumber))



      if math =="multiplication":
          e.insert(0, int (fi_num) * int(secondnumber))
      if math == "mod":
          e.insert(0, int(firstt_num) % int(secondnumber))





b_1= Button(root,text="1",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(1))
b_2= Button(root,text="2",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(2))
b_3= Button(root,text="3",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(3))
b_4= Button(root,text="4",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(4))
b_5= Button(root,text="5",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(5))
b_6= Button(root,text="6",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(6))
b_7= Button(root,text="7",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(7))
b_8= Button(root,text="8",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(8))
b_9= Button(root,text="9",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(9))
b_0= Button(root,text="0",padx=40,pady=20,borderwidth=4,bg="cyan",command=lambda :button_click(0))
b_add=Button(root,text="+",padx=40,pady=20,borderwidth=4,bg="cyan",command=button_add)
b_equal=Button(root,text="=",padx=40,pady=20,borderwidth=4,bg="cyan",command=equal)
b_clear=Button(root,text="Clear",padx=30,pady=20,borderwidth=4,bg="cyan",command=button_clear)
b_multiply=Button(root,text="x",padx=40,pady=20,borderwidth=4,bg="cyan",command=multiply)
b_subtract=Button(root,text="-",padx=40,pady=20,borderwidth=4,bg="cyan",command=subtruct)
b_divide=Button(root,text="/",padx=40,pady=20,borderwidth=4,bg="cyan",command=divide)
b_mod=Button(root,text="%",padx=40,pady=20,borderwidth=4,bg="cyan",command=mod)
mybutton=Button(root,text="Finished?",padx=20,pady=20,borderwidth=4,bg="cyan",command=myclick)
b_0.grid(row=7, column=1)
b_1.grid(row=5, column=0)
b_2.grid(row=5, column=1)
b_3.grid(row=5, column=2)
b_4.grid(row=6, column=0)
b_5.grid(row=6, column=1)
b_6.grid(row=6, column=2)
b_7.grid(row=4, column=0)
b_8.grid(row=4, column=1)
b_9.grid(row=4, column=2)
b_add.grid(row=7,column=0)
b_equal.grid(row=9,column=0)
b_clear.grid(row=9,column=1)
b_divide.grid(row=8,column=0)
b_multiply.grid(row=8,column=1)
b_subtract.grid(row=8,column=2)
b_mod.grid(row=7,column=2)
mybutton.grid(row=9,column=2)

root.mainloop()
