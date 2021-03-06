import tkinter as tk
from tkinter import ttk
import sqlite3
import os
import webbrowser
from reportlab.pdfgen import canvas
from reportlab.lib.colors import black

conn = sqlite3.connect('VRCtable.db')
cur = conn.cursor()


# entry gui to design solar panel system.
def designgui():
    ##assigning some variables to be global. i do this a lot. helpts to pass values between functions
    ## in this program
    global array_1_model_input, array_1_length, array_1_strings, \
        array_2_length, array_2_strings, inverter_1_input, inverter_2_input, \
        ac_breaker_current_limit, battery_input, SS_Switch, array_3_model_input, \
        array_3_length, array_3_strings, array_4_length, array_4_strings, check, application, check

    ## combo value input functions simply access each row of the database and saves it to a list.
    ## a drop down box can then be created using values from this list
    def combo_values_input_panel():

        query = cur.execute('SELECT Panel FROM Panelspecifications')
        data = []
        for row in cur.fetchall():
            data.append(row[0])
        return data

    def combo_values_input_inverter():


        query2 = cur.execute('SELECT Inverter FROM Inverterspecifications')

        data = []
        for row in cur.fetchall():
            data.append(row[0])
        return data

    def combo_values_input_battery():

        query3 = cur.execute('SELECT Battery FROM Batteryspecifications')

        data = []
        for row in cur.fetchall():
            data.append(row[0])
        return data

    def combo_values_input_breaker():

        query2 = cur.execute('SELECT ACBreaker FROM ACBreakerspecifications')

        data = []
        for row in cur.fetchall():
            data.append(row[0])
        return data

    # creates a function that will allow the user to input data for when the system has 3 or more arrays,
    def more_array():

        global \
            txt12_array_4_length, txt13_array_4_strings, combo_panel_2



        lbl12 = tk.Label(window, text="Array 4 length")
        lbl12.grid(column=0, row=12)
        txt12_array_4_length = tk.Entry(window, width=10)
        txt12_array_4_length.grid(column=1, row=12)

        lbl3 = tk.Label(window, text="Array 4 strings")
        lbl3.grid(column=0, row=13)
        txt13_array_4_strings = tk.Entry(window, width=10)
        txt13_array_4_strings.grid(column=1, row=13)

        lbl14 = tk.Label(window, text="Panel 2 model")
        lbl14.grid(column=0, row=14)
        combo_panel_2 = ttk.Combobox(window, width=30, height=20)
        combo_panel_2.set('None')
        combo_panel_2.grid(column=1, row=14)
        combo_panel_2['values'] = combo_values_input_panel()

        # making a check value so that later parts of the code know that there are 3 or more arrays.




    window = tk.Tk()
    window.title("Design Tool")
    window.geometry('500x400')
    check = 0

    lbl1 = tk.Label(window, text="Panel 1 model")
    lbl1.grid(column=0, row=0)
    combo = ttk.Combobox(window, width=30, height=20)
    combo.set('SunPower P19 320W Residential')
    combo.grid(column=1, row=0)
    combo['values'] = combo_values_input_panel()

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
    combo2 = ttk.Combobox(window, width=30, height=20)
    combo2.set('Fronius Symo 10.0kW -M')
    combo2.grid(column=1, row=5)
    combo2['values'] = combo_values_input_inverter()

    lbl_inv_2 = tk.Label(window, text="Inverter 2 model")
    lbl_inv_2.grid(column=0, row=6)
    combo_inv_2 = ttk.Combobox(window, width=30, height=20)
    combo_inv_2.set('None')
    combo_inv_2.grid(column=1, row=6)
    combo_inv_2['values'] = combo_values_input_inverter()

    lbl8 = tk.Label(window, text="Battery model")
    lbl8.grid(column=0, row=7)
    combo4 = ttk.Combobox(window, width=30, height=20)
    combo4.set('None')
    combo4.grid(column=1, row=7)
    combo4['values'] = combo_values_input_battery()

    lbl7 = tk.Label(window, text="Solar Supply Main Switch")
    lbl7.grid(column=0, row=8)
    txt7 = ttk.Combobox(window, width=30, height=20)
    txt7.set('250V 1P 63A 6kA Suntree SL7-63')
    txt7.grid(column=1, row=8)
    txt7['values'] = combo_values_input_breaker()

    lbl9 = tk.Label(window, text="AC Breaker")
    lbl9.grid(column=0, row=9)
    txt9 = ttk.Combobox(window, width=30, height=20)
    txt9.set('250V 1P 63A 6kA Suntree SUKF')
    txt9.grid(column=1, row=9)
    txt9['values'] = combo_values_input_breaker()

    lbl_app = tk.Label(window, text="application")
    lbl_app.grid(column=0, row=17)
    txt_app = ttk.Combobox(window, width=30, height=20)
    txt_app.set('Residential')
    txt_app.grid(column=1, row=17)
    txt_app['values'] = ['Residential', 'Commercial']

    lbl10 = tk.Label(window, text="Array 3 length")
    lbl10.grid(column=0, row=10)
    txt10_array_3_length = tk.Entry(window, width=10)
    txt10_array_3_length.grid(column=1, row=10)

    lbl11 = tk.Label(window, text="Array 3 strings")
    lbl11.grid(column=0, row=11)
    txt11_array_3_strings = tk.Entry(window, width=10)
    txt11_array_3_strings.grid(column=1, row=11)

    var = tk.IntVar(window)
    inv_2_3_array_checklbl = tk.Label(window, text="2 inverters?")
    inv_2_3_array_checklbl.grid(column=2, row=15)
    inv_2_3_array_check = tk.Checkbutton(window, variable=var)
    inv_2_3_array_check.grid(column=2, row=16)
    inv_2_3_array_check.var = var
    calculate = tk.Button(window, text='3+ arrays', command=more_array)
    calculate.grid(column=5, row=9)

    quit = tk.Button(window, text='GO', command=window.quit)
    quit.grid(column=1, row=16)

    window.mainloop()

    #assigning to global variables things that have ben entered into the gui window.
    array_1_model_input = combo.get()
    array_1_length = int(txt2.get())
    array_1_strings = int(txt3.get())
    try:
        array_2_length = int(txt4.get())
        array_2_strings = int(txt5.get())
    except:
        array_2_length = 0
        array_2_strings = 0
    try:
        array_3_length = int(txt10_array_3_length.get())
        array_3_strings = int(txt11_array_3_strings.get())
    except:
        array_3_length = 0
        array_3_strings = 0
    array_3_model_input = combo.get()
    check = inv_2_3_array_check.var.get()
    inverter_1_input = combo2.get()
    inverter_2_input = combo_inv_2.get()
    ac_breaker_current_limit = txt7.get()
    SS_Switch = txt9.get()
    battery_input = combo4.get()
    application = txt_app.get()
    if check == 1:
        try:
            array_3_model_input = combo_panel_2.get()
        except:
            array_3_model_input = array_1_model_input
        array_3_length = int(txt10_array_3_length.get())
        array_3_strings = int(txt11_array_3_strings.get())
        try:
            array_4_length = int(txt12_array_4_length.get())
            array_4_strings = int(txt13_array_4_strings.get())
        except:
            array_4_length = 0
            array_4_strings = 0

    window.destroy()


