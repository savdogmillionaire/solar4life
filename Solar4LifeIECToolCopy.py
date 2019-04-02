class system_specs:

    # inputs
    def __init__(self,
                 arrays,
                 strings_mppt1,
                 strings_mppt2,
                 strings_mppt3,
                 strings_mppt4,
                 array_number_of_panels,
                 panel_Voc,
                 Voctemperaturecoeffcient_pc_per_C,
                 panel_Isc,I_mppt_max_inv,
                 I_DC_max_inv,
                 panel_wattage,
                 inverter_nominal_output,
                 application,
                 panel_startup_input_voltage,
                 ac_breaker_current_limit,
                 Max_AC_inverter_current,
                 string1_panels,
                 string2_panels):

        self.strings_mpp_1 = strings_mppt_1
        self.strings_mpp_2 = strings_mppt_2
        self.strings_mpp_3 = strings_mppt_3
        self.strings_mpp_4 = strings_mppt_4

        self.string_1_panels = string1_panels
        self.string_2_panels = string2_panels
        self.string_3_panels = string3_panels
        self.string_4_panels = string4_panels
        self.string_5_panels = string5_panels
        self.string_6_panels = string6_panels
        self.string_7_panels = string7_panels
        self.string_8_panels = string8_panels

        self.array_1_number_of_panels = array_1_number_of_panels
        self.array_2_number_of_panels = array_2_number_of_panels
        self.array_3_number_of_panels = array_3_number_of_panels
        self.array_4_number_of_panels = array_4_number_of_panels

        self.array_1_panel_Voc = array_1_panel_Voc
        self.array_2_panel_Voc = array_2_panel_Voc
        self.array_3_panel_Voc = array_3_panel_Voc
        self.array_4_panel_Voc = array_4_panel_Voc

        self.array_1_Voctemperaturecoeffcient_pc_per_C = array_1_Voctemperaturecoeffcient_pc_per_C
        self.array_2_Voctemperaturecoeffcient_pc_per_C = array_2_Voctemperaturecoeffcient_pc_per_C
        self.array_3_Voctemperaturecoeffcient_pc_per_C = array_3_Voctemperaturecoeffcient_pc_per_C
        self.array_4_Voctemperaturecoeffcient_pc_per_C = array_4_Voctemperaturecoeffcient_pc_per_C

        self.array_1_panel_Voc_minus_10 = self.array_1_panel_Voc + (((array_1_Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array_1_panel_Voc)
        self.array_2_panel_Voc_minus_10 = self.array_2_panel_Voc + (((array_2_Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array_2_panel_Voc)
        self.array_3_panel_Voc_minus_10 = self.array_3_panel_Voc + (((array_3_Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array_3_panel_Voc)
        self.array_4_panel_Voc_minus_10 = self.array_4_panel_Voc + (((array_4_Voctemperaturecoeffcient_pc_per_C / 100) * -35) * self.array_4_panel_Voc)

        self.array_1_panel_Isc = array_1_panel_Isc
        self.array_2_panel_Isc = array_2_panel_Isc
        self.array_3_panel_Isc = array_3_panel_Isc
        self.array_4_panel_Isc = array_4_panel_Isc


        self.I_mppt_max_inv_1 = I_mppt_max_inv_inv_1
        self.I_mppt_max_inv_2 = I_mppt_max_inv_inv_2

        self.I_DC_max_inv_1 = I_DC_max_inv_1
        self.I_DC_max_inv_2 = I_DC_max_inv_2

        self.array_1_panel_wattage = array_1_panel_wattage
        self.array_2_panel_wattage = array_2_panel_wattage
        self.array_3_panel_wattage = array_3_panel_wattage
        self.array_4_panel_wattage = array_4_panel_wattage

        self.inverter_1_nominal_output = inverter_1_nominal_output
        self.inverter_2_nominal_output = inverter_2_nominal_output

        self.inverter_1_panel_startup_input_voltage = inverter_1_panel_startup_input_voltage
        self.inverter_2_panel_startup_input_voltage = inverter_2_panel_startup_input_voltage

        self.inverter_1_ac_breaker_current_limit = inverter_1_ac_breaker_current_limit
        self.inverter_2_ac_breaker_current_limit = inverter_2_ac_breaker_current_limit

        self.inverter_1_Max_AC_inverter_current = inverter_1_Max_AC_inverter_current
        self.inverter_2_Max_AC_inverter_current = inverter_2_Max_AC_inverter_current

        self.arrays = arrays
        self.application = application



    # calculates total open circuit voltage taking weather into account
    def array_Voc(self):
        array_Voc = self.array_number_of_panels * self.panel_Voc
        return array_Voc
    # calculates total open circuit voltage taking weather into account
    def array_Voc_minus_10(self):
        array_Voc_minus_10 = self.array_number_of_panels * self.panel_Voc_minus_10
        return array_Voc_minus_10
    ##calcualtes total short circuit current
    def array_Isc(self):
        array_Isc = self.strings_mppt * self.panel_Isc
        return array_Isc
    # checks whether the array ISC will cause clipping but will still work, if it the configuration cant be used at all,
    # or if it is fine
    def inverter_mppt_max_check(self):
        array_isc = self.strings_mppt * self.panel_Isc
        if array_isc < self.I_DC_max_inv and array_isc < self.I_mppt_max_inv:
            return "Short circuit current of array is perfect"
        if array_isc < self.I_mppt_max_inv and array_isc > self.I_DC_max_inv:
            return "Short circuit current of array is lower than max input current of inverter, but clipping" \
                   " may still occur. consider lowering Panel Isc"
        if array_isc > self.I_mppt_max_inv and array_isc > self.I_DC_max_inv:
            return "Short circuit current of array is higher than max input current of inverter, please" \
                   " change panels used, use fewer strings, or change inverter"

    ##checks to see if the total array wattage is less than CEC mandated max wattage guideline.
    # based on nominal inverter output
    def CEC_Oversize_Check(self):
        answer1 = self.array_number_of_panels * self.panel_wattage
        answer2 = self.inverter_nominal_output * 1.33
        if answer1 > answer2:
            return "Array wattage of %dW is larger than CEC guidelines of %dW, please change" % (answer1, answer2)
        else:
            return "Array wattage of %dW conforms to CEC guidelines of %dW" % (answer1, answer2)

    # checks how many panels can be placed for each inverter, and checks to tsee if the
    # applications is residential or commercial when calculating
    def Max_panels(self):
        if self.application == 'Residential':
            answer = 600 / (self.panel_Voc_minus_10)
            return "Maximum number of panels for each inverter: %d" % (answer)
        if self.application == 'Commercial':
            answer = 1000 / (self.panel_Voc_minus_10)
            return "Maximum number of panels for each inverter: %d" % (answer)
    #checks if there are a minimum amount of panel to exceed the minimum inverter startup voltage
    def Min_panels_startup(self):
        answer = self.panel_startup_input_voltage / (self.panel_Voc_minus_10)
        return "Minimum number of panels for each inverter: %d" % (answer)

    #calculates the maximu amount of panels that can be placed that will be under the maximim system rating
    def Power_optimiser_limit(self):
        oversize = self.inverter_nominal_output * (4/3)
        answer = oversize / self.panel_wattage
        return "Number of Panels less than or equal to allowed based on %.2fW inverter oversizing: %d" % (oversize, answer)

    ## checks if the ac breaekr rating is 1.2 * the max inverter dc output
    def Circuit_breaker_current_limit(self):
        answer = self.ac_breaker_current_limit * 1.2
        if self.Max_AC_inverter_current > answer:
            return "Max AC output current of the Inverter %dA is greater than maximum allowed AC Breaker " \
                   "current of %dA, please change" % (self.Max_AC_inverter_current, answer)
        else:
            return "Maximum allowed AC Breaker current of %dA works with Inverter output " \
                   "current of %dA" % (answer, self.Max_AC_inverter_current)

    # checks if the strings in an array are of uneven length
    def Even_Odd_string_length(self):
        if self.strings_mppt == 1:
            answer = 'string length comparison not applicable'
        elif self.strings_mppt > 1 and self.string1_panels % self.string2_panels != 0:
            answer = 'uneven string length in array'
        else:
            answer = 'string lengths of mppt are equal'
        return answer

















