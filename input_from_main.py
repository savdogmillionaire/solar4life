from designgui import array_1_model_input, array_1_length, array_1_strings, array_2_length, array_2_strings, \
    inverter_1_input, ac_breaker_current_limit


class array:
    def __init__(self, number, model, panel_Voc, Voctemperaturecoeffcient_pc_per_C, panel_isc, wattage, panels,
                 strings):
        self.number = number
        self.model = model
        self.panel_Voc = panel_Voc
        self.Voctemperaturecoeffcient_pc_per_C = Voctemperaturecoeffcient_pc_per_C
        self.panel_isc = panel_isc
        self.wattage = wattage
        self.panels = panels
        self.strings = strings


class string(array):
    def __init__(self, number, model, panel_Voc, Voctemperaturecoeffcient_pc_per_C, panel_isc, wattage, panels, strings,
                 str_number, length):
        array.__init__(self, number, model, panel_Voc, Voctemperaturecoeffcient_pc_per_C, panel_isc, wattage, panels,
                       strings)
        self.str_number = str_number
        self.length = length


class inverter:
    def __init__(self, number, model, ac_breaker_current_limit, Max_AC_inverter_current, panel_startup_input_voltage,
                 nominal_output, I_mppt_max, I_DC_max):
        self.number = number
        self.model = model
        self.ac_breaker_current_limit = ac_breaker_current_limit
        self.Max_AC_inverter_current = Max_AC_inverter_current
        self.panel_startup_input_voltage = panel_startup_input_voltage
        self.nominal_output = nominal_output
        self.I_mppt_max = I_mppt_max
        self.I_DC_max = I_DC_max


