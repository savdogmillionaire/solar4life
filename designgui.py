import tkinter as tk
from tkinter import ttk
import sqlite3

global array_1_model_input, array_1_length, array_1_strings, \
    array_2_length, array_2_strings, inverter_1_input, ac_breaker_current_limit


def combo_values_input():
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()
    query = cur.execute('SELECT Panel FROM Panelspecifications')
    data = []
    for row in cur.fetchall():
        data.append(row[0])
        data.append(row[0])
    return data

    cur.close()
    conn.close()


def combo_values_input_inverter():
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()

    query2 = cur.execute('SELECT Inverter FROM Inverterspecifications')

    data = []
    for row in cur.fetchall():
        data.append(row[0])
        data.append(row[0])
    return data

    cur.close()
    conn.close()


def clicked1():
    res = "array 1 model :  " + combo.get()
    lbl1.configure(text=res)
    combo.get()

    res = "array 1 model :  " + txt2.get()
    lbl1.configure(text=res)
    txt2.get()

    res = "array 1 strings :  " + txt3.get()
    lbl3.configure(text=res)
    txt3.get()

    res = "array 2 length :  " + txt4.get()
    lbl4.configure(text=res)
    txt4.get()

    res = "array 2 strings :  " + txt5.get()
    lbl5.configure(text=res)
    txt5.get()

    res = "inverter 1 model :  " + combo2.get()
    lbl6.configure(text=res)
    combo2.get()


window = tk.Tk()
window.title("Design Tool")
window.geometry('950x900')

lbl1 = tk.Label(window, text="Panel model")
lbl1.grid(column=0, row=0)
combo = ttk.Combobox(window, width=50, height=20)
combo.grid(column=1, row=0)
combo['values'] = combo_values_input()

lbl2 = tk.Label(window, text="Array 1 length")
lbl2.grid(column=0, row=1)
txt2 = tk.Entry(window, width=10)
txt2.grid(column=1, row=1)

lbl3 = tk.Label(window, text="Array 1 strings")
lbl3.grid(column=0, row=2)
txt3 = tk.Entry(window, width=10)
txt3.grid(column=1, row=2)

lbl4 = tk.Label(window, text="Array 2 length")
lbl4.grid(column=0, row=3)
txt4 = tk.Entry(window, width=10)
txt4.grid(column=1, row=3)

lbl5 = tk.Label(window, text="Array 2 strings")
lbl5.grid(column=0, row=4)
txt5 = tk.Entry(window, width=10)
txt5.grid(column=1, row=4)

lbl6 = tk.Label(window, text="Inverter 1 model")
lbl6.grid(column=0, row=5)
combo2 = ttk.Combobox(window, width=50, height=20)
combo2.grid(column=1, row=5)
combo2['values'] = combo_values_input_inverter()

lbl7 = tk.Label(window, text="AC Breaker Current limit")
lbl7.grid(column=0, row=6)
txt7 = tk.Entry(window, width=10)
txt7.grid(column=1, row=6)

calculate = tk.Button(window, text='calc', command=clicked1)
calculate.grid(column=4, row=7)
quit = tk.Button(window, text='GO', command=quit)
quit.grid(column=4, row=8)










window.mainloop()

array_1_model_input = combo.get()
array_1_length = int(txt2.get())
array_1_strings = int(txt3.get())
array_2_length = int(txt4.get())
array_2_strings = int(txt5.get())
inverter_1_input = combo2.get()
ac_breaker_current_limit = int(txt7.get())
