from imu_nmea import (hhmmss_to_s, nearest, angle_control, 
                                mid_near, median_value, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


x = t_dict('nmea.csv', 'imu.csv', 15, 0.2, 1.2)


# imu = pd.read_csv('imu.csv', sep =',', comment = '@',  usecols=['timestamp', 'orientation.x'])

# imu_time, imu_ang = zip(*[[hhmmss_to_s(float(datetime.utcfromtimestamp(i[0]/1000).strftime('%H%M%S.%f'))), i[1]] 
#                                                                     for i in imu.values.tolist()])

# print(imu_time, imu_ang)
# time_dict, RMC_time, RMC_ang = t_dict('nmea.csv', 20)

# print(time_dict, RMC_time, RMC_ang)


# for key in time_dict.keys():
#     x = [RMC_ang[i] for i in mid_near(RMC_time, key, 1.2)]
#     if len(x) > 0:
#         med = np.median(angle_control(x))
#         if med < 0:
#             med += 360
            
#         print(key, med)    
    


# print(data_time)                                                              



