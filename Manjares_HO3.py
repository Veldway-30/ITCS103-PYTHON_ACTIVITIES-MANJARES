import tkinter as tk

def add():
    num1 = entry1.get()
    num2 = entry2.get()
    try:
        num1 = float(num1)
        num2 = float(num2)
        result_label.config(text=f"The Sum of is " + str(num1+num2))
    except:
        result_label.config(text="wrong input")

def substract():
    n1 = entry1.get()
    n2 = entry2.get()
    try:
        n1 = float(n1)
        n2 = float(n2)
        result_label.config(text="Diff is " + str(n1-n2))
    except:
        result_label.config(text="wrong input")

def multiply():
    a = entry1.get()
    b = entry2.get()
    try:
        a = float(a)
        b = float(b)
        result_label.config(text="Multiply is " + str(a*b))
    except:
        result_label.config(text="wrong input")

def divide():
    x = entry1.get()
    y = entry2.get()
    try:
        x = float(x)
        y = float(y)
        if y == 0:
            result_label.config(text="cant divide by zero")
        else:
            result_label.config(text="Divide is " + str(x/y))
    except:
        result_label.config(text="wrong input")

win = tk.Tk()
win.title("CALC")
win.configure(bg="#003049")

result_label = tk.Label(win, text="Result here", bg="white")
result_label.grid(row=0, column=0, columnspan=2, sticky="nsew")

label1 = tk.Label(win, text="Enter 1st Number:", bg="white")
label1.grid(row=1, column=0, pady=10)
entry1 = tk.Entry(win)
entry1.grid(row=1, column=1)

label2 = tk.Label(win, text="Enter 2nd Number:", bg="white")
label2.grid(row=2, column=0, padx = 10)
entry2 = tk.Entry(win)
entry2.grid(row=2, column=1)

btn1 = tk.Button(win, text="Add", command=add)
btn1.grid(row=3, column=0, pady=10)

btn2 = tk.Button(win, text="Substract", command=substract)
btn2.grid(row=3, column=1, pady=10)

btn3 = tk.Button(win, text="Multiply", command=multiply)
btn3.grid(row=4, column=0, pady =1)

btn4 = tk.Button(win, text="Divide", command=divide)
btn4.grid(row=4, column=1, pady=10)

win.mainloop()
