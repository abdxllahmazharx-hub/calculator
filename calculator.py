import math 
from statistics import quantiles
from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("500x500")

equation = StringVar()
eqStr = ""

def calculator(event):
    global eqStr
    char = event.widget.cget("text")
    if char == "=" :
        answer = eval(equation.get())
        equation.set(answer)
    elif char == "√" :
        answer = math.sqrt(float(equation.get()))
        equation.set(answer)
    elif char == "^" :
        eqStr += "**"
        equation.set(eqStr)
    elif char == "AC" :
        eqStr = ""
        equation.set("")
    elif char == "⌫" :
        eqStr = eqStr[: -1]
        equation.set(eqStr)
    else:
        eqStr = eqStr + char
        equation.set(eqStr)

entry = Entry(root, font= ("Arial", 30), relief=SUNKEN, borderwidth=10, textvariable=equation)
entry.grid(row=0 , column=0, columnspan=4)

button = Button(root, text="7", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=1, column=0)
button.bind("<Button-1>",calculator)

button = Button(root, text="8", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=1, column=1)
button.bind("<Button-1>",calculator)

button = Button(root, text="9", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=1, column=2)
button.bind("<Button-1>",calculator)

button = Button(root, text="+",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=1, column=3)
button.bind("<Button-1>",calculator)

# -----------------------------------------

button = Button(root, text="4", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=0)
button.bind("<Button-1>",calculator)

button = Button(root, text="5", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=1)
button.bind("<Button-1>",calculator)

button = Button(root, text="6", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=2)
button.bind("<Button-1>",calculator)

button = Button(root, text="-",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=2, column=3)
button.bind("<Button-1>",calculator)

# -----------------------------------------

button = Button(root, text="1", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=0)
button.bind("<Button-1>",calculator)

button = Button(root, text="2", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=1)
button.bind("<Button-1>",calculator)

button = Button(root, text="3", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=2)
button.bind("<Button-1>",calculator)

button = Button(root, text="x",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=3, column=3)
button.bind("<Button-1>",calculator)

# -----------------------------------------

button = Button(root, text=".", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=0)
button.bind("<Button-1>",calculator)

button = Button(root, text="0", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=1)
button.bind("<Button-1>",calculator)

button = Button(root, text="/", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=2)
button.bind("<Button-1>",calculator)

button = Button(root, text="=",bg="green", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=4, column=3)
button.bind("<Button-1>",calculator)

# -----------------------------------------

button = Button(root, text="√",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=0)
button.bind("<Button-1>",calculator)

button = Button(root, text="^",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=1)
button.bind("<Button-1>",calculator)

button = Button(root, text="AC",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=2)
button.bind("<Button-1>",calculator)

button = Button(root, text="⌫",bg="orange", font= ("Arial", 30), height=1, width=4, relief=RAISED, borderwidth=6)
button.grid(row=5, column=3)
button.bind("<Button-1>",calculator)


root.mainloop()