##calculation program.
def input_from_main():
    #assigning system classes as being global variables.
    global system_1, system_2

    # creating classes. these classes can be called and new variables made for each part of the system.
    # room for expansion perhaps.
    class array:
        def __init__(self, number, model, panels, strings):
            self.number = number
            self.model = model
            cur.execute('SELECT VocV FROM Panelspecifications where Panel=?', (model,))
            self.panel_Voc = cur.fetchone()
            cur.execute('SELECT Voctemperaturecoeffcient_pc_per_C FROM Panelspecifications where Panel=?', (model,))
            self.Voctemperaturecoeffcient_pc_per_C = cur.fetchone()
            cur.execute('SELECT IscA FROM Panelspecifications where Panel=?', (model,))
            self.panel_isc = cur.fetchone()[0]
            cur.execute('SELECT PmaxW FROM Panelspecifications where Panel=?', (model,))
            self.wattage = cur.fetchone()
            self.panels = panels
            self.strings = strings

    class string(array):
        def __init__(self, number, model, panels, strings, str_number, length):
            array.__init__(self, number, model, panels, strings)
            self.str_number = str_number
            self.length = length

    class inverter:
        def __init__(self, number, model):
            self.number = number
            self.model = model
            ## inverter database searching
            cur.execute('SELECT MaxACCurrent FROM Inverterspecifications where Inverter=?', (model,))
            Max_AC_inverter_current = cur.fetchone()
            self.Max_AC_inverter_current = Max_AC_inverter_current
            cur.execute('SELECT MinDCInputVoltageV FROM Inverterspecifications where Inverter=?', (model,))
            panel_startup_input_voltage = cur.fetchone()
            self.panel_startup_input_voltage = panel_startup_input_voltage
            cur.execute('SELECT ACNominalPowerW FROM Inverterspecifications where Inverter=?', (model,))
            nominal_output = cur.fetchone()
            self.nominal_output = nominal_output
            cur.execute('SELECT MaximuminputshortcircuitcurrentforMPPT1A FROM Inverterspecifications where Inverter=?',
                        (model,))
            I_mppt_max = cur.fetchone()
            self.I_mppt_max = I_mppt_max
            cur.execute('SELECT MaxInputCurrent1A FROM Inverterspecifications where Inverter=?', (model,))
            I_DC_max = cur.fetchone()
            self.I_DC_max = I_DC_max


    ## the meat of the calculations are performed here. should be verififed against excel designer tool
    # to begin with. works well for smaller systems.
    # TODO verify calcs for 3 or more arrays. i doubt it is 100% accurate.
    class systemspecs:
        # inputs
        def __init__(self, array1, array2, array3, inverter1, string1, string2, string3, string4, string5, string6,
                     application):

            self.array1 = array1
            self.array2 = array2
            self.array3 = array3
            self.inverter1 = inverter1
            self.string1 = string1
            self.string2 = string2
            self.string3 = string3
            self.string4 = string4
            self.application = application

        # calculates total open circuit voltage taking weather into account
        def array_Voc(self):
            array_Voc_1 = self.array1.panels * self.array1.panel_Voc[0]
            array_Voc_2 = self.array2.panels * self.array2.panel_Voc[0]
            array_Voc_3 = self.array3.panels * self.array3.panel_Voc[0]
            return array_Voc_1, array_Voc_2, array_Voc_3

        # calculates total open circuit voltage taking weather into account
        def panel_Voc_minus_10(self):
            panel_1_Voc_minus_10 = self.array1.panel_Voc[0] + (
                    ((self.array1.Voctemperaturecoeffcient_pc_per_C[0] / 100) * -35) * self.array1.panel_Voc[0])
            panel_2_Voc_minus_10 = self.array2.panel_Voc[0] + (
                    ((self.array2.Voctemperaturecoeffcient_pc_per_C[0] / 100) * -35) * self.array2.panel_Voc[0])
            panel_3_Voc_minus_10 = self.array3.panel_Voc[0] + (
                    ((self.array3.Voctemperaturecoeffcient_pc_per_C[0] / 100) * -35) * self.array3.panel_Voc[0])
            return panel_1_Voc_minus_10, panel_2_Voc_minus_10, panel_3_Voc_minus_10

        def array_Voc_minus_10(self):
            array_1_Voc_minus_10 = self.panel_Voc_minus_10()[0] * self.array1.panels
            array_2_Voc_minus_10 = self.panel_Voc_minus_10()[1] * self.array2.panels
            array_3_Voc_minus_10 = self.panel_Voc_minus_10()[1] * self.array3.panels
            return array_1_Voc_minus_10, array_2_Voc_minus_10, array_3_Voc_minus_10 

        ##calcualtes total short circuit current
        def array_Isc(self):
            array_1_Isc = self.array1.strings * self.array1.panel_isc
            array_2_Isc = self.array2.strings * self.array2.panel_isc
            array_3_Isc = self.array3.strings * self.array3.panel_isc
            return array_1_Isc, array_2_Isc, array_3_Isc

        # checks whether the array ISC will cause clipping but will still work, if it the configuration cant be used at all,
        # or if it is fine
        def inverter_mppt_max_check_1(self):
            array_isc1 = (self.array_Isc()[0])

            if array_isc1 < self.inverter1.I_DC_max[0] and array_isc1 <= self.inverter1.I_mppt_max[0]:
                return "ARRAY 1 GOOD"
            if array_isc1 > self.inverter1.I_DC_max[0] and array_isc1 < self.inverter1.I_mppt_max[0]:
                return "ARRAY 1 GONNA CLIP"
            if array_isc1 >= self.inverter1.I_DC_max[0] and array_isc1 > self.inverter1.I_mppt_max[0]:
                raise ValueError('must lower ISC of array 1, configuration wont work')

        def inverter_mppt_max_check_2(self):
            array_isc2 = (self.array_Isc()[1])
            if array_isc2 < self.inverter1.I_DC_max[0] and array_isc2 <= self.inverter1.I_mppt_max[0]:
                return "ARRAY 2 GOOD"
            if array_isc2 > self.inverter1.I_DC_max[0] and array_isc2 < self.inverter1.I_mppt_max[0]:
                return "ARRAY 2 GONNA CLIP"
            if array_isc2 >= self.inverter1.I_DC_max[0] and array_isc2 > self.inverter1.I_mppt_max[0]:
                raise ValueError('must lower ISC of array 2, configuration wont work')

        def inverter_mppt_max_check_3(self):
            array_isc3 = (self.array_Isc()[1])
            if array_isc3 < self.inverter1.I_DC_max[0] and array_isc3 <= self.inverter1.I_mppt_max[0]:
                return "ARRAY 3 GOOD"
            if array_isc3 > self.inverter1.I_DC_max[0] and array_isc3 < self.inverter1.I_mppt_max[0]:
                return "ARRAY 3 GONNA CLIP"
            if array_isc3 >= self.inverter1.I_DC_max[0] and array_isc3 > self.inverter1.I_mppt_max[0]:
                raise ValueError('must lower ISC of array 3, configuration wont work')

        ##checks to see if the total array wattage is less than CEC mandated max wattage guideline.
        # based on nominal inverter output
        def CEC_Oversize_Check(self):
            oversize = self.array1.panels * self.array1.wattage[0]
            if self.array2.panels > 0:
                oversize += self.array2.panels * self.array2.wattage[0]
            if self.array3.panels > 0:
                oversize += self.array3.panels * self.array3.wattage[0]
            answer2 = self.inverter1.nominal_output[0] * 1.33
            if oversize > answer2:
                return "Array wattage of %dW is larger than CEC guidelines of %dW, please change" % (oversize, answer2)
            else:
                return "Array wattage of %dW conforms to CEC guidelines of %dW" % (oversize, answer2)

        # checks how many panels can be placed for each inverter, and checks to tsee if the
        # applications is residential or commercial when calculating
        def Max_panels(self):
            biggest_Voc = max(self.panel_Voc_minus_10())
            if self.application == 'Residential':
                Max_panels = 600 / biggest_Voc
                return Max_panels
            if self.application == 'Commercial':
                Max_panels = 1000 / biggest_Voc
                return Max_panels

        # checks how many panels can be placed for each inverter, and checks to tsee if the
        # applications is residential or commercial when calculating
        def Res_Com_check(self):
            arraysize = max(self.array_Voc_minus_10())


            if self.application == 'Residential':
                if arraysize > 600:
                    raise ValueError('Please lower Voc minus 10 of array')
                return 'array Voc of %s less than 600V limit ' % arraysize
            if self.application == 'Commercial':
                if arraysize > 1000:
                    raise ValueError('Please lower Voc minus 10 of array')
                return 'array Voc of %s is less than 1000V limit ' % arraysize

        # checks if there are a minimum amount of panel to exceed the minimum inverter startup voltage
        def Min_panels_startup(self):
            smallest_Voc = min(self.panel_Voc_minus_10())
            answer = self.inverter1.panel_startup_input_voltage[0] / smallest_Voc
            return answer

        # calculates the maximu amount of panels that can be placed that will be under the maximim system rating
        def Power_optimiser_limit(self):
            oversize1 = self.inverter1.nominal_output[0] * (4 / 3)
            answer = oversize1 / (self.array1.wattage[0] + self.array2.wattage[0])
            return "Number of Panels less than or equal to allowed based on %.2fW inverter oversizing: %d" % (
                oversize1, answer)

        ## checks if the ac breaekr rating is 1.2 * the max inverter dc output
        def Circuit_breaker_current_limit(self, ac_breaker_current):
            answer = ac_breaker_current * 1.2
            if self.inverter1.Max_AC_inverter_current[0] > answer:
                raise ValueError(
                    'Max AC output current of the Inverter is greater than chosen maximum allowed AC Breaker')
                # return "Max AC output current of the Inverter %dA is greater than maximum allowed AC Breaker " \
                # "current of %dA, please change" % (self.inverter1.Max_AC_inverter_current, answer)
            else:
                return "Maximum allowed AC Breaker current chosen of %dA works with Inverter output " \
                       "current of %dA" % (answer, self.inverter1.Max_AC_inverter_current[0])

        # checks if the strings in an array are of uneven length. should be obsolete.
        def Even_Odd_string_length(self):
            if self.array1.strings == 1 and self.array2.strings == 1:
                answer = 'string length comparison not applicable'
            elif self.array1.strings > 1 and self.string1.length % self.string2.length != 0:
                answer = 'uneven string length in array'
            elif self.array2.strings > 1 and self.string3.length % self.string4.length != 0:
                answer = 'uneven string length in array'
            else:
                answer = 'string lengths of mppt are equal'
            return answer

        ## TODO implement solar edge calculations.
        def solar_edge_checks(self):
            pass
            # check panel Voc minus 10 vs. optimiser limit
            # check string wattage against inverter optimiser limit.

    ## TODO maybe implement ability to read mppt 1 and 2. for now just 1
    ## below area assigns values entered into previous textbox to parts of the system.
    cur.execute('SELECT Current FROM ACBreakerspecifications where ACBreaker=?', (ac_breaker_current_limit,))
    ac_breaker_current = int(cur.fetchone()[0])
    inverter_1 = inverter(1, inverter_1_input)
    inverter_2 = inverter(2, inverter_2_input)
    array_1 = array(1, array_1_model_input, array_1_length, array_1_strings)
    array_2 = array(2, array_1_model_input, array_2_length, array_2_strings)
    if inverter_2 == "None":
        array_3 = array(3, array_3_model_input, 0, 0)
        string_5 = string(3, array_3_model_input, 0, 0, 5, 0)
        string_6 = string(3, array_3_model_input, 0, 0, 6, 0)
    else:
        array_3 = array(3, array_3_model_input, array_3_length, array_3_strings)
        string_5 = string(3, array_3_model_input, array_3_length, array_3_strings, 5, array_3_length)
        string_6 = string(3, array_3_model_input, array_3_length, array_3_strings, 6, array_3_length)

    string_1 = string(1, array_1_model_input, array_1_length, array_1_strings, 1, array_1_length)
    string_2 = string(1, array_1_model_input, array_1_length, array_1_strings, 2, array_1_length)
    string_3 = string(2, array_1_model_input, array_2_length, array_2_strings, 3, array_2_length)
    string_4 = string(2, array_1_model_input, array_2_length, array_2_strings, 4, array_2_length)
    system_1 = systemspecs(array_1, array_2, array_3, inverter_1, string_1, string_2, string_3, string_4, string_5,
                           string_6, application)
    # system information is printed below.
    #TODO create a popup window displaying this infromation with tKinter.
    print(system_1.array_Voc_minus_10())
    print(system_1.Res_Com_check())
    print(system_1.inverter_mppt_max_check_1())
    print(system_1.inverter_mppt_max_check_2())
    print(system_1.Circuit_breaker_current_limit(ac_breaker_current))
    print(system_1.Power_optimiser_limit())
    print(system_1.Min_panels_startup())
    print(system_1.Max_panels())
    print(system_1.CEC_Oversize_Check())
    print("")

    ##checks to see if arrays 3 and 4 created. could be tweaked
    if check == 1:
        array_3 = array(3, array_3_model_input, array_3_length, array_3_strings)
        array_4 = array(4, array_3_model_input, array_4_length, array_4_strings)
        array_dummy = array(5, array_1_model_input, 0, 0)
        string_5 = string(3, array_3_model_input, array_3_length, array_3_strings, 5, array_3_length)
        string_6 = string(3, array_3_model_input, array_3_length, array_3_strings, 6, array_3_length)
        string_7 = string(4, array_3_model_input, array_4_length, array_4_strings, 7, array_4_length)
        string_8 = string(4, array_3_model_input, array_4_length, array_4_strings, 8, array_4_length)
        string_dummy = string(5, array_1_model_input, 0, 0, 9, 0)
        system_2 = systemspecs(array_3, array_4, array_dummy, inverter_2, string_5, string_6, string_7, string_8,
                               string_dummy, string_dummy, application)
        # system information is printed below.
        # TODO create a popup window displaying this infromation with tKinter.
        print(system_2.array_Voc_minus_10())
        print(system_2.Res_Com_check())
        print(system_2.inverter_mppt_max_check_1())
        print(system_2.inverter_mppt_max_check_2())
        print(system_2.Circuit_breaker_current_limit(ac_breaker_current))
        print(system_2.Power_optimiser_limit())
        print(system_2.Min_panels_startup())
        print(system_2.Max_panels())
        print(system_2.CEC_Oversize_Check())
        print("")






## this gui pops up when tyou want to create a SLD. ideally, it would not require manual inputs.
## however, it is a bit of a relic from previous versions.
## TODO SLDGUI should really not have to require manual inputs. should be able to know the system maybe check to see if entries have 0??

## configuration based on earlier calculations. a bit messy to implement
def SLDGUI():
    global inverterno, battery, arrays, phase, current, reposit

    window2 = tk.Tk()
    window2.title("SLD make tool")
    window2.geometry('350x300')

    lbl8 = tk.Label(window2, text="inverterno")
    lbl8.grid(column=0, row=7)
    txt8 = ttk.Combobox(window2, width=10)
    txt8.set('1')
    txt8.grid(column=1, row=7)
    txt8['values'] = ['1', '2']

    lbl9 = tk.Label(window2, text="battery")
    lbl9.grid(column=0, row=8)
    txt9 = ttk.Combobox(window2, width=10)
    txt9.set('0')
    txt9.grid(column=1, row=8)
    txt9['values'] = ['0', '1']

    lbl10 = tk.Label(window2, text="arrays")
    lbl10.grid(column=0, row=9)
    txt10 = tk.Entry(window2, width=10)
    txt10.grid(column=1, row=9)

    lbl11 = tk.Label(window2, text="phase")
    lbl11.grid(column=0, row=10)
    txt11 = ttk.Combobox(window2, width=10)
    txt11['values'] = ['1', '3']
    txt11.set('1')
    txt11.grid(column=1, row=10)

    var = tk.StringVar(window2)
    var.set("AC")
    lbl12 = tk.Label(window2, text="current")
    lbl12.grid(column=0, row=11)
    txt12 = tk.OptionMenu(window2, var, 'AC', 'DC')
    txt12.grid(column=1, row=11)

    lbl13 = tk.Label(window2, text="reposit")
    lbl13.grid(column=0, row=12)
    txt13 = ttk.Combobox(window2, width=10)
    txt13.set('1')
    txt13.grid(column=1, row=12)
    txt13['values'] = ['0', '1']

    quit2 = tk.Button(window2, text='Create SLD', command=window2.quit)
    quit2.grid(column=4, row=8)

    window2.mainloop()

    #assigning to global variables things that have ben entered into the SLD gui window.
    inverterno = int(txt8.get())
    battery = int(txt9.get())
    arrays = int(txt10.get())
    phase = int(txt11.get())
    current = var.get()
    reposit = int(txt13.get())

    window2.destroy()

    ## This Program creates the sLD
    ##
    ## TODO run through array panel configurations, as well as reposit or not.
    ##
    ##


## creates a name and address for use in SLD and VRC. based on an input of customer ID
def name_address(customer_ID):
    """"""
    global name, address

    # establish connecttion to database
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()

    ##accessing databse to find customer details based on a unique customer ID
    cur.execute('SELECT Name FROM customer_details WHERE CustomerID =?', customer_ID)
    name = cur.fetchone()[0]
    cur.execute('SELECT Street FROM customer_details WHERE CustomerID =?', customer_ID)
    street = cur.fetchone()[0]
    cur.execute('SELECT Suburb FROM customer_details WHERE CustomerID =?', customer_ID)
    suburb = cur.fetchone()[0]
    cur.execute('SELECT State FROM customer_details WHERE CustomerID =?', customer_ID)
    state = cur.fetchone()[0]
    cur.execute('SELECT Postcode FROM customer_details WHERE CustomerID =?', customer_ID)
    postoode = cur.fetchone()[0]
    ## string concatenation to create title.
    address = street + ', ' + suburb + ' ' + state + ' ' + str(postoode)

    print(name, address)

    conn.close()


