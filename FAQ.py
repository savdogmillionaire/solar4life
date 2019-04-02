

#################################################
#
#
#
#      Welcome
#      This is where i do things.
#
#
#
#
#################################################

#from designgui import array_1_model_input,array_1_length,array_1_strings,array_2_length,array_2_strings,inverter_1_input,ac_breaker_current_limit
import input_from_main
from SLDGUI import inverterno, battery, arrays, phase, current, reposit
from SLDGenSQLCopy import *

create_SLD('SLD', name, address, inverterno, battery, arrays, phase)

