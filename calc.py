import tkinter as tk
from tkinter.ttk import *
import subprocess
def CE():
    svarVindu.delete(0, "end")

def dlt():
    tekst = svarVindu.get()
    lengde = len(tekst)
    svarVindu.delete(lengde-1,"end")

def pwr():
    root.destroy()
    subprocess.call([r'C:\power.bat'])


def seven():
    svarVindu.insert("end", "7")

def eigth():
    svarVindu.insert("end", "8")

def nine():
    svarVindu.insert("end", "9")

def multi():
    svarVindu.insert("end", "×")

def four():
    svarVindu.insert("end", "4")

def five():
    svarVindu.insert("end", "5")

def six():
    svarVindu.insert("end", "6")

def add():
    svarVindu.insert("end", "+")

def one():
    svarVindu.insert("end", "1")

def two():
    svarVindu.insert("end", "2")

def three():
    svarVindu.insert("end", "3")

def subtract():
    svarVindu.insert("end", "-")

def zero():
    svarVindu.insert("end", "0")

def comma():
    svarVindu.insert("end", ",")


def divide():
    svarVindu.insert("end", "÷")

def equal():
    text = svarVindu.get()
    new_text = ""
    for i in text:
        if i == "÷":
            i = "/"
        if i == ",":
            i = "."
        if i == "×":
            i = "*"
        new_text = new_text + i
    answers = eval(new_text)
    new_new_text = ""
    for i in str(answers):
        if i == ".":
            i = ","
        new_new_text = new_new_text + i
    CE()
    svarVindu.insert("end", new_new_text)






root = tk.Tk()
photo = tk.PhotoImage(file = "C:\power 27 px.png")
svarVindu = tk.Entry(root, font = ("arial", 20))
svarVindu.grid(row = 0, column = 0 , columnspan= 4)


ceButton = tk.Button(root, text = "CE", font = ("arial", 20), command= CE)
ceButton.grid(row = 1, column = 0 , sticky= "we")

cButton = tk.Button(root, text = "C", font = ("arial", 20),command= CE)
cButton.grid(row = 1, column = 1 , sticky= "we") 

delButton = tk.Button(root, text = "del", font = ("arial", 20),command= dlt)
delButton.grid(row = 1, column = 2, sticky= "we")

pwrButton = tk.Button(root, image = photo,command = pwr)
pwrButton.grid(row = 1, column = 3, sticky= "nswe")

sevenButton = tk.Button(root, text= "7", font = ("arial", 20),command = seven)
sevenButton.grid(row = 2, column = 0, sticky= "we")

eigthButton = tk.Button(root, text= "8", font = ("arial", 20),command = eigth)
eigthButton.grid(row = 2, column = 1, sticky= "we")

nineButton = tk.Button(root, text= "9", font = ("arial", 20),command = nine)
nineButton.grid(row = 2, column = 2, sticky= "we")

multiButton = tk.Button(root, text= "×", font = ("arial", 20),command = multi)
multiButton.grid(row = 2, column = 3, sticky= "we")

fourButton = tk.Button(root, text= "4", font = ("arial", 20),command = four)
fourButton.grid(row = 3, column = 0, sticky= "we")

fiveButton = tk.Button(root, text= "5", font = ("arial", 20),command =five)
fiveButton.grid(row = 3, column = 1, sticky= "we")

sixButton = tk.Button(root, text= "6", font = ("arial", 20),command = six)
sixButton.grid(row = 3, column = 2, sticky= "we")

addButton = tk.Button(root, text= "+", font = ("arial", 20), command = add)
addButton.grid(row = 3, column = 3, sticky= "we")

oneButton = tk.Button(root, text= "1", font = ("arial", 20),command = one)
oneButton.grid(row = 4, column = 0, sticky= "we")

twoButton = tk.Button(root, text= "2", font = ("arial", 20), command = two)
twoButton.grid(row = 4, column = 1, sticky= "we")

threeButton = tk.Button(root, text= "3", font = ("arial", 20), command = three)
threeButton.grid(row = 4, column = 2, sticky= "we")

subtract = tk.Button(root, text= "-", font = ("arial", 20), command = subtract)
subtract.grid(row = 4, column = 3, sticky= "we")

zeroButton = tk.Button(root, text= "0", font = ("arial", 20), command = zero)
zeroButton.grid(row = 5, column = 0, sticky= "we")

commaButton = tk.Button(root, text= ",", font = ("arial", 20), command = comma)
commaButton.grid(row = 5, column = 1, sticky= "we")

equalButton = tk.Button(root, text= "=", font = ("arial", 20), command = equal)
equalButton.grid(row = 5, column = 2, sticky= "we")

divideButton = tk.Button(root, text= "÷", font = ("arial", 20), command = divide)
divideButton.grid(row = 5, column = 3, sticky= "we")


root.mainloop()