## my first program at solar4life. also by far the messiest. the code to create lines on the SLD is held
## together with magic and sticky tape.

""""""""""
check which layouts work

to make a new layout, best to copy paste the most similar layout under a new if statements, and change slightly
probably do this part on excel or google sheets.

Phase   Arrays  Batteries   Current Reposit     Inverters | Works?  Annotated?     
1       1       0           -       0           1         |  Y          -
1       1       0           -       1           1         |  Y          -
1       1       1           AC      1           1         |  Y          needs check
1       1       1           DC      1           1         |  Y          needs check
1       2       0           -       0           1         |  Y          -
1       2       0           -       1           1         |  Y          -                                  
1       2       1           AC      1           1         |  Y          needs check
1       2       1           DC      1           1         |  Y          needs check
1       3       0           -       0           1         |  N          not exist
1       3       0           -       1           1         |  N          not exist
1       3       1           AC      1           1         |  N          not exist
1       3       1           DC      1           1         |  N          not exist
1       3       0           -       0           2         |  N          not exist
1       3       0           -       1           2         |  N          not exist
1       3       1           AC      1           2         |  N          not exist
1       3       1           DC      1           2         |  N          not exist
1       4       0           -       0           1         |  N          not exist 
1       4       0           -       1           1         |  N          not exist 
1       4       1           AC      1           1         |  N          not exist 
1       4       1           DC      1           1         |  N          not exist 
1       4       0           -       0           2         |  N          not exist
1       4       0           -       1           2         |  N          not exist  
1       4       1           AC      1           2         |  N          not exist           
1       4       1           DC      1           2         |  N          not exist
3       1       0           -       0           1         |  Y          -          
3       1       0           -       1           1         |  Y          -          
3       1       1           AC      1           1         |  Y          needs check
3       1       1           DC      1           1         |  Y          needs check
3       2       0           -       0           1         |  Y          -          
3       2       0           -       1           1         |  Y          -          
3       2       1           AC      1           1         |  Y          needs check
3       2       1           DC      1           1         |  Y          needs check
3       3       0           -       0           1         |  N          not exist
3       3       0           -       1           1         |  N          not exist
3       3       1           AC      1           1         |  N          not exist
3       3       1           DC      1           1         |  N          not exist
3       3       0           -       0           2         |  N          not exist
3       3       0           -       1           2         |  N          not exist
3       3       1           AC      1           2         |  N          not exist
3       3       1           DC      1           2         |  N          not exist
3       4       0           -       0           1         |  N          not exist
3       4       0           -       1           1         |  N          not exist
3       4       1           AC      1           1         |  N          not exist
3       4       1           DC      1           1         |  N          not exist
3       4       0           -       0           2         |  N          lines aren't good
3       4       0           -       1           2         |  N          lines aren't good
3       4       1           AC      1           2         |  Y          needs check
3       4       1           DC      1           2         |  Y          needs check




"""""""""""

