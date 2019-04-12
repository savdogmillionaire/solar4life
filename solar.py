from pysolar.solar import *
import datetime
from dateutil import tz
import sqlite3

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np

AEST = tz.gettz('Australia/Canberra')
latitude_deg = -35.2809  # positive in the northern hemisphere
longitude_deg = 149.1300  # negative reckoning west from prime meridian in Greenwich, England


def make_irrad_table():
    date2 = datetime.datetime(2018, 5, 3)
    print(date2.strftime('%j'))
    days = int(date2.strftime('%j'))

    print(datetime.datetime(2018, 1, 1, 12) + datetime.timedelta(days - 1))

    irradiation_array = np.zeros((365, 14))
    day_count = 0
    while day_count < 365:
        hour = 7
        day_count += 1
        while hour <= 19:
            date = datetime.datetime(2018, 1, 1, hour, tzinfo=AEST) + datetime.timedelta(day_count - 1)
            altitude_deg = get_altitude(latitude_deg, longitude_deg, date)
            irradiation_array[day_count - 1, hour - 6] = radiation.get_radiation_direct(date, altitude_deg)
            hour += 1

    first_col_fill = 1
    while first_col_fill <= 365:
        irradiation_array[first_col_fill - 1, 0] = first_col_fill
        first_col_fill += 1

    np.savetxt('irradiation_array.csv', irradiation_array, fmt='%d', delimiter=',')


conn = sqlite3.connect('VRCtable.db')
cur = conn.cursor()

cur.execute('SELECT * FROM irradiation_array WHERE day_of_year = 14')
irrad_data_1 = cur.fetchone()
cur.execute('SELECT * FROM irradiation_array WHERE day_of_year = 114')
irrad_data_2 = cur.fetchone()

fig, ax = plt.subplots()
time = ['7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19']

print(irrad_data_1)
print(irrad_data_2)

ax.plot(time, irrad_data_1[1:])
ax.plot(time, irrad_data_2[1:])
fig.savefig("test.png")
plt.show()

date3 = datetime.datetime(2018, 1, 1, tzinfo=AEST) + datetime.timedelta(14 - 1)
date4 = int(date3.strftime('%m'))
print(date4)

conn.close()
