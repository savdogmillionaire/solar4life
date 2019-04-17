from pysolar.solar import *
import datetime
from dateutil import tz
import sqlite3
import calendar

import matplotlib.pyplot as plt

plt.style.use('seaborn-whitegrid')
import numpy as np

AEST = tz.gettz('Australia/Canberra')
latitude_deg = -35.2809  # positive in the northern hemisphere
longitude_deg = 149.1300  # negative reckoning west from prime meridian in Greenwich, England


def tilt_azimuth_factor(tilt, orientation):
    # kWhmod=Sincident[cos(α)sin(β)cos(Ψ−Θ)+sin(α)cos(β)]
    tilt_azimuth_factor = np.ones((1, 12))
    tilt_rad = tilt * (np.pi / 180)
    orientation_rad = orientation * (np.pi / 180)
    x = 1
    while x <= 12:
        date = datetime.datetime(2018, x, 15, 12, tzinfo=AEST)
        orientation_array = np.array(orientation_rad)
        tilt_array = np.array(tilt_rad)
        altitude = np.array(get_altitude(latitude_deg, longitude_deg, date)) * (np.pi / 180)

        azimuth = np.array(get_azimuth_fast(latitude_deg, longitude_deg, date)) * (np.pi / 180)

        panel_azimuth = np.subtract(azimuth, orientation_array)
        factor = ((np.cos(altitude) * np.sin(tilt_array) * np.cos(panel_azimuth)) \
                  + (np.sin(altitude) * np.cos(tilt_array)))
        tilt_azimuth_factor[0, x - 1] = tilt_azimuth_factor[0, x - 1] * factor
        x += 1
    return tilt_azimuth_factor


print(tilt_azimuth_factor(22.5, 0))
date = datetime.datetime(2018, 12, 15, tzinfo=AEST)
azimuth = np.array(get_azimuth(latitude_deg, longitude_deg, date))
altitude = np.array(get_altitude(latitude_deg, longitude_deg, date))
print(azimuth)
print(altitude)
