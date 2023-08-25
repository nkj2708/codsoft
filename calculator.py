from tkinter import *

root = Tk() 
root.geometry("312x324")  
root.resizable(0, 0)  
root.title("Calculator")


def click(item):
    global expression
    expression = expression + str(item)
    itext.set(expression)


def clear(): 
    global expression 
    expression = "" 
    itext.set("")
 
 
def equal():
    global expression
    result = str(eval(expression)) 
    itext.set(result)
    expression = ""
 
expression = ""
 
 
itext = StringVar()
 
 
iframe = Frame(root, width=312, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=2)
 
iframe.pack(side=TOP)
 
ifield = Entry(iframe, font=('arial', 20, 'bold'), textvariable=itext, width=50, bg="#eee", bd=0, justify=RIGHT)
 
ifield.grid(row=0, column=0)
 
ifield.pack(ipady=10) 
 
frame = Frame(root, width=312, height=272.5, bg="grey")
 
frame.pack()
 
# first row
 
clear_btn = Button(frame, text = "C", fg = "black", width = 32, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: clear()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)
 
divide = Button(frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click("/")).grid(row = 0, column = 3, padx = 1, pady = 1)
 
# second row
 
bt7 = Button(frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(7)).grid(row = 1, column = 0, padx = 1, pady = 1)
 
bt8 = Button(frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(8)).grid(row = 1, column = 1, padx = 1, pady = 1)
 
bt9 = Button(frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(9)).grid(row = 1, column = 2, padx = 1, pady = 1)
 
btx = Button(frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click("*")).grid(row = 1, column = 3, padx = 1, pady = 1)
 
# third row
 
bt4 = Button(frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(4)).grid(row = 2, column = 0, padx = 1, pady = 1)
 
bt5 = Button(frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(5)).grid(row = 2, column = 1, padx = 1, pady = 1)
 
bt6 = Button(frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(6)).grid(row = 2, column = 2, padx = 1, pady = 1)
 
bt_ = Button(frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click("-")).grid(row = 2, column = 3, padx = 1, pady = 1)
 
# fourth row
 
bt1 = Button(frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(1)).grid(row = 3, column = 0, padx = 1, pady = 1)
 
bt2 = Button(frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(2)).grid(row = 3, column = 1, padx = 1, pady = 1)
 
bt3 = Button(frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(3)).grid(row = 3, column = 2, padx = 1, pady = 1)
 
btp = Button(frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click("+")).grid(row = 3, column = 3, padx = 1, pady = 1)
 
# fifth row
 
bt0 = Button(frame, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "pink", cursor = "hand2", command = lambda: click(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)
 
btpnt = Button(frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: click(".")).grid(row = 4, column = 2, padx = 1, pady = 1)
 
bteq = Button(frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "yellow", cursor = "hand2", command = lambda: equal()).grid(row = 4, column = 3, padx = 1, pady = 1)
 
root.mainloop()