def create_SLD(fname, inverterno, battery, array, phase, current, reposit):

    # establish connecttion to database
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()


    ## where images of some shapes in the program used. cahgne if required.
    trianglepath = r"C:\Users\Solar4Life\Desktop\solar4life\sld generator files\sava assets\triangle.png"
    sinepath = r"C:\Users\Solar4Life\Desktop\solar4life\sld generator files\sava assets\sine.png"

    ## TODO might need to change how componenet attributes are assigned. like when there are 2 different panels
    #checks the database for values that will be printed on the SLD as strings.
    panelspec = ('%s' % array_1_model_input,)
    panelspec2 = ('%s' % array_1_model_input,)
    batteryl = ('%s' % battery_input,)
    inverter1 = ('%s' % inverter_1_input,)
    inverter2 = ('%s' % inverter_2_input,)
    meter1 = ('LG Meter',)
    meter2 = ('',)

    Inverter1ACIsolator = ('%s' % SS_Switch,)
    Inverter2ACIsolator = ('%s' % SS_Switch,)
    SolarSupplyMainSwitch = ('%s' % ac_breaker_current_limit,)
    BatteryACIsolator = ('1P 25A 6kA NHP mod6 AC Breaker',)
    BatteryDCIsolator = ('1P 25A 6kA NHP mod6 AC Breaker',)
    EPSACIsolator = ('3P 32A 6kA NHP mod6 AC Breaker',)

    filename = os.path.join(fname + ".pdf")
    c = canvas.Canvas(filename)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    ##Title
    c.drawCentredString(300, 820, 'Single Line Diagram for %s - %s' % (name, address))

    #function to draw arcs. it helped.
    def draw_arc(x, y):
        x += -7.5
        y += 7
        c.arc(x, y, x + 15, y - 15, extent=180)

    ## draws meter based on how many meters ther are an layout of wiring
    def draw_reposit():
        if reposit > 0:
            if phase == 1 and battery == 1:
                ##reposit
                c.setFont('Helvetica', 7)
                c.rect(250, 50, 50, 30)

                cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter1)
                model = cur.fetchone()[0]
                c.drawRightString(300, 40, 'Model Number: %s ' % model)
                cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter1)
                make = cur.fetchone()[0]
                c.drawRightString(300, 30, "Make: %s " % make)

                if reposit >= 2:
                    cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter2)
                    model = cur.fetchone()[0]
                    c.drawRightString(300, 20, 'Model Number: %s ' % model)
                    cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter2)
                    make = cur.fetchone()[0]
                    c.drawRightString(300, 10, "Make: %s " % make)

                c.drawString(255, 60, "Reposit")
                c.circle(200, 185, 7)
                c.line(200, 177, 200, 65)
                c.line(200, 65, 250, 65)
                c.line(300, 65, 340, 65)
                c.line(340, 65, 340, 93.5)
                c.rect(333.5, 93.5, 13, 13)
                c.drawCentredString(340, 122, 'Voltage')
                c.drawCentredString(340, 112, 'Reference')

            if phase == 1 and battery == 0:
                c.setFont('Helvetica', 7)
                c.rect(250, 50, 50, 30)
                c.drawString(255, 60, "Reposit")
                cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter1)
                model = cur.fetchone()[0]
                c.drawRightString(300, 40, 'Model Number: %s ' % model)
                cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter1)
                if reposit >= 2:
                    make = cur.fetchone()[0]
                    c.drawRightString(300, 30, "Make: %s " % make)
                    cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter2)
                    model = cur.fetchone()[0]
                    c.drawRightString(300, 20, 'Model Number: %s ' % model)
                    cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter2)
                    make = cur.fetchone()[0]
                    c.drawRightString(300, 10, "Make: %s " % make)

                c.circle(230, 185, 7)
                c.line(230, 177, 230, 65)
                c.line(230, 65, 250, 65)
                c.line(300, 65, 340, 65)
                c.line(340, 65, 340, 93.5)
                c.rect(333.5, 93.5, 13, 13)
                c.drawCentredString(340, 122, 'Voltage')
                c.drawCentredString(340, 112, 'Reference')

            if phase == 3:
                ##reposit
                c.circle(225, 195, 5)
                c.circle(205, 182.5, 5)
                c.circle(185, 170, 5)
                draw_arc(205, 170)
                draw_arc(225, 182.5)
                draw_arc(225, 170)

                c.setFont('Helvetica', 7)
                c.rect(300, 25, 50, 30)

                cur.execute('SELECT Model FROM Meterspecifications where Meter=?', meter1)
                model = cur.fetchone()[0]
                c.drawString(255, 17, 'Model Number: %s ' % model)
                cur.execute('SELECT Make FROM Meterspecifications where Meter=?', meter1)
                make = cur.fetchone()[0]
                c.drawString(255, 8, "Make: %s " % make)

                c.drawString(305, 30, "Reposit")
                c.rect(363.5, 113.5, 13, 13)
                c.rect(393.5, 128.5, 13, 13)
                c.rect(423.5, 143.5, 13, 13)
                draw_arc(370, 135)
                draw_arc(370, 150)
                draw_arc(400, 150)
                c.drawString(440, 122, 'Voltage')
                c.drawString(440, 112, 'Reference')

    ##switch function. draws based on x and y coordinates, and rotation
    def draw_switch(x, y, rot):
        if rot == 0:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x, y + 15, 2, stroke=1, fill=0)
            c.line(x, y + 2, x - 7, y + 15)

        if rot == 90:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x + 15, y, 2, stroke=1, fill=0)
            c.line(x + 2, y, x + 15, y - 7)

        if rot == 180:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x, y - 15, 2, stroke=1, fill=0)
            c.line(x, y - 2, x + 7, y - 15)

        if rot == 270:
            c.circle(x, y, 2, stroke=1, fill=0)
            c.circle(x + 15, y, 2, stroke=1, fill=0)
            c.line(x + 2, y, x + 15, y + 7)

    ##draw battery function. needs x and y coordinates
    def draw_battery(x, y, battery):

        c.line(x + 10, y - 10, x + 10, y)
        c.line(x + 10, y, x - 35, y)
        c.line(x - 35, y, x - 35, y + 35)
        c.line(x - 35, y + 35, x - 20, y + 35)
        c.line(x - 20, y + 25, x - 20, y + 45)
        c.line(x - 10, y + 15, x - 10, y + 55)
        c.line(x, y + 25, x, y + 45)
        c.line(x + 10, y + 15, x + 10, y + 55)
        c.line(x + 20, y + 25, x + 20, y + 45)
        c.line(x + 30, y + 15, x + 30, y + 55)
        c.line(x + 40, y + 25, x + 40, y + 45)
        c.line(x + 50, y + 15, x + 50, y + 55)
        c.line(x + 60, y + 25, x + 60, y + 45)
        c.line(x + 70, y + 15, x + 70, y + 55)
        c.line(x + 70, y + 35, x + 85, y + 35)
        c.line(x + 85, y + 35, x + 85, y)
        c.line(x + 85, y, x + 40, y)
        c.line(x + 40, y, x + 40, y - 10)
        x += 100
        y += 40
        c.setFont('Helvetica', 12)
        c.drawString(x - 120, y + 70, "1 x Battery")
        c.setFont('Helvetica', 8)

        ## TODO BMU label

        cur.execute('SELECT make FROM Batteryspecifications where Battery=?', battery)
        bmake = cur.fetchone()[0]
        c.drawString(x - 120, y + 55, "Make: %s" % bmake)

        cur.execute('SELECT model FROM Batteryspecifications where Battery=?', battery)
        bmodel = cur.fetchone()[0]
        c.drawString(x - 120, y + 40, "Model: %s" % bmodel)

        cur.execute('SELECT CapacityatDoDkWh FROM Batteryspecifications where Battery=?', battery)
        bcap = cur.fetchone()[0]
        c.drawString(x - 120, y + 25, "Capacity: %s kWh" % bcap)

    ## draw array and associated switches
    def draw_array(x, y, arrayno, arraymodules, panelspec, strings):

        c.rect(x, y, 180, 170)
        c.line(x + 35, y + 125, x + 35, y + 160)
        c.line(x + 45, y + 130, x + 45, y + 155)
        c.line(x + 35, y + 142.5, x + 5, y + 142.5)
        c.line(x + 45, y + 142.5, x + 75, y + 142.5)

        c.setFont('Helvetica', 12)
        c.drawString(x + 80, 630 + 145, 'Array %d' % arrayno)
        c.setFont('Helvetica', 8)


        cur.execute('SELECT PmaxW FROM Panelspecifications where Panel=?', panelspec)
        arraymodulerating = cur.fetchone()[0]
        c.drawString(x + 5, y + 65, '%d x %dW modules' % (arraymodules, arraymodulerating))

        cur.execute('SELECT Model FROM Panelspecifications where Panel=?', panelspec)
        arraymodelnumber = cur.fetchone()[0]
        c.drawCentredString(x + 75, y + 80, '%s' % arraymodelnumber)
        c.setFont('Helvetica', 7)
        cur.execute('SELECT Manufacturer FROM Panelspecifications where Panel=?', panelspec)
        arraymanufacturer = cur.fetchone()[0]
        c.drawString(x + 5, y + 97, '%s' % arraymanufacturer)
        c.setFont('Helvetica', 7)

        c.drawString(x + 5, y + 110, '%d/ String/s of:' % strings)

        draw_switch(x + 65, 630 - 50, 180)
        draw_switch(x + 95, 630 - 50, 180)
        draw_switch(x + 65, 630 - 100, 180)
        draw_switch(x + 95, 630 - 100, 180)
        c.setDash(array=[3], phase=13)
        c.line(x + 65, 630 - 107, x + 95, 630 - 107)
        c.line(x + 65, 630 - 57, x + 95, 630 - 57)
        c.setDash(array=[], phase=0)
        if arrayno == 1:
            x += 120
            c.drawString(x - 15, 630 - 50, 'Rooftop DC Isolator')
            c.drawString(x - 15, 630 - 65, '1200V 32A')
            c.drawString(x - 15, 630 - 100, 'Inverter DC Isolator')
            c.drawString(x - 15, 630 - 115, '1200V 32A')
            x += -120
            ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')
            c.drawString(x + 5, y + 20, 'Isc')
            c.drawString(x + 60, y + 20, '=  %.2fA' % system_1.array_Isc()[0])
            c.drawString(x + 5, y + 35, 'Voc')
            c.drawString(x + 60, y + 35, '=  %.2fV' % system_1.array_Voc()[0])
            c.drawString(x + 5, y + 50, 'Voc(-10C)')
            c.drawString(x + 60, y + 50, '=  %.2fV' % system_1.array_Voc_minus_10()[0])

        else:

            c.drawString(x - 5, 630 - 50, 'Rooftop DC Isolator')
            c.drawString(x - 5, 630 - 65, '1200V 32A')
            c.drawString(x - 5, 630 - 100, 'Inverter DC Isolator')
            c.drawString(x - 5, 630 - 115, '1200V 32A')

            ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')
            c.drawString(x + 5, y + 20, 'Isc')
            c.drawString(x + 60, y + 20, '=  %.2fA' % system_1.array_Isc()[1])
            c.drawString(x + 5, y + 35, 'Voc')
            c.drawString(x + 60, y + 35, '=  %.2fV' % system_1.array_Voc()[1])
            c.drawString(x + 5, y + 50, 'Voc(-10C)')
            c.drawString(x + 60, y + 50, '=  %.2fV' % system_1.array_Voc_minus_10()[1])
        c.circle(x + 65, 630, 2, stroke=1, fill=0)
        c.circle(x + 95, 630, 2, stroke=1, fill=0)
        c.setFont('Helvetica', 12)

    ## draw arrays and wires when there are 4 arrays required
    def draw_small_array(x, y, arrayno, system):

        if arrayno == 1 or arrayno == 3:
            c.setFont('Helvetica', 12)
            c.rect(x, y, 120, 140)
            c.line(x + 30, y + 105, x + 30, y + 135)
            c.line(x + 37, y + 110, x + 37, y + 130)
            c.line(x + 30, y + 120, x + 10, y + 120)
            c.line(x + 37, y + 120, x + 55, y + 120)
            c.drawString(x + 70, y + 115, 'Array %d' % arrayno)
            c.setFont('Helvetica', 7)
            ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')

            c.drawString(x + 5, y + 5, 'Isc')
            arrayisc = system.array_Isc()[0]
            c.drawString(x + 60, y + 5, '=  %.2fA' % arrayisc)

            c.drawString(x + 5, y + 20, 'Voc')
            arrayvoc = system.array_Voc()[0]
            c.drawString(x + 60, y + 20, '=  %.2fV' % arrayvoc)

            c.drawString(x + 5, y + 35, 'Voc(-10C)')
            arrayvocminus10 = system.array_Voc_minus_10()[0]
            c.drawString(x + 60, y + 35, '=  %.2fV' % arrayvocminus10)

            arraymodulerating = system.array1.wattage[0]
            arraymodules1 = system.string1.length
            c.drawString(x + 5, y + 50, '%d x %dW modules' % (arraymodules1, arraymodulerating))

            cur.execute('SELECT Model FROM Panelspecifications where Panel=?', panelspec)
            arraymodelnumber = cur.fetchone()[0]
            c.drawString(x + 35, y + 65, '%s' % arraymodelnumber)

            cur.execute('SELECT Manufacturer FROM Panelspecifications where Panel=?', panelspec)
            arraymanufacturer = cur.fetchone()[0]
            c.drawString(x + 5, y + 80, '%s' % arraymanufacturer)

            c.drawString(x + 5, y + 90, '%d/ String/s of:' % system.string1.strings)

            draw_switch(x + 35, y - 40, 180)
            draw_switch(x + 65, y - 40, 180)
            draw_switch(x + 35, y - 90, 180)
            draw_switch(x + 65, y - 90, 180)
            c.setDash(array=[3], phase=13)
            c.line(x + 35, y - 97, x + 65, y - 97)
            c.line(x + 35, y - 47, x + 65, y - 47)
            c.setDash(array=[], phase=0)
            c.drawString(x + 90, y - 40, 'Rooftop DC Isolator')
            c.drawString(x + 90, y - 55, '1200V 32A')
            c.drawString(x + 90, y - 90, 'Inverter DC Isolator')
            c.drawString(x + 90, y - 105, '1200V 32A')
            c.circle(x + 35, y, 2, stroke=1, fill=0)
            c.circle(x + 65, y, 2, stroke=1, fill=0)
            c.setFont('Helvetica', 12)

            c.line(x + 35, y - 2, x + 35, y - 38)
            c.line(x + 35, y - 57, x + 35, y - 88)
            c.line(x + 35, y - 107, x + 35, y - 170)
            c.line(x + 35, y - 170, x + 70, y - 170)
            c.line(x + 70, y - 170, x + 70, y - 185)

            c.line(x + 65, y - 2, x + 65, y - 38)
            c.line(x + 65, y - 57, x + 65, y - 88)
            c.line(x + 65, y - 107, x + 65, y - 157.5)
            c.line(x + 65, y - 157.5, x + 82.5, y - 157.5)
            c.line(x + 82.5, y - 157.5, x + 82.5, y - 185)
            arrayno += 1
        if arrayno == 2 or arrayno == 4:
            x += 130

            c.setFont('Helvetica', 12)
            c.circle(x + 35, y, 2, stroke=1, fill=0)
            c.circle(x + 65, y, 2, stroke=1, fill=0)
            c.rect(x, y, 120, 140)
            c.line(x + 30, y + 105, x + 30, y + 135)
            c.line(x + 37, y + 110, x + 37, y + 130)
            c.line(x + 30, y + 120, x + 10, y + 120)
            c.line(x + 37, y + 120, x + 55, y + 120)
            c.drawString(x + 70, y + 115, 'Array %d' % arrayno)
            c.setFont('Helvetica', 7)
            ##c.drawString(x + 5, y + 5, 'w/ Built-In Optimisers')

            c.drawString(x + 5, y + 5, 'Isc')
            arrayisc = system.array_Isc()[1]
            c.drawString(x + 60, y + 5, '=  %.2fA' % arrayisc)

            c.drawString(x + 5, y + 20, 'Voc')
            arrayvoc = system.array_Voc()[1]
            c.drawString(x + 60, y + 20, '=  %.2fV' % arrayvoc)

            c.drawString(x + 5, y + 35, 'Voc(-10C)')
            arrayvocminus10 = system.array_Voc_minus_10()[1]
            c.drawString(x + 60, y + 35, '=  %.2fV' % arrayvocminus10)

            arraymodulerating = system.array1.wattage[0]
            arraymodules1 = system.string3.length
            c.drawString(x + 5, y + 50, '%d x %dW modules' % (arraymodules1, arraymodulerating))

            cur.execute('SELECT Model FROM Panelspecifications where Panel=?', panelspec)
            arraymodelnumber = cur.fetchone()[0]
            c.drawString(x + 35, y + 65, '%s' % arraymodelnumber)

            cur.execute('SELECT Manufacturer FROM Panelspecifications where Panel=?', panelspec)
            arraymanufacturer = cur.fetchone()[0]
            c.drawString(x + 5, y + 80, '%s' % arraymanufacturer)

            c.drawString(x + 5, y + 90, '%d/ String/s of:' % system.string3.strings)

            draw_switch(x + 35, y - 40, 180)
            draw_switch(x + 65, y - 40, 180)
            draw_switch(x + 35, y - 90, 180)
            draw_switch(x + 65, y - 90, 180)
            c.setDash(array=[3], phase=13)
            c.line(x + 35, y - 97, x + 65, y - 97)
            c.line(x + 35, y - 47, x + 65, y - 47)
            c.setDash(array=[], phase=0)

            c.line(x + 35, y - 2, x + 35, y - 38)
            c.line(x + 35, y - 57, x + 35, y - 88)
            c.line(x + 35, y - 107, x + 35, y - 120)
            c.line(x + 35, y - 120, x - 35, y - 120)
            c.line(x - 35, y - 120, x - 35, y - 185)

            c.line(x + 65, y - 2, x + 65, y - 38)
            c.line(x + 65, y - 57, x + 65, y - 88)
            c.line(x + 65, y - 107, x + 65, y - 132.5)
            c.line(x + 65, y - 132.5, x - 22.5, y - 132.5)
            c.line(x - 22.5, y - 132.5, x - 22.5, y - 185)

    ##draw inverter function
    def draw_inverter(x, y, inverter, inverterno, batt):

        c.rect(x, y, 75, 75)
        c.line(x, y, x + 75, y + 75)
        c.drawImage(sinepath, x + 45, y + 5, width=25, height=25)
        c.line(x + 5, y + 55, x + 35, y + 55)
        c.line(x + 5, y + 45, x + 15, y + 45)
        c.line(x + 25, y + 45, x + 35, y + 45)
        ##label
        x += 200
        y += -15
        if batt == 'N':
            c.setFont('Helvetica', 14)
            c.drawString(x - 120, y + 80, "1 x Inverter")
            c.setFont('Helvetica', 7)

            cur.execute('SELECT Make FROM Inverterspecifications where Inverter =?', inverter)
            imake = cur.fetchone()[0]
            c.drawString(x - 120, y + 65, "Make: %s" % imake)

            cur.execute('SELECT Series FROM Inverterspecifications where Inverter =?', inverter)
            iseries = cur.fetchone()[0]
            c.drawString(x - 120, y + 50, "Series: %s" % iseries)

            c.drawString(x - 120, y + 35, "Model:")
            cur.execute('SELECT Model FROM Inverterspecifications where Inverter =?', inverter)
            imodel = cur.fetchone()[0]
            c.setFont('Helvetica', 6)
            c.drawString(x - 120, y + 23, "%s" % imodel)

            c.setFont('Times-Italic', 6)
            if inverterno == 1 and current == 'DC' and battery > 0:
                c.drawString(x - 45, y + 80, "When network is down inverter")
                c.drawString(x - 45, y + 72, "isolates from the grid and")
                c.drawString(x - 45, y + 64, "can only power essential loads")
            if inverterno == 1 and current == 'AC' and battery > 0:
                c.drawString(x - 45, y + 80, "*Inverter isolates in ")
                c.drawString(x - 45, y + 72, "the event of blackout")

    ## draw most of the wriing and components that are common to all systems
    def basic_wiring(x, y):

        ##earth-CN
        c.line(530, 70, 570, 70)
        c.line(550, 70, 550, 210)
        c.line(535, 65, 565, 65)
        c.line(540, 60, 560, 60)
        c.line(550, 210, 480, 210)
        c.circle(480, 210, 2, stroke=1, fill=1)

        ## customer neutral link
        c.setFont('Helvetica', 8)
        c.drawString(420, 230, 'Customer Neutral')
        c.circle(430, 210, 2, stroke=1, fill=1)
        c.rect(430, 200, 50, 20)

        ##neutrallink/servicefuse
        c.rect(85, 40, 20, 40)
        c.rect(115, 40, 20, 40)
        c.setFont('Helvetica', 7)
        c.drawRightString(75, 60, 'Neutral Link')
        c.drawString(140, 60, 'Service')
        c.drawString(140, 45, 'Fuse')

        ##NDS
        c.setFillColor(black)
        c.setFont('Helvetica', 8)
        c.drawString(45, 15, 'Normal Distribution Supply')

        ## always there wiring
        # circle to NL / SF
        c.line(95, 80, 95, 110)
        c.line(125, 80, 125, 110)
        # NL / SF to nds
        c.line(95, 40, 95, 30)
        c.line(125, 40, 125, 30)
        c.circle(95, 30, 2)
        c.circle(125, 30, 2)

        ##main circle
        c.circle(110, 130, 25, stroke=1, fill=0)
        c.setFont('Helvetica', 18)
        c.drawString(103, 122, "M")

        ##customers final subcircuits
        c.line(370, 100, 370, 50)
        c.circle(370, 100, 2, stroke=1, fill=1)
        c.drawImage(trianglepath, 367, 44, width=7, height=7)
        c.line(400, 100, 400, 50)
        c.circle(400, 100, 2, stroke=1, fill=1)
        c.drawImage(trianglepath, 397, 44, width=7, height=7)
        c.line(430, 100, 430, 50)
        c.circle(430, 100, 2, stroke=1, fill=1)
        c.drawImage(trianglepath, 427, 44, width=7, height=7)
        c.setFillColor(black)
        c.setFont('Helvetica', 8)
        c.drawCentredString(400, 25, "Customer's Final")
        c.drawCentredString(400, 15, 'Subcircuits')
        c.setFont('Helvetica', 12)

        draw_reposit()

    ## main meat of the wiring. depends on variables taken from main design tool.
    def complex_wiring(phase, array, battery, inverterno, current):

        if phase == 1:
            if array == 1:
                draw_array(25, 630, 1, array_1_length, panelspec, array_1_strings)
                if battery == 0:
                    ##wiring
                    x = 25
                    c.circle(x + 65, 630 - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)
                    c.line(x + 65, 630 - 117, x + 65, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 77.5, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 95, 630 - 129.5)
                    c.line(x + 95, 630 - 129.5, x + 95, 630 - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(250, 310, 0)
                    draw_switch(250, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(260, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(260, 305, "%s" % i1iso)

                    c.drawString(260, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(260, 245, "%s" % SSiso)

                    draw_arc(250, 210)
                    draw_switch(180, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(187.5, 170, 'Main Switch')
                    c.circle(250, 185, 2, stroke=1, fill=1)
                    c.circle(225, 210, 2, stroke=1, fill=1)

                    c.line(250, 185, 250, 248)
                    c.line(250, 266, 250, 308)
                    c.line(250, 327, 250, 360)
                    c.line(250, 360, 130, 360)
                    c.line(130, 360, 130, 375)

                    c.line(225, 210, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 242.5, 210)
                    c.line(257.5, 210, 430, 210)

                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 177.5, 185)
                    c.line(197.5, 185, 300, 185)
                    c.line(300, 185, 300, 100)
                    c.line(300, 100, 430, 100)

                if battery == 1 and current == 'DC':
                    x = 25
                    c.circle(x + 65, 630 - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)
                    c.line(x + 65, 630 - 117, x + 65, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 77.5, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 95, 630 - 129.5)
                    c.line(x + 95, 630 - 129.5, x + 95, 630 - 117)
                    draw_battery(400, 550, batteryl)

                    c.line(410, 630 - 90, 410, 630 - 145)
                    c.line(410, 630 - 145, x + 280, 630 - 145)
                    c.line(x + 261, 630 - 145, x + 95, 630 - 145)
                    c.line(x + 95, 630 - 145, x + 95, 630 - 178)
                    draw_switch(x + 263, 630 - 145, 270)

                    c.circle(x + 95, 630 - 180, 2, stroke=1, fill=1)

                    draw_inverter(75, 375, inverter1, inverterno, 'N')
                    c.circle(x + 105, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 415, 630 - 90, x + 415, 630 - 165)
                    c.line(x + 415, 630 - 165, x + 280, 630 - 165)
                    c.line(x + 261, 630 - 165, x + 105, 630 - 165)
                    c.line(x + 105, 630 - 165, x + 105, 630 - 180)
                    draw_switch(x + 263, 630 - 165, 270)
                    c.setFont('Helvetica', 7)
                    c.drawString(x + 240, 630 - 110, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 240, 630 - 125, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 270, 630 - 145, x + 270, 630 - 165)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM
                    draw_switch(225, 310, 0)
                    draw_switch(225, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 305, '%s' % i1iso)

                    c.drawString(235, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 245, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    ##inv switch line
                    c.line(225, 185, 225, 248)
                    c.line(225, 266, 225, 308)
                    c.line(225, 327, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    ##main line
                    c.line(200, 210, 200, 320)
                    c.line(200, 320, 90, 320)
                    c.line(90, 320, 90, 375)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##L1 P1 Line
                    c.line(130, 375, 130, 360)
                    c.line(130, 360, 380, 360)
                    c.line(380, 360, 380, 327.5)
                    draw_switch(380, 310, 0)

                    c.setFont('Helvetica', 6)
                    c.drawString(390, 320, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(380, 307.5, 380, 278)
                    draw_switch(380, 260, 0)
                    c.line(380, 258, 380, 190)
                    c.line(380, 190, 450, 190)
                    c.line(450, 190, 450, 100)
                    c.line(450, 100, 500, 100)

                    c.line(470, 100, 470, 50)
                    c.circle(470, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 467, 44, width=7, height=7)
                    c.line(500, 100, 500, 50)
                    c.circle(500, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 497, 44, width=7, height=7)
                    c.drawCentredString(470, 110, 'L1')
                    c.drawCentredString(500, 110, 'L1')

                if battery == 1 and current == 'AC':
                    x = 25
                    c.circle(x + 65, 630 - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)
                    c.line(x + 65, 630 - 117, x + 65, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 77.5, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 95, 630 - 129.5)
                    c.line(x + 95, 630 - 129.5, x + 95, 630 - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')

                    ##BOTTOM
                    draw_switch(225, 310, 0)
                    draw_switch(225, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 305, '%s' % i1iso)

                    c.drawString(235, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 245, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    ##inv switch line
                    c.line(225, 185, 225, 248)
                    c.line(225, 266, 225, 308)
                    c.line(225, 327, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    ##main line
                    c.line(200, 210, 200, 320)
                    c.line(200, 320, 90, 320)
                    c.line(90, 320, 90, 375)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##reposit

                    ##battery inverter wiring
                    c.circle(275, 185, 2, stroke=1, fill=1)
                    c.line(275, 185, 380, 185)
                    c.line(380, 185, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)

                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)

                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)

            if array == 2:
                if battery == 0:
                    draw_array(20, 630, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(320, 630, 2, array_2_length, panelspec, array_2_strings)

                    # inverter circles
                    x = 20
                    y = 630
                    c.circle(x + 65, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 180, 2, stroke=1, fill=1)

                    ##jagged wiring
                    c.line(x + 77.5, y - 178, x + 77.5, y - 140)
                    c.line(x + 77.5, y - 140, x + 95, y - 140)
                    c.line(x + 95, y - 140, x + 95, y - 117)

                    c.line(x + 90, y - 178, x + 90, y - 152.5)
                    c.line(x + 90, y - 152.5, x + 365, y - 152.5)
                    c.line(x + 365, y - 152.5, x + 365, y - 117)

                    c.line(x + 102.5, y - 178, x + 102.5, y - 165)
                    c.line(x + 102.5, y - 165, x + 395, y - 165)
                    c.line(x + 395, y - 165, x + 395, y - 117)

                    c.circle(x + 65, y, 2, stroke=1, fill=0)
                    c.circle(x + 95, y, 2, stroke=1, fill=0)
                    c.line(x + 65, y - 2, x + 65, y - 48)
                    c.line(x + 95, y - 2, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 65, y - 117, x + 65, y - 178)

                    ##wiring
                    c.line(x + 65, y, x + 65, y - 48)
                    c.line(x + 95, y, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 365, y - 98, x + 365, y - 67)
                    c.line(x + 395, y - 98, x + 395, y - 67)

                    c.line(x + 365, y - 48, x + 365, y - 2)
                    c.line(x + 395, y - 48, x + 395, y - 2)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(250, 310, 0)
                    draw_switch(250, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(260, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(260, 305, '%s' % i1iso)

                    c.drawString(260, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(260, 245, '%s' % SSiso)

                    draw_arc(250, 210)
                    draw_switch(180, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(187.5, 170, 'Main Switch')
                    c.circle(250, 185, 2, stroke=1, fill=1)
                    c.circle(225, 210, 2, stroke=1, fill=1)

                    c.line(250, 185, 250, 248)
                    c.line(250, 266, 250, 308)
                    c.line(250, 327, 250, 360)
                    c.line(250, 360, 130, 360)
                    c.line(130, 360, 130, 375)

                    c.line(225, 210, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 375)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 242.5, 210)
                    c.line(257.5, 210, 430, 210)

                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 177.5, 185)
                    c.line(197.5, 185, 300, 185)
                    c.line(300, 185, 300, 100)
                    c.line(300, 100, 430, 100)

                if battery == 1 and current == 'DC':
                    x = 20
                    y = 630
                    draw_array(x, 630, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, 630, 2, array_2_length, panelspec, array_2_strings)
                    draw_battery(x + 430, 550, batteryl)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 115, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 127.5, y - 205, 2, stroke=1, fill=1)

                    c.line(490, 630 - 90, 490, 450)
                    c.line(490, 450, x + 367, 450)

                    c.line(x + 440, 630 - 90, x + 440, 630 - 165)
                    c.line(x + 440, 630 - 165, x + 367, 630 - 165)
                    c.line(x + 348, 630 - 165, x + 115, 630 - 165)
                    c.line(x + 115, 630 - 165, x + 115, 427)

                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)

                    c.line(x + 65, 630 - 117, x + 65, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 77.5, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 95, 630 - 125)
                    c.line(x + 95, 630 - 125, x + 95, 630 - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    draw_switch(x + 350, y - 165, 270)
                    draw_switch(x + 350, y - 180, 270)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.setFont('Helvetica', 7)
                    c.drawString(x + 330, 630 - 125, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 330, 630 - 140, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 357, 630 - 165, x + 357, 630 - 180)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM

                    ##inv switch line
                    draw_switch(225, 280, 0)
                    draw_switch(225, 240, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 275, '%s' % i1iso)

                    c.drawString(235, 250, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 235, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    c.line(225, 185, 225, 238)
                    c.line(225, 256, 225, 278)
                    c.line(225, 297, 225, 290)
                    c.line(225, 290, 110, 290)
                    c.line(110, 290, 110, 350)

                    ##main line
                    c.line(200, 210, 200, 280)
                    c.line(200, 280, 90, 280)
                    c.line(90, 280, 90, 350)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##L1 P1 Line
                    c.line(130, 350, 130, 335)
                    c.line(130, 335, 380, 335)
                    c.line(380, 335, 380, 313)
                    draw_switch(380, 295, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(390, 305, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 290, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(380, 292, 380, 262)
                    draw_switch(380, 245, 0)
                    c.line(380, 243, 380, 160)
                    c.line(380, 160, 450, 160)
                    c.line(450, 160, 450, 100)
                    c.line(450, 100, 500, 100)

                    c.line(470, 100, 470, 50)
                    c.circle(470, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 467, 44, width=7, height=7)
                    c.line(500, 100, 500, 50)
                    c.circle(500, 100, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 497, 44, width=7, height=7)
                    c.drawCentredString(470, 110, 'L1')
                    c.drawCentredString(500, 110, 'L1')

                    ##reposit

                if battery == 1 and current == 'AC':
                    x = 20
                    y = 630
                    draw_array(x, 630, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, 630, 2, array_2_length, panelspec, array_2_strings)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')
                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')

                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)

                    c.line(x + 65, 630 - 117, x + 65, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 77.5, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 95, 630 - 125)
                    c.line(x + 95, 630 - 125, x + 95, 630 - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    ##BOTTOM
                    draw_switch(225, 310, 0)
                    draw_switch(225, 250, 0)
                    c.setFont('Helvetica', 7)
                    c.drawString(235, 320, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(235, 305, '%s' % i1iso)

                    c.drawString(235, 260, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(235, 245, '%s' % SSiso)

                    draw_arc(225, 210)
                    draw_switch(155, 185, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(162.5, 170, 'Main Switch')
                    c.circle(225, 185, 2, stroke=1, fill=1)
                    c.circle(200, 210, 2, stroke=1, fill=1)

                    ##inv switch line
                    c.line(225, 185, 225, 248)
                    c.line(225, 266, 225, 308)
                    c.line(225, 327, 225, 340)
                    c.line(225, 340, 110, 340)
                    c.line(110, 340, 110, 350)

                    ##main line
                    c.line(200, 210, 200, 320)
                    c.line(200, 320, 90, 320)
                    c.line(90, 320, 90, 350)

                    ##out of m into CN
                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 217.5, 210)
                    c.line(232.5, 210, 372.5, 210)
                    draw_arc(380, 210)
                    c.line(387.5, 210, 430, 210)

                    ##into CFS
                    c.line(125, 150, 125, 185)
                    c.line(125, 185, 152.5, 185)
                    c.line(172.5, 185, 275, 185)
                    c.line(275, 185, 275, 100)
                    c.line(275, 100, 430, 100)

                    ##battery inverter wiring
                    c.circle(275, 185, 2, stroke=1, fill=1)
                    c.line(275, 185, 380, 185)
                    c.line(380, 185, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)

                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)

                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)

            if array == 3:
                pass
            if array == 4:
                pass

        if phase == 3:
            if array == 1:
                draw_array(25, 630, 1, array_1_length, panelspec, array_1_strings)
                if battery == 0:
                    ##top
                    x = 25
                    c.circle(x + 65, 630 - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)
                    c.line(x + 65, 630 - 117, x + 65, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 77.5, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 95, 630 - 129.5)
                    c.line(x + 95, 630 - 129.5, x + 95, 630 - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)
                    # dc inv arcs
                    # draw_arc(325, 210)
                    # draw_arc(325, 195)
                    # draw_arc(325, 182.5)
                    # draw_arc(325, 170)
                    # c.line(312.5, 210, 317.5, 210)
                    # c.line(312.5, 195, 317.5, 195)
                    # c.line(312.5, 182.5, 317.5, 182.5)
                    # c.line(332.5, 170, 370, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'DC':
                    x = 25
                    c.circle(x + 65, 630 - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)
                    c.line(x + 65, 630 - 117, x + 65, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 77.5, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 95, 630 - 129.5)
                    c.line(x + 95, 630 - 129.5, x + 95, 630 - 117)
                    draw_battery(400, 550, batteryl)

                    c.line(410, 630 - 90, 410, 630 - 145)
                    c.line(410, 630 - 145, x + 280, 630 - 145)
                    c.line(x + 261, 630 - 145, x + 95, 630 - 145)
                    c.line(x + 95, 630 - 145, x + 95, 630 - 178)
                    draw_switch(x + 263, 630 - 145, 270)

                    c.circle(x + 95, 630 - 180, 2, stroke=1, fill=1)

                    draw_inverter(75, 375, inverter1, inverterno, 'N')
                    c.circle(x + 105, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 415, 630 - 90, x + 415, 630 - 165)
                    c.line(x + 415, 630 - 165, x + 280, 630 - 165)
                    c.line(x + 261, 630 - 165, x + 105, 630 - 165)
                    c.line(x + 105, 630 - 165, x + 105, 630 - 180)
                    draw_switch(x + 263, 630 - 165, 270)
                    c.setFont('Helvetica', 7)
                    c.drawString(x + 240, 630 - 110, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 240, 630 - 125, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 270, 630 - 145, x + 270, 630 - 165)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)

                    draw_arc(325, 210)
                    draw_arc(325, 195)
                    draw_arc(325, 182.5)
                    draw_arc(325, 170)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 170, 370, 170)

                    ##L1 P1 Line
                    c.line(130, 375, 130, 360)
                    c.line(130, 360, 325, 360)
                    c.line(325, 360, 325, 327.5)
                    draw_switch(325, 310, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(335, 305, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(335, 290, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(325, 307.5, 325, 278)
                    draw_switch(325, 260, 0)
                    c.line(325, 258, 325, 125)
                    c.line(325, 125, 250, 125)

                    c.line(250, 125, 250, 75)
                    c.circle(250, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 247, 70, width=7, height=7)
                    c.line(280, 125, 280, 75)
                    c.circle(280, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 277, 70, width=7, height=7)
                    c.drawCentredString(250, 135, 'L1')
                    c.drawCentredString(280, 135, 'P1')

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(332.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(332.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 317.5, 170)
                    c.line(332.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'AC':
                    x = 25
                    c.circle(x + 65, 630 - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, 630 - 180, 2, stroke=1, fill=1)
                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)
                    c.line(x + 65, 630 - 117, x + 65, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 77.5, 630 - 178)
                    c.line(x + 77.5, 630 - 129.5, x + 95, 630 - 129.5)
                    c.line(x + 95, 630 - 129.5, x + 95, 630 - 117)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)
                    # dc inv arcs
                    # draw_arc(325, 210)
                    # draw_arc(325, 195)
                    # draw_arc(325, 182.5)
                    # draw_arc(325, 170)
                    # c.line(312.5, 210, 317.5, 210)
                    # c.line(312.5, 195, 317.5, 195)
                    # c.line(312.5, 182.5, 317.5, 182.5)
                    # c.line(332.5, 170, 370, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)
                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)
                    draw_arc(380, 210)

            if array == 2:
                if battery == 0:
                    # top
                    draw_array(20, 630, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(320, 630, 2, array_2_length, panelspec, array_2_strings)
                    # inverter circles
                    x = 20
                    y = 630
                    c.circle(x + 65, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 180, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 180, 2, stroke=1, fill=1)

                    ##jagged wiring
                    c.line(x + 77.5, y - 178, x + 77.5, y - 140)
                    c.line(x + 77.5, y - 140, x + 95, y - 140)
                    c.line(x + 95, y - 140, x + 95, y - 117)

                    c.line(x + 90, y - 178, x + 90, y - 152.5)
                    c.line(x + 90, y - 152.5, x + 365, y - 152.5)
                    c.line(x + 365, y - 152.5, x + 365, y - 117)

                    c.line(x + 102.5, y - 178, x + 102.5, y - 165)
                    c.line(x + 102.5, y - 165, x + 395, y - 165)
                    c.line(x + 395, y - 165, x + 395, y - 117)

                    c.circle(x + 65, y, 2, stroke=1, fill=0)
                    c.circle(x + 95, y, 2, stroke=1, fill=0)
                    c.line(x + 65, y - 2, x + 65, y - 48)
                    c.line(x + 95, y - 2, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 65, y - 117, x + 65, y - 178)

                    ##wiring
                    c.line(x + 65, y, x + 65, y - 48)
                    c.line(x + 95, y, x + 95, y - 48)
                    c.line(x + 65, y - 67, x + 65, y - 98)
                    c.line(x + 95, y - 67, x + 95, y - 98)
                    c.line(x + 365, y - 98, x + 365, y - 67)
                    c.line(x + 395, y - 98, x + 395, y - 67)

                    c.line(x + 365, y - 48, x + 365, y - 2)
                    c.line(x + 395, y - 48, x + 395, y - 2)
                    draw_inverter(75, 375, inverter1, inverterno, 'N')

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 375)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 375)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 375)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 375)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)
                    # dc inv arcs
                    # draw_arc(325, 210)
                    # draw_arc(325, 195)
                    # draw_arc(325, 182.5)
                    # draw_arc(325, 170)
                    # c.line(312.5, 210, 317.5, 210)
                    # c.line(312.5, 195, 317.5, 195)
                    # c.line(312.5, 182.5, 317.5, 182.5)
                    # c.line(332.5, 170, 370, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit
                    if reposit == 1:
                        # ball to repo
                        c.line(185, 167.5, 185, 30)
                        c.line(205, 177.5, 205, 40)
                        c.line(225, 187.5, 225, 50)
                        c.line(185, 30, 300, 30)
                        c.line(205, 40, 300, 40)
                        c.line(225, 50, 300, 50)

                        # repo to VR
                        c.line(335, 55, 335, 150)
                        c.line(335, 150, 363.5, 150)
                        c.line(378.5, 150, 392.5, 150)
                        c.line(407.5, 150, 423.5, 150)

                        c.line(340, 55, 340, 135)
                        c.line(340, 135, 363.5, 135)
                        c.line(378.5, 135, 393.5, 135)

                        c.line(345, 55, 345, 120)
                        c.line(345, 120, 363.5, 120)
                    else:
                        c.line(190, 170, 260, 170)
                        c.line(210, 182.5, 260, 182.5)

                if battery == 1 and current == 'DC':
                    x = 20
                    y = 630
                    draw_array(x, 630, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, 630, 2, array_2_length, panelspec, array_2_strings)
                    draw_battery(x + 430, 550, batteryl)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 115, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 127.5, y - 205, 2, stroke=1, fill=1)

                    c.line(490, 630 - 90, 490, 450)
                    c.line(490, 450, x + 367, 450)

                    c.line(x + 440, 630 - 90, x + 440, 630 - 165)
                    c.line(x + 440, 630 - 165, x + 367, 630 - 165)
                    c.line(x + 348, 630 - 165, x + 115, 630 - 165)
                    c.line(x + 115, 630 - 165, x + 115, 427)

                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)

                    c.line(x + 65, 630 - 117, x + 65, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 77.5, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 95, 630 - 125)
                    c.line(x + 95, 630 - 125, x + 95, 630 - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    draw_switch(x + 350, y - 165, 270)
                    draw_switch(x + 350, y - 180, 270)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.line(x + 127.5, 450, x + 127.5, 427)
                    c.line(x + 127.5, 450, x + 348, 450)

                    c.setFont('Helvetica', 7)
                    c.drawString(x + 330, 630 - 125, 'Battery DC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryDCIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(x + 330, 630 - 140, '1200V 32A')
                    c.setFont('Helvetica', 12)
                    c.setDash(array=[3], phase=13)
                    c.line(x + 357, 630 - 165, x + 357, 630 - 180)
                    c.setDash(array=[], phase=0)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 290)
                    c.line(245, 290, 85, 290)
                    c.line(85, 290, 85, 350)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 275, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 260, '%s' % i1iso)

                    c.drawRightString(230, 240, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 225, '%s' % SSiso)
                    draw_switch(265, 275, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 273)
                    c.line(265, 292, 265, 310)
                    c.line(265, 310, 100, 310)
                    c.line(100, 310, 100, 350)

                    draw_switch(285, 275, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 273)
                    c.line(285, 292, 285, 320)
                    c.line(285, 320, 110, 320)
                    c.line(110, 320, 110, 350)

                    draw_switch(305, 275, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 273)
                    c.line(305, 292, 305, 330)
                    c.line(305, 330, 120, 330)
                    c.line(120, 330, 120, 350)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 282.5, 305, 282.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)

                    draw_arc(325, 210)
                    draw_arc(325, 195)
                    draw_arc(325, 182.5)
                    draw_arc(325, 170)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 170, 370, 170)

                    ##L1 P1 Line
                    c.line(130, 350, 130, 340)
                    c.line(130, 340, 325, 340)
                    c.line(325, 340, 325, 312.5)
                    draw_switch(325, 295, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(335, 280, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(335, 265, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(325, 292.5, 325, 263)
                    draw_switch(325, 245, 0)
                    c.line(325, 243, 325, 125)
                    c.line(325, 125, 250, 125)

                    c.line(250, 125, 250, 75)
                    c.circle(250, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 247, 70, width=7, height=7)
                    c.line(280, 125, 280, 75)
                    c.circle(280, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 277, 70, width=7, height=7)
                    c.drawCentredString(250, 135, 'L1')
                    c.drawCentredString(280, 135, 'P1')

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 317.5, 210)
                    c.line(332.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 317.5, 195)
                    c.line(332.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 317.5, 170)
                    c.line(332.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                if battery == 1 and current == 'AC':
                    x = 20
                    y = 630
                    draw_array(x, 630, 1, array_1_length, panelspec, array_1_strings)
                    draw_array(x + 200, 630, 2, array_2_length, panelspec, array_2_strings)
                    draw_inverter(x + 60, 350, inverter1, inverterno, 'N')

                    draw_battery(430, 540, batteryl)
                    draw_inverter(420, 455, inverter2, inverterno, 'Y')
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    c.line(x + 65, 630 - 2, x + 65, 630 - 48)
                    c.line(x + 95, 630 - 2, x + 95, 630 - 48)
                    c.line(x + 65, 630 - 67, x + 65, 630 - 98)
                    c.line(x + 95, 630 - 67, x + 95, 630 - 98)

                    c.line(x + 65, 630 - 117, x + 65, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 77.5, 630 - 205)
                    c.line(x + 77.5, 630 - 125, x + 95, 630 - 125)
                    c.line(x + 95, 630 - 125, x + 95, 630 - 117)

                    c.line(x + 102.5, y - 205, x + 102.5, y - 150)
                    c.line(x + 102.5, y - 150, x + 295, y - 150)
                    c.line(x + 295, y - 150, x + 295, y - 117)

                    c.line(x + 265, y - 2, x + 265, y - 48)
                    c.line(x + 295, y - 2, x + 295, y - 48)
                    c.line(x + 265, y - 67, x + 265, y - 98)
                    c.line(x + 295, y - 67, x + 295, y - 98)
                    c.line(x + 265, y - 117, x + 265, y - 137.5)

                    c.line(x + 90, y - 205, x + 90, y - 137.5)
                    c.line(x + 90, y - 137.5, x + 265, y - 137.5)
                    c.line(x + 265, y - 137.5, x + 265, y - 117)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 310)
                    c.line(245, 310, 85, 310)
                    c.line(85, 310, 85, 350)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawRightString(230, 290, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawRightString(230, 275, '%s' % i1iso)

                    c.drawRightString(230, 245, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawRightString(230, 230, '%s' % SSiso)
                    draw_switch(265, 290, 0)
                    draw_switch(265, 230, 0)
                    c.line(265, 195, 265, 228)
                    c.line(265, 246, 265, 288)
                    c.line(265, 307, 265, 325)
                    c.line(265, 325, 100, 325)
                    c.line(100, 325, 100, 350)

                    draw_switch(285, 290, 0)
                    draw_switch(285, 230, 0)
                    c.line(285, 182.5, 285, 228)
                    c.line(285, 246, 285, 288)
                    c.line(285, 307, 285, 335)
                    c.line(285, 335, 110, 335)
                    c.line(110, 335, 110, 350)

                    draw_switch(305, 290, 0)
                    draw_switch(305, 230, 0)
                    c.line(305, 170, 305, 228)
                    c.line(305, 246, 305, 288)
                    c.line(305, 307, 305, 345)
                    c.line(305, 345, 120, 345)
                    c.line(120, 345, 120, 350)

                    c.setDash(array=[3], phase=13)
                    c.line(265, 297.5, 305, 297.5)
                    c.line(265, 237.5, 305, 237.5)
                    c.setDash(array=[], phase=0)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(285, 210)
                    draw_arc(285, 195)
                    c.circle(285, 182.5, 2, stroke=1, fill=1)
                    draw_arc(305, 210)
                    draw_arc(305, 195)
                    draw_arc(305, 182.5)
                    c.circle(305, 170, 2, stroke=1, fill=1)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 277.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 277.5, 195)
                    c.line(292.5, 195, 297.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 297.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 307.5)
                    c.line(380, 326.5, 380, 380)
                    c.line(380, 380, 470, 380)
                    c.line(470, 380, 470, 455)
                    draw_switch(380, 310, 0)
                    c.drawString(390, 320, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(390, 305, '%s' % i1iso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 400)
                    c.line(355, 400, 450, 400)
                    c.line(450, 400, 450, 455)
                    draw_arc(380, 210)

            if array == 3:
                if battery == 0:
                    pass
                if battery == 1 and current == 'DC':
                    pass
                if battery == 1 and current == 'AC':
                    pass

            if array == 4:
                draw_small_array(10, 660, 1, system_1)
                draw_small_array(335, 660, 3, system_2)
                draw_inverter(75, 400, inverter1, inverterno, 'N')
                draw_inverter(400, 400, inverter2, inverterno, 'N')
                if battery == 1 and current == 'DC':
                    draw_battery(270, 520, batteryl)

                    ##topdots
                    x = 15
                    y = 680
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 115, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 127.5, y - 205, 2, stroke=1, fill=1)

                    ##top battery to inverter
                    c.line(x + 115, y - 205, x + 115, y - 175)
                    c.line(x + 115, y - 175, x + 208, y - 175)
                    draw_switch(x + 210, y - 175, 270)
                    c.line(x + 227, y - 175, x + 265, y - 175)
                    c.line(x + 265, y - 175, x + 265, y - 170)

                    c.line(x + 127.5, y - 205, x + 127.5, y - 190)
                    c.line(x + 127.5, y - 190, x + 208, y - 190)
                    draw_switch(x + 210, y - 190, 270)
                    c.line(x + 227, y - 190, x + 295, y - 190)
                    c.line(x + 295, y - 190, x + 295, y - 170)

                    c.setDash(array=[3], phase=13)
                    c.line(x + 219, y - 190, x + 219, y - 170)
                    c.setDash(array=[], phase=0)
                    c.setFont('Helvetica', 7)
                    c.drawString(x + 227, y - 205, 'Battery DC Isolator')

                    x += 325
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 230)
                    c.line(245, 230, 100, 230)
                    c.line(100, 230, 100, 400)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawString(135, 340, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(135, 325, '%s' % i1iso)

                    c.drawString(135, 295, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(135, 280, '%s' % SSiso)
                    draw_switch(125, 327, 0)
                    draw_switch(125, 282, 0)
                    c.line(265, 195, 265, 245)
                    c.line(265, 245, 125, 245)
                    c.line(125, 245, 125, 280)
                    c.line(125, 300, 125, 325)
                    c.line(125, 345, 125, 400)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(325, 210)
                    draw_arc(325, 195)
                    draw_arc(325, 182.5)
                    draw_arc(325, 170)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 317.5, 210)
                    c.line(332.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 317.5, 195)
                    c.line(332.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 317.5, 182.5)
                    c.line(332.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 317.5, 170)
                    c.line(332.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 250)
                    c.line(380, 250, 460, 250)
                    c.line(460, 250, 460, 278)
                    c.line(460, 297, 460, 318)
                    c.line(460, 340, 460, 400)
                    draw_switch(460, 320, 0)
                    c.drawString(470, 330, 'Inverter 2 AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter2ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(470, 315, '%s' % i1iso)
                    draw_switch(460, 280, 0)

                    c.drawString(470, 290, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(470, 275, '%s' % SSiso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 265)
                    c.line(355, 265, 440, 265)
                    c.line(440, 265, 440, 400)
                    draw_arc(380, 210)

                    ##L1 P1 Line
                    c.line(140, 400, 140, 370)
                    c.line(140, 370, 325, 370)
                    c.line(325, 370, 325, 312.5)
                    draw_switch(325, 295, 0)
                    c.setFont('Helvetica', 6)
                    c.drawString(330, 310, 'EPS AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?', EPSACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(330, 295, '%s' % i1iso)
                    c.setFont('Helvetica', 7)

                    c.line(325, 292.5, 325, 263)
                    draw_switch(325, 245, 0)
                    c.line(325, 243, 325, 125)
                    c.line(325, 125, 250, 125)

                    c.line(250, 125, 250, 75)
                    c.circle(250, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 247, 70, width=7, height=7)
                    c.line(280, 125, 280, 75)
                    c.circle(280, 125, 2, stroke=1, fill=1)
                    c.drawImage(trianglepath, 277, 70, width=7, height=7)
                    c.drawCentredString(250, 135, 'L1')
                    c.drawCentredString(280, 135, 'P1')

                    ##backfeed
                    c.setFont('Times-Italic', 6)
                    c.drawString(312, 510, '* In case of blackout, ')
                    c.drawString(312, 503, ' blackout backfeed')
                    c.drawString(312, 496, ' is impossible')
                    c.drawString(10, 390, '* Inverter isolates in ')
                    c.drawString(10, 383, 'the event of a blackout')
                    c.drawString(340, 390, '* Inverter isolates ')
                    c.drawString(340, 383, 'in the event of a blackout')

                if battery == 1 and current == 'AC':
                    draw_battery(270, 400, batteryl)
                    draw_inverter(250, 315, inverter1, inverterno, 'Y')
                    x = 15
                    y = 680
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    x += 325
                    c.circle(x + 65, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 77.5, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 90, y - 205, 2, stroke=1, fill=1)
                    c.circle(x + 102.5, y - 205, 2, stroke=1, fill=1)

                    ##BOTTOM
                    draw_switch(145, 195, 270)
                    draw_switch(145, 182.5, 270)
                    draw_switch(145, 170, 270)
                    c.setFont('Helvetica', 7)
                    c.drawCentredString(152.5, 155, 'Main')
                    c.drawCentredString(152.5, 145, 'Switch')
                    c.circle(245, 210, 2, stroke=1, fill=1)

                    ##main line
                    c.line(245, 210, 245, 230)
                    c.line(245, 230, 100, 230)
                    c.line(100, 230, 100, 400)
                    ##inv switch line

                    c.setFont('Helvetica', 7)
                    c.drawString(135, 340, 'Inverter 1 Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter1ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(135, 325, '%s' % i1iso)

                    c.drawString(135, 295, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(135, 280, '%s' % SSiso)
                    draw_switch(125, 327, 0)
                    draw_switch(125, 282, 0)
                    c.line(265, 195, 265, 245)
                    c.line(265, 245, 125, 245)
                    c.line(125, 245, 125, 280)
                    c.line(125, 300, 125, 325)
                    c.line(125, 345, 125, 400)

                    c.circle(285, 210, 2, stroke=1, fill=1)
                    c.line(285, 210, 285, 315)

                    c.circle(305, 195, 2, stroke=1, fill=1)
                    draw_switch(305, 270, 0)
                    c.drawString(315, 290, 'Battery AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                BatteryACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(315, 275, '%s' % i1iso)
                    c.line(305, 195, 305, 268)
                    c.line(305, 287, 305, 315)

                    ##out of m into CN
                    ##ac inv arcs
                    draw_arc(265, 210)
                    c.circle(265, 195, 2, stroke=1, fill=1)
                    draw_arc(305, 210)

                    c.line(95, 150, 95, 210)
                    c.line(95, 210, 257.5, 210)
                    c.line(272.5, 210, 292.5, 210)
                    c.line(292.5, 210, 297.5, 210)
                    c.line(312.5, 210, 372.5, 210)
                    c.line(387.5, 210, 430, 210)

                    c.line(105, 150, 105, 195)
                    c.line(105, 195, 144, 195)
                    c.line(162, 195, 312.5, 195)
                    c.line(312.5, 195, 430, 195)
                    c.line(430, 195, 430, 100)

                    c.line(115, 150, 115, 182.5)
                    c.line(115, 182.5, 144, 182.5)
                    c.line(162, 182.5, 217.5, 182.5)
                    c.line(232.5, 182.5, 312.5, 182.5)
                    c.line(312.5, 182.5, 400, 182.5)
                    c.line(400, 182.5, 400, 100)

                    c.line(125, 150, 125, 170)
                    c.line(125, 170, 144, 170)
                    c.line(162, 170, 197.5, 170)
                    c.line(212.5, 170, 217.5, 170)
                    c.line(232.5, 170, 370, 170)
                    c.line(370, 170, 370, 100)

                    ##reposit

                    # ball to repo
                    c.line(185, 167.5, 185, 30)
                    c.line(205, 177.5, 205, 40)
                    c.line(225, 187.5, 225, 50)
                    c.line(185, 30, 300, 30)
                    c.line(205, 40, 300, 40)
                    c.line(225, 50, 300, 50)

                    # repo to VR
                    c.line(335, 55, 335, 150)
                    c.line(335, 150, 363.5, 150)
                    c.line(378.5, 150, 392.5, 150)
                    c.line(407.5, 150, 423.5, 150)

                    c.line(340, 55, 340, 135)
                    c.line(340, 135, 363.5, 135)
                    c.line(378.5, 135, 393.5, 135)

                    c.line(345, 55, 345, 120)
                    c.line(345, 120, 363.5, 120)

                    ##battery inverter wiring
                    c.circle(380, 195, 2, stroke=1, fill=1)
                    c.line(380, 195, 380, 250)
                    c.line(380, 250, 460, 250)
                    c.line(460, 250, 460, 278)
                    c.line(460, 297, 460, 318)
                    c.line(460, 340, 460, 400)
                    draw_switch(460, 320, 0)
                    c.drawString(470, 330, 'Inverter 2 AC Isolator')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                Inverter2ACIsolator)
                    i1iso = cur.fetchone()[0]
                    c.drawString(470, 315, '%s' % i1iso)
                    draw_switch(460, 280, 0)
                    c.drawString(470, 290, 'Solar Supply Main Switch')
                    cur.execute('SELECT ACBreaker FROM ACbreakerspecifications where ACBreaker =?',
                                SolarSupplyMainSwitch)
                    SSiso = cur.fetchone()[0]
                    c.drawString(470, 275, '%s' % SSiso)
                    c.circle(355, 210, 2, stroke=1, fill=1)
                    c.line(355, 210, 355, 265)
                    c.line(355, 265, 440, 265)
                    c.line(440, 265, 440, 400)
                    draw_arc(380, 210)

                    ##backfeed
                    c.setFont('Times-Italic', 7)
                    c.drawString(302, 540, '* In case of blackout, ')
                    c.drawString(302, 533, ' backfeed is ')
                    c.drawString(302, 526, 'impossible')
                    c.drawString(10, 390, '* Inverter isolates in ')
                    c.drawString(10, 383, 'the event of a blackout')
                    c.drawString(470, 390, '* Inverter isolates ')
                    c.drawString(470, 383, 'in the event of a blackout')

    basic_wiring(25, 100)
    complex_wiring(phase, array, battery, inverterno, current)
    c.save()
    url = r'file:///C:\Users\Solar4Life\Desktop\solar4life\sld generator files\SLD %s.pdf' % name
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    # make sure to close connection to database at end of program
    conn.close()

def VRC_GUI():
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()
    ## cable parameters
    window_vrc_gui = tk.Tk()
    window_vrc_gui.title("VRC make tool")
    window_vrc_gui.geometry('450x400')

    def combo_values_cable_thick():
        query = cur.execute('SELECT conductor_size FROM cccarray')
        data = []
        for row in cur.fetchall():
            data.append(row[0])
        return data

    lbl_1_VRC = tk.Label(window_vrc_gui, text="CC to POA Cable Thickness")
    lbl_1_VRC.grid(column=0, row=1)
    combo_1 = ttk.Combobox(window_vrc_gui, width=20, height=10)
    combo_1.grid(column=1, row=1)
    combo_1['values'] = combo_values_cable_thick()

    lbl_2 = tk.Label(window_vrc_gui, text="CC to POA distance")
    lbl_2.grid(column=0, row=2)
    txt_2 = tk.Entry(window_vrc_gui, width=10)
    txt_2.grid(column=1, row=2)

    lbl_3_VRC = tk.Label(window_vrc_gui, text="POA TO MB Cable Thickness")
    lbl_3_VRC.grid(column=0, row=3)
    combo_3 = ttk.Combobox(window_vrc_gui, width=20, height=10)
    combo_3.grid(column=1, row=3)
    combo_3['values'] = combo_values_cable_thick()

    lbl_4 = tk.Label(window_vrc_gui, text="POA TO MB distance")
    lbl_4.grid(column=0, row=4)
    txt_4 = tk.Entry(window_vrc_gui, width=10)
    txt_4.grid(column=1, row=4)

    lbl_5_VRC = tk.Label(window_vrc_gui, text="MB to INV Cable Thickness")
    lbl_5_VRC.grid(column=0, row=5)
    combo_5 = ttk.Combobox(window_vrc_gui, width=20, height=10)
    combo_5.grid(column=1, row=5)
    combo_5['values'] = combo_values_cable_thick()

    lbl_6 = tk.Label(window_vrc_gui, text="MB to INV distance")
    lbl_6.grid(column=0, row=6)
    txt_6 = tk.Entry(window_vrc_gui, width=10)
    txt_6.grid(column=1, row=6)

    # SB stuff. i dont understand
    # lbl_9_VRC = tk.Label(window_vrc_gui, text="SB")
    # lbl_9_VRC.grid(column=0, row=7)
    # combo_9 = ttk.Combobox(window_vrc_gui, width=30, height=20)
    # combo_9.grid(column=1, row=7)
    # combo_9['values'] = combo_values_cable_thick()
    #
    # lbl_10 = tk.Label(window_vrc_gui, text="SB")
    # lbl_10.grid(column=0, row=8)
    # txt_10 = tk.Entry(window_vrc_gui, width=10)
    # txt_10.grid(column=1, row=8)

    lbl_7_VRC = tk.Label(window_vrc_gui, text="Type_of_Service")
    lbl_7_VRC.grid(column=0, row=9)
    combo_7 = ttk.Combobox(window_vrc_gui, width=20, height=10)
    combo_7.set('underground')
    combo_7.grid(column=1, row=9)
    combo_7['values'] = ['overhead', 'underground', 'overhead from underground']

    lbl_8_VRC = tk.Label(window_vrc_gui, text="material")
    lbl_8_VRC.grid(column=0, row=10)
    combo_8 = ttk.Combobox(window_vrc_gui, width=20, height=10)
    combo_8.set('Cu')
    combo_8.grid(column=1, row=10)
    combo_8['values'] = ['Cu', 'other thing']

    quit = tk.Button(window_vrc_gui, text='GO', command=window_vrc_gui.quit)
    quit.grid(column=1, row=11)

    # make sure to close connection
    # to database at end of program
    conn.close()

    window_vrc_gui.mainloop()

    global cable_params

    class cable_params:
        CC_to_POA_Cable_Thickness_mm2 = float(combo_1.get())
        CC_to_POA_Distance_m = float(txt_2.get())
        POA_to_MB_Cable_Thickness_mm2 = float(combo_3.get())
        POA_to_MB_Distance_m = float(txt_4.get())
        MB_to_INV_Cable_Thickness_mm2 = float(combo_5.get())
        MB_to_INV_Distance_m = float(txt_6.get())
        #        MB_to_SB_Cable_Thickness_mm2 = float(combo_9.get())
        #        MB_to_SB_Distance_m = float(txt_10.get())
        Type_of_Service = combo_7.get()
        material = combo_8.get()

    window_vrc_gui.destroy()


##quite old. creates the voltage rise calculations for basic stuff fairly well.
# TODO does need refinement
def create_VRC(fname, name, address):
    """"""
    filename = os.path.join(fname + ".pdf")
    c = canvas.Canvas(filename)
    c.setLineWidth(.3)
    c.setFont('Helvetica', 12)

    # establish connecttion to database
    conn = sqlite3.connect('VRCtable.db')
    cur = conn.cursor()

    ## main meat of the program. uses classes and arrays to somwhat efficiently calculate values
    def calcs():

        ##finds ccc based on cable diameter and phase and calculates for each portion
        ##cc to poa
        invname = inverter_1_input
        cur.execute("SELECT MaxACCurrent FROM Inverterspecifications where Inverter = '%s' " % invname)
        a = cur.fetchone()[0]

        cur.execute('SELECT single_phase FROM cccarray where conductor_size = %d'
                    % cable_params.CC_to_POA_Cable_Thickness_mm2)
        b1 = cur.fetchone()[0]

        if cable_params.Type_of_Service == 'underground':
            cc_poa_ccc = 0.
        else:
            cc_poa_ccc = ((a * cable_params.CC_to_POA_Distance_m) / b1)

        ##poa to mb
        cur.execute('SELECT single_phase FROM cccarray where conductor_size = %d'
                    % cable_params.POA_to_MB_Cable_Thickness_mm2)
        b2 = cur.fetchone()[0]
        poa_mb_ccc = ((a * cable_params.POA_to_MB_Distance_m) / b2)

        ##mb to inverter
        cur.execute('SELECT single_phase FROM cccarray where conductor_size = %d'
                    % cable_params.POA_to_MB_Cable_Thickness_mm2)
        b3 = cur.fetchone()[0]
        mb_inv_ccc = ((a * cable_params.MB_to_INV_Distance_m) / b3)

        ## saves value to a dict so the name of each value is saved, then does basic
        ## operations to find total VRC and where the VRC for a portiun is maximum
        cccdict = {'cc_poa': cc_poa_ccc, 'poa_mb': poa_mb_ccc, 'mb_inv': mb_inv_ccc}
        totalrun = cc_poa_ccc + poa_mb_ccc + mb_inv_ccc
        highestccc = max(cccdict.values())
        maxname = (max(cccdict, key=cccdict.get))

        ##other drawing stuff
        c.drawCentredString(150, 620, '%s' % cable_params.material)
        c.drawCentredString(300, 620, '%s' % cable_params.material)
        c.drawCentredString(450, 620, '%s' % cable_params.material)

        ## changes bottom note on VRC based on whether or not it has passed certain conditions
        if totalrun > 3:
            c.drawCentredString(300, 320, 'Total is greater than 3%, please change something')
        else:
            c.drawCentredString(300, 320, 'Note: no single run is greater than 2%')
        if highestccc > 2:
            c.drawCentredString(300, 300, 'A single run, %s, is greater than 2%% . please change something' % maxname)
        else:
            c.drawCentredString(300, 300, ' and the total is not greater than 3%')

        ##cc to POA drawing
        c.drawCentredString(150, 520, '%dm x %dmm^2' %
                            (cable_params.CC_to_POA_Distance_m, cable_params.CC_to_POA_Cable_Thickness_mm2))
        c.drawCentredString(150, 480, '%dA x %dm' %
                            (a, cable_params.CC_to_POA_Distance_m))
        c.line(100, 475, 200, 475)
        c.drawCentredString(150, 460, '%d' % a)
        c.drawCentredString(150, 430, '= %.3f%% VR' % cc_poa_ccc)

        ##POA to MB drawing
        c.drawCentredString(300, 520, '%dm x %dmm^2' %
                            (cable_params.POA_to_MB_Distance_m, cable_params.POA_to_MB_Cable_Thickness_mm2))
        c.drawCentredString(300, 480, '%dA x %dm' %
                            (a, cable_params.POA_to_MB_Distance_m))
        c.line(250, 475, 350, 475)
        c.drawCentredString(300, 460, '%d' % a)
        c.drawCentredString(300, 430, '= %.3f%% VR' % poa_mb_ccc)

        ##MB to inv drawing
        c.drawCentredString(450, 520, '%dm x %dmm^2' %
                            (cable_params.MB_to_INV_Distance_m, cable_params.MB_to_INV_Cable_Thickness_mm2))
        c.drawCentredString(450, 480, '%dA x %dm' %
                            (a, cable_params.MB_to_INV_Distance_m))
        c.line(400, 475, 500, 475)
        c.drawCentredString(450, 460, '%d' % a)
        c.drawCentredString(450, 430, '= %.3f%% VR' % mb_inv_ccc)
        ##

    def draw_background(name, address):

        ##Title
        c.drawCentredString(300, 750, 'Voltage Rise Calculations for %s - %s' % (name, address))
        c.circle(75, 650, 10, stroke=1, fill=1)
        c.circle(225, 650, 10, stroke=1, fill=1)
        c.circle(375, 650, 10, stroke=1, fill=1)
        c.circle(525, 650, 10, stroke=1, fill=1)

        c.drawCentredString(75, 600, 'CC')
        c.drawCentredString(225, 600, 'P.O.A')
        c.drawCentredString(375, 600, 'M.B')
        c.drawCentredString(525, 600, 'INV')

        c.line(75, 650, 525, 650)
        c.line(225, 575, 225, 400)
        c.line(375, 575, 375, 400)

    draw_background(name, address)
    calcs()
    c.save()
    url = r'file:///C:\Users\Solar4Life\Desktop\solar4life\sld generator files\VRC diagram.pdf'
    chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
    webbrowser.get(chrome_path).open(url)
    # make sure to close connection to database at end of program
    conn.close()


#starting gui. nice n tidy.
def start_screen():
    class Application(tk.Frame):
        def __init__(self, master=None):
            super().__init__(master)
            self.mainwindow = mainwindow
            self.pack()
            self.create_widgets()

        def create_widgets(self):
            # creates entry box for customer ID.
            self.entrybutton = tk.Entry(self, width=10)
            self.entrybutton.grid(column=1, row=2)

            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "enter customer ID (123456)"
            self.hi_there["command"] = self.say_hi
            self.hi_there.grid(column=2, row=2)

            self.design1 = tk.Button(self)
            self.design1["text"] = "design and test"
            self.design1["command"] = self.design_tool
            self.design1.grid(column=1, row=4)

            self.makeSLD = tk.Button(self)
            self.makeSLD["text"] = "SLD"
            self.makeSLD["command"] = self.SLD
            self.makeSLD.grid(column=1, row=5)

            self.makeVRC = tk.Button(self)
            self.makeVRC["text"] = "VRC"
            self.makeVRC["command"] = self.VRC
            self.makeVRC.grid(column=1, row=6)


            self.quit = tk.Button(self, text="QUIT", fg="red",
                                  command=self.master.destroy)
            self.quit.grid(column=1, row=7)

        def say_hi(self):
            customer_ID_int = int(self.entrybutton.get())
            customer_ID = ('%d' % customer_ID_int,)
            name_address(customer_ID)

        def design_tool(self):
            designgui()
            input_from_main()

        def SLD(self):
            SLDGUI()
            SLD_name = "SLD %s" % name
            create_SLD(SLD_name, inverterno, battery, arrays, phase, current, reposit)

        def VRC(self):
            VRC_GUI()
            create_VRC("VRC diagram", name, address)

    mainwindow = tk.Tk()
    mainwindow.title("main engineering tool")
    mainwindow.geometry('250x200')
    app = Application(master=mainwindow)
    app.mainloop()

start_screen()
conn.close()
