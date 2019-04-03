

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

from input_from_main import *
from SLDGUI import inverterno, battery, arrays, phase, current, reposit
from SLDGenSQLCopy import *

customer_ID = (123456,)
create_SLD('SLD', inverterno, battery, arrays, phase,customer_ID,current, reposit)

