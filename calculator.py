import tkinter as tk
from tkinter import *


app = tk.Tk()
app.geometry("170x230")
app.title("calculator")
app.maxsize(170, 230)
app.minsize(170, 230)

ent = Entry(app,  width=16,  borderwidth=3,  relief=RIDGE)
ent.grid(pady=10, row=0, sticky="w", padx=15)


def clearf():
    global ent
    ent.delete(0,  "end")


def delete():
    global ent
    a = ent.get()
    ent.delete(first=len(a) - 1,  last="end")


def fresult():
    global ent

    def clearf():
        global ent
        ent.delete(0, "end")

    if ent.get() == "":
        pass
    elif ent.get()[0] == "0":
        ent.delete(0,  "end")
    else:
        c_res = ent.get()
        c_res = eval(c_res)
        clearf()
        ent.insert("end",  c_res)


clean = Button(app, text="C", width=2, command=clearf, bg="green", fg="white", relief=RIDGE)
clean.grid(row=0, sticky="w", padx=125)
Char_nine = Button(app, text="9", width=2, command=lambda: ent.insert("end", "9"), borderwidth=3, relief=RIDGE)
Char_nine.grid(row=1, sticky="w", padx=15)
Char_eight = Button(app, text="8", width=2, command=lambda: ent.insert("end", "8"), borderwidth=3, relief=RIDGE)
Char_eight.grid(row=1, sticky="w", padx=45)
Char_seven = Button(app, text="7", width=2, command=lambda: ent.insert("end", "7"), borderwidth=3, relief=RIDGE)
Char_seven.grid(row=1, sticky="w", padx=75)
Char_plus = Button(app, text="+", width=2, command=lambda: ent.insert("end", "+"), borderwidth=3, relief=RIDGE)
Char_plus.grid(row=1, sticky="e", padx=125)
Char_six = Button(app, text="6", width=2, command=lambda: ent.insert("end", "6"), borderwidth=3, relief=RIDGE)
Char_six.grid(row=2, sticky="w", padx=15, pady=5)
Char_five = Button(app, text="5", width=2, command=lambda: ent.insert("end", "5"), borderwidth=3, relief=RIDGE)
Char_five.grid(row=2, sticky="w", padx=45, pady=5)
Char_four = Button(app, text="4", width=2, command=lambda: ent.insert("end", "4"), borderwidth=3, relief=RIDGE)
Char_four.grid(row=2, sticky="w", padx=75, pady=5)
Char_minus = Button(app, text="-", width=2, command=lambda: ent.insert("end", "-"), borderwidth=3, relief=RIDGE)
Char_minus.grid(row=2, sticky="e", padx=125, pady=5)
Char_three = Button(app, text="3", width=2, command=lambda: ent.insert("end", "3"), borderwidth=3, relief=RIDGE)
Char_three.grid(row=3, sticky="w", padx=15, pady=5)
Char_two = Button(app, text="2", width=2, command=lambda: ent.insert("end", "2"), borderwidth=3, relief=RIDGE)
Char_two.grid(row=3, sticky="w", padx=45, pady=5)
Char_one = Button(app, text="1", width=2, command=lambda: ent.insert("end", "1"), borderwidth=3, relief=RIDGE)
Char_one.grid(row=3, sticky="w", padx=75, pady=5)
Char_multiply = Button(app, text="*", width=2, command=lambda: ent.insert("end", "*"), borderwidth=3, relief=RIDGE)
Char_multiply.grid(row=3, sticky="e", padx=125, pady=5)
Char_zero = Button(app, text="0", width=2, command=lambda: ent.insert("end", "0"), borderwidth=3, relief=RIDGE)
Char_zero.grid(row=4, sticky="w", padx=15, pady=5)
Char_double_zero = Button(app, text="00", width=2, command=lambda: ent.insert("end", "00"), borderwidth=3, relief=RIDGE)
Char_double_zero.grid(row=4, sticky="w", padx=45, pady=5)
Char_dot = Button(app, text=".", width=2, command=lambda: ent.insert("end", "."), borderwidth=3, relief=RIDGE)
Char_dot.grid(row=4, sticky="w", padx=75, pady=5)
Char_divide = Button(app, text="/", width=2, command=lambda: ent.insert("end", "/"), borderwidth=3, relief=RIDGE)
Char_divide.grid(row=4, sticky="e", padx=125, pady=5)
result = Button(app, text="=", width=10, command=fresult, bg="green", fg="white", borderwidth=3, relief=RIDGE)
result.grid(row=5, sticky="w", padx=15, pady=5)
Char_modulus = Button(app, text="%", width=2, command=lambda: ent.insert("end", "%"), borderwidth=3, relief=RIDGE)
Char_modulus.grid(row=5, sticky="e", padx=125, pady=5)
delete = Button(app, text="del", width=2, command=delete, borderwidth=3, relief=RIDGE)
delete.grid(row=5, sticky="w", padx=80, pady=5)

app.mainloop()
