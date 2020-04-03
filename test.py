from imu_nmea import (hhmmss_to_s, nearest, mid_near, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


time = '010504.254'
deg = [355, 118, 58, 0, 180, 245]
search_med = [355, 348, 12, 16, 8, 359, 0]


def medium_angle(data):
    rad_data = []
    for i in range(len(data)):
        if data[i] >= 0 and data[i] <= 180:
            rad_data.append(data[i])            
        if data[i] > 180 and data[i] < 360:
            rad_data.append(data[i] - 360)
    return rad_data

 

time_dict, RMC_time, RMC_ang = t_dict('nmea.csv', 20)

print(time_dict)

# for key in time_dict.keys():
#     def_near = [RMC_ang[i] for i in mid_near(RMC_time, key, 1)]  #ЕСЛИ 360 то хз
#     print(np.max(def_near), np.min(def_near))


x = (datetime.utcfromtimestamp(1582107260545/1000)).strftime('%H%M%S.%f')

imu = pd.read_csv('imu.csv', sep =',', comment = '@',  usecols=['timestamp', 'orientation.x'])

