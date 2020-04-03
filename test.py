from imu_nmea import (hhmmss_to_s, nearest, angle_control, mid_near, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


time = '010504.254'

#time_dict, RMC_time, RMC_ang = t_dict('nmea.csv', 20)


# for key in time_dict.keys():
#     x = [RMC_ang[i] for i in mid_near(RMC_time, key, 1.2)]
#     if len(x) > 0:
#         med = np.median(angle_control(x))
#         if med < 0:
#             med += 360
            
#         print(key, med, count)    
    


imu = pd.read_csv('imu.csv', sep =',', comment = '@',  usecols=['timestamp', 'orientation.x'])
data = imu.values.tolist()

for i in range(len(data)):
    data[i][0] = float(datetime.utcfromtimestamp(float(data[i][0])/1000).strftime('%H%M%S.%f'))

print(data)
