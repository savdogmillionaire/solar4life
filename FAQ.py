

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

from designgui import array_1_model_input,array_1_length,array_1_strings,array_2_length,array_2_strings,inverter_1_input,ac_breaker_current_limit
#from input_from_main import *
from SLDGUI import inverterno, battery, arrays, phase, current, reposit
from SLDGenSQLCopy import *

customer_ID = (123456,)
create_SLD('SLD', inverterno, battery, arrays, phase,customer_ID,current, reposit)

