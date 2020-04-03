from imu_nmea import (hhmmss_to_s, nearest, angle_control, mid_near, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


time = '010504.254'
deg = [355, 118, 58, 0, 180, 245]
search_med = [355, 348, 12, 16, 8, 359, 0]



time_dict, RMC_time, RMC_ang = t_dict('nmea.csv', 20)

print(RMC_ang)
for key in time_dict.keys():
    x = [RMC_ang[i] for i in mid_near(RMC_time, key, 1)]
    if len(x) > 0:
        angles = angle_control(x)
        med = np.mean(angles)
        max_a = max(angles)
        min_a = min(angles)
        if med < 0:
            med += 360
        print(x, '\n', angles, '\n', med, '\n',max_a,  '\n', min_a,  '\n\n')    
    


x = (datetime.utcfromtimestamp(1582107260545/1000)).strftime('%H%M%S.%f')

imu = pd.read_csv('imu.csv', sep =',', comment = '@',  usecols=['timestamp', 'orientation.x'])

