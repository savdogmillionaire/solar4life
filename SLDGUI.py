from tkinter import *

window = Tk()
window.title("SLD make tool")
window.geometry('550x500')

# lbl1 = Label(window, text="Panel model")
# lbl1.grid(column=0, row=0)
# txt1 = Entry(window,width=10)
# txt1.grid(column=1, row=0)
#
# lbl2 = Label(window, text="Array 1 length")
# lbl2.grid(column=0, row=1)
# txt2 = Entry(window,width=10)
# txt2.grid(column=1, row=1)
#
# lbl3 = Label(window, text="Array 1 strings")
# lbl3.grid(column=0, row=2)
# txt3 = Entry(window,width=10)
# txt3.grid(column=1, row=2)
#
# lbl4 = Label(window, text="Array 2 length")
# lbl4.grid(column=0, row=3)
# txt4 = Entry(window,width=10)
# txt4.grid(column=1, row=3)
#
# lbl5 = Label(window, text="Array 2 strings")
# lbl5.grid(column=0, row=4)
# txt5 = Entry(window,width=10)
# txt5.grid(column=1, row=4)
#
# lbl6 = Label(window, text="Inverter 1 model")
# lbl6.grid(column=0, row=5)
# txt6 = Entry(window,width=10)
# txt6.grid(column=1, row=5)

lbl8 = Label(window, text="inverterno")
lbl8.grid(column=0, row=7)
txt8 = Entry(window, width=10)
txt8.grid(column=1, row=7)

lbl9 = Label(window, text="battery")
lbl9.grid(column=0, row=8)
txt9 = Entry(window, width=10)
txt9.grid(column=1, row=8)

lbl10 = Label(window, text="arrays")
lbl10.grid(column=0, row=9)
txt10 = Entry(window, width=10)
txt10.grid(column=1, row=9)

lbl11 = Label(window, text="phase")
lbl11.grid(column=0, row=10)
txt11 = Entry(window, width=10)
txt11.grid(column=1, row=10)

var = StringVar(window)
var.set("AC")
lbl12 = Label(window, text="current")
lbl12.grid(column=0, row=11)
txt12 = OptionMenu(window, var, 'AC', 'DC')
txt12.grid(column=1, row=11)

lbl13 = Label(window, text="reposit")
lbl13.grid(column=0, row=12)
txt13 = Entry(window, width=10)
txt13.grid(column=1, row=12)


def clicked1():
    # res = "array 1 model :  " + txt1.get()
    # lbl1.configure(text= res)
    # txt1.get()
    #
    # res = "array 1 length :  " + txt2.get()
    # lbl2.configure(text= res)
    # txt2.get()
    #
    # res = "array 1 strings :  " + txt3.get()
    # lbl3.configure(text=res)
    # txt3.get()
    #
    # res = "array 2 length :  " + txt4.get()
    # lbl4.configure(text= res)
    # txt4.get()
    #
    # res = "array 2 strings :  " + txt5.get()
    # lbl5.configure(text=res)
    # txt5.get()
    #
    # res = "inverter 1 model :  " + txt6.get()
    # lbl6.configure(text=res)
    # txt6.get()

    res = "inverterno" + txt8.get()
    lbl8.configure(text=res)
    txt8.get()

    res = "battery" + txt9.get()
    lbl9.configure(text=res)
    txt9.get()

    res = "arrays" + txt10.get()
    lbl10.configure(text=res)
    txt10.get()

    res = "phase" + txt11.get()
    lbl11.configure(text=res)
    txt11.get()

    res = "current" + var.get()
    lbl12.configure(text=res)
    var.get()

    res = "reposit" + txt13.get()
    lbl13.configure(text=res)
    txt13.get()


Button(window, text='Create SLD', command=window.quit).grid(row=4, column=3, sticky=W, pady=4)

window.mainloop()

# array_1_model_input = txt1.get()
# array_1_length = int(txt2.get())
# array_1_strings = int(txt3.get())
# array_2_length = int(txt4.get())
# array_2_strings = int(txt5.get())
# inverter_1_input = txt6.get()
inverterno = int(txt8.get())
battery = int(txt9.get())
arrays = int(txt10.get())
phase = int(txt11.get())
current = var.get()
reposit = int(txt13.get())