class systemspecs:
    # inputs
    def __init__(self, array1, array2, inverter1, string1, string2, string3, string4, application):

        self.array1 = array1
        self.array2 = array2
        self.inverter1 = inverter1
        self.string1 = string1
        self.string2 = string2
        self.string3 = string3
        self.string4 = string4
        self.application = application

    # calculates total open circuit voltage taking weather into account
    def array_Voc(self):
        array_Voc_1 = self.array1.panels * self.array1.panel_Voc
        array_Voc_2 = self.array2.panels * self.array2.panel_Voc
        return (array_Voc_1, array_Voc_2)

    # calculates total open circuit voltage taking weather into account
    def panel_Voc_minus_10(self):
        panel_1_Voc_minus_10 = self.array1.panel_Voc + (
                ((self.array1.Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array1.panel_Voc)
        panel_2_Voc_minus_10 = self.array2.panel_Voc + (
                ((self.array2.Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array2.panel_Voc)
        return (panel_1_Voc_minus_10, panel_2_Voc_minus_10)

    def array_Voc_minus_10(self):
        array_1_Voc_minus_10 = (self.array1.panel_Voc + (((
                                                                  self.array1.Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array1.panel_Voc)) * self.array1.panels
        array_2_Voc_minus_10 = self.panel_Voc_minus_10()[1] * self.array2.panels
        # array_2_Voc_minus_10 =  (self.array_2.panel_Voc + (((self.array_2.Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array_2.panel_Voc)) * self.array_2.panels
        return (array_1_Voc_minus_10, array_2_Voc_minus_10)

    ##calcualtes total short circuit current
    def array_Isc(self):
        array_1_Isc = self.array1.strings * self.array1.panel_isc
        array_2_Isc = self.array2.strings * self.array2.panel_isc
        return (array_1_Isc, array_2_Isc)

    # checks whether the array ISC will cause clipping but will still work, if it the configuration cant be used at all,
    # or if it is fine
    def inverter_mppt_max_check(self):

        array_isc1 = self.array_Isc()[0]
        array_isc2 = self.array_Isc()[1]

        if (array_isc1 and array_isc2) < self.inverter1.I_DC_max and (
                array_isc1 and array_isc2) < self.inverter1.I_mppt_max:
            return "GOOD"
        if (array_isc1 and array_isc2) < self.inverter1.I_DC_max and (
                array_isc1 and array_isc2) > self.inverter1.I_mppt_max:
            return "KINDA BAD"
        if (array_isc1 and array_isc2) > self.inverter1.I_DC_max and (
                array_isc1 and array_isc2) > self.inverter1.I_mppt_max:
            return "BAD"

    ##checks to see if the total array wattage is less than CEC mandated max wattage guideline.
    # based on nominal inverter output
    def CEC_Oversize_Check(self):
        oversize = self.array1.panels * self.array1.wattage
        answer2 = self.inverter1.nominal_output * 1.33
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

    # checks if there are a minimum amount of panel to exceed the minimum inverter startup voltage
    def Min_panels_startup(self):
        smallest_Voc = min(self.panel_Voc_minus_10())
        answer = self.inverter1.panel_startup_input_voltage / smallest_Voc
        return answer

    # calculates the maximu amount of panels that can be placed that will be under the maximim system rating
    def Power_optimiser_limit(self):
        oversize1 = self.inverter1.nominal_output * (4 / 3)
        answer = oversize1 / self.array1.wattage
        return "Number of Panels less than or equal to allowed based on %.2fW inverter oversizing: %d" % (
            oversize1, answer)

    ## checks if the ac breaekr rating is 1.2 * the max inverter dc output
    def Circuit_breaker_current_limit(self, ac_breaker_current):
        answer = ac_breaker_current * 1.2
        if self.inverter1.Max_AC_inverter_current > answer:
            raise ValueError('Max AC output current of the Inverter is greater than maximum allowed AC Breaker')
            # return "Max AC output current of the Inverter %dA is greater than maximum allowed AC Breaker " \
            # "current of %dA, please change" % (self.inverter1.Max_AC_inverter_current, answer)
        else:
            return "Maximum allowed AC Breaker current of %dA works with Inverter output " \
                   "current of %dA" % (answer, self.inverter1.Max_AC_inverter_current)

    # checks if the strings in an array are of uneven length
    def Even_Odd_string_length(self):
        if self.array1.strings == 1:
            answer = 'string length comparison not applicable'
        elif self.array1.strings > 1 and self.string1.length % self.string2.length != 0:
            answer = 'uneven string length in array'
        elif self.array2.strings > 1 and self.string3.length % self.string4.length != 0:
            answer = 'uneven string length in array'
        else:
            answer = 'string lengths of mppt are equal'
        return answer


## this part will take vlaues that have been input from the main System design program. for now...
array_1 = array(1, array_1_model_input, 39.7, -0.03, 15, 330, array_1_length, array_1_strings)
array_2 = array(2, array_1_model_input, 39.7, -0.03, 5, 270, array_2_length, array_2_strings)
array_3 = array(3, array_1_model_input, 39.7, -0.03, 15, 330, 10, 2)
array_4 = array(4, array_1_model_input, 39.7, -0.03, 5, 270, 20, 2)
string_1 = string(1, 'model1', 39.7, -0.03, 5, 270, 15, 2, 1, array_1_length)
string_2 = string(1, 'model1', 39.7, -0.03, 5, 270, 5, 2, 2, array_1_length)
string_3 = string(2, 1, 1, 1, 1, 11, 1, 1, 1, array_2_strings)
string_4 = string(2, 1, 1, 1, 11, 1, 1, 1, 1, array_2_strings)
string_5 = string(3, 'model1', 39.7, -0.03, 5, 270, 15, 2, 1, 10)
string_6 = string(3, 'model1', 39.7, -0.03, 5, 270, 5, 2, 2, 10)
string_7 = string(4, 1, 1, 1, 1, 11, 1, 1, 1, 1)
string_8 = string(5, 1, 1, 1, 11, 1, 1, 1, 1, 1)

inverter_1 = inverter(1, inverter_1_input, 25, 20, 150, 5000, 10, 18)
inverter_2 = inverter(2, 'b', 25, 20, 150, 5000, 10, 18)

system_1 = systemspecs(array_1, array_2, inverter_1, string_1, string_2, string_3, string_4, 'Residential')
system_2 = systemspecs(array_3, array_4, inverter_2, string_5, string_6, string_7, string_8, 'Commercial')

print(system_1.string1.length)
print(system_1.array_Voc())
print(system_1.array_Voc_minus_10())
print(system_1.array_Isc())
print(system_1.inverter_mppt_max_check())
print(system_1.CEC_Oversize_Check())
print(system_1.Max_panels())
print(system_1.Min_panels_startup())
print(system_1.Power_optimiser_limit())
print(system_1.Circuit_breaker_current_limit(ac_breaker_current_limit))
print(system_1.Even_Odd_string_length())
print("")
