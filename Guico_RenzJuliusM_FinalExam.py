from tkinter import *
window = Tk()
window.title("Find the smallest number")
window.geometry("400x300+20+100")
def findSmallest():
    L = []
    L.append(eval(evaluate2.get()))
    L.append(eval(evaluate3.get()))
    L.append(eval(evaluate4.get()))
    evaluate.set(min(L))

lbl1 = Label(window, text = "Find the least number among three numbers")
lbl1.grid(row=0, column=1, columnspan=2,sticky=EW)

lbl2 = Label(window,text = "Enter the first number:")
lbl2.grid(row=1, column = 0,sticky=W)
evaluate2 = StringVar()

ent2 = Entry(window,bd=3,textvariable=evaluate2)
ent2.grid(row=1, column = 1)

lbl3 = Label(window,text = "Enter the second number:")
lbl3.grid(row=2, column=0)
evaluate3=StringVar()

ent3 = Entry(window,bd=3,textvariable=evaluate3)
ent3.grid(row=2,column=1)

lbl4 = Label(window,text="Enter the third number:")
lbl4.grid(row=3,column =0, sticky=W)
evaluate4 = StringVar()

ent4 = Entry(window,bd=3,textvariable=evaluate4)
ent4.grid(row=3, column=1)

btn1 = Button(window,text = "Find the smallest no.",command=findSmallest)
btn1.grid(row=4, column = 1)

lbl5 = Label(window,text="The smallest number:")
lbl5.grid(row=5,column=0,sticky=W)
evaluate = StringVar()

ent5 = Entry(window,bd=3,state="readonly",textvariable=evaluate)
ent5.grid(row=5,column=1)

mainloop()