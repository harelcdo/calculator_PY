import tkinter as tk
from tkinter import *
from tkinter import messagebox


root=tk.Tk()
root.geometry("250x400")

#label
data=StringVar()
lbl=Label(root,bg="white",fg="black",font=("Verdana",20))
lbl.pack(expand=True,fill="both")

#Frame
frame1=Frame(root,bg="#000000")
frame1.pack(expand=True,fill="both")

frame2=Frame(root,bg="white")
frame2.pack(expand=True,fill="both")

frame3=Frame(root,bg="blue")
frame3.pack(expand=True,fill="both")

frame4=Frame(root,bg="yellow")
frame4.pack(expand=True,fill="both")

#Frame1 Buttons
b1=Button(frame1,text="1",border=1,bg="black",fg="white")
b1.pack(side=LEFT,expand=True,fill="both")

b2=Button(frame1,text="2",border=1,bg="black",fg="white")
b2.pack(side=LEFT,expand=True,fill="both")

b3=Button(frame1,text="3",border=1,bg="black",fg="white")
b3.pack(side=LEFT,expand=True,fill="both")

b_add=Button(frame1,text="+",border=1,bg="black",fg="white")
b_add.pack(side=LEFT,expand=True,fill="both")

#Frame2 Buttons
b4=Button(frame2,text="4",border=1,bg="black",fg="white")
b4.pack(side=LEFT,expand=True,fill="both")

b5=Button(frame2,text="5",border=1,bg="black",fg="white")
b5.pack(side=LEFT,expand=True,fill="both")

b6=Button(frame2,text="6",border=1,bg="black",fg="white")
b6.pack(side=LEFT,expand=True,fill="both")

b_sub=Button(frame2,text="-",border=1,bg="black",fg="white")
b_sub.pack(side=LEFT,expand=True,fill="both")

#Frame3 Buttons
b7=Button(frame3,text="7",border=1,bg="black",fg="white")
b7.pack(side=LEFT,expand=True,fill="both")

b8=Button(frame3,text="8",border=1,bg="black",fg="white")
b8.pack(side=LEFT,expand=True,fill="both")

b9=Button(frame3,text="9",border=1,bg="black",fg="white")
b9.pack(side=LEFT,expand=True,fill="both")

b_multi=Button(frame3,text="*",border=1,bg="black",fg="white")
b_multi.pack(side=LEFT,expand=True,fill="both")

#Frame4 Buttons
b_clear= Button(frame4,text="c",border=1,bg="black",fg="white")
b_clear.pack(side=LEFT,expand=TRUE,fill="both")

b0= Button(frame4,text="0",border=1,bg="black",fg="white")
b0.pack(side=LEFT,expand=TRUE,fill="both")

b_div= Button(frame4,text="/",border=1,bg="black",fg="white")
b_div.pack(side=LEFT,expand=TRUE,fill="both")

b_equal= Button(frame4,text="=",border=1,bg="black",fg="white")
b_equal.pack(side=LEFT,expand=TRUE,fill="both")





mainloop()