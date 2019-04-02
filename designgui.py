from tkinter import *

window = Tk()
window.title("Design Tool")
window.geometry('550x400')

lbl1 = Label(window, text="Panel model")
lbl1.grid(column=0, row=0)
txt1 = Entry(window,width=10)
txt1.grid(column=1, row=0)

lbl2 = Label(window, text="Array 1 length")
lbl2.grid(column=0, row=1)
txt2 = Entry(window,width=10)
txt2.grid(column=1, row=1)

lbl3 = Label(window, text="Array 1 strings")
lbl3.grid(column=0, row=2)
txt3 = Entry(window,width=10)
txt3.grid(column=1, row=2)

lbl4 = Label(window, text="Array 2 length")
lbl4.grid(column=0, row=3)
txt4 = Entry(window,width=10)
txt4.grid(column=1, row=3)

lbl5 = Label(window, text="Array 2 strings")
lbl5.grid(column=0, row=4)
txt5 = Entry(window,width=10)
txt5.grid(column=1, row=4)

lbl6 = Label(window, text="Inverter 1 model")
lbl6.grid(column=0, row=5)
txt6 = Entry(window,width=10)
txt6.grid(column=1, row=5)

lbl7 = Label(window, text="AC Breaker Current limit")
lbl7.grid(column=0, row=6)
txt7 = Entry(window,width=10)
txt7.grid(column=1, row=6)

def clicked1():
    res = "array 1 model :  " + txt1.get()
    lbl1.configure(text= res)
    txt1.get()

    res = "array 1 length :  " + txt2.get()
    lbl2.configure(text= res)
    txt2.get()

    res = "array 1 strings :  " + txt3.get()
    lbl3.configure(text=res)
    txt3.get()

    res = "array 2 length :  " + txt4.get()
    lbl4.configure(text= res)
    txt4.get()

    res = "array 2 strings :  " + txt5.get()
    lbl5.configure(text=res)
    txt5.get()

    res = "inverter 1 model :  " + txt6.get()
    lbl6.configure(text=res)
    txt6.get()

    res = "ac breaker current limit :  " + txt7.get()
    lbl7.configure(text=res)
    txt7.get()





Button(window, text='Calculate system', command=clicked1).grid(row=3, column=3, sticky=W, pady=4)
Button(window, text='QUIT', command=window.quit).grid(row=4, column=3, sticky=W, pady=4)


window.mainloop()

array_1_model_input = txt1.get()
array_1_length      = int(txt2.get())
array_1_strings         = int(txt3.get())
array_2_length      = int(txt4.get())
array_2_strings         = int(txt5.get())
inverter_1_input    = txt6.get()
ac_breaker_current_limit = int(txt7.get())
