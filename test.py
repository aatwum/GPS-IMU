from imu_nmea import (hhmmss_to_s, nearest, angle_control, 
                                mid_near, median_value, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


x = t_dict('nmea.csv', 'imu.csv', 15, 2, 1.2)
print(x)

# time_nmea = 155000
# time_data = [145553, 463223, 154830, 154940, 155000]
# ang_data = [10, 15, 105, 120, 130]
# time = 10000

# def median_value(value, time_data, ang_data, time):
#     x = [ang_data[i] for i in mid_near(time_data, value, time)]
#     if len(x) > 0:
#         med = np.median(angle_control(x))
#         if med < 0:
#             med += 360
#         return med 

# print(median_value(time_nmea, time_data, ang_data, time))

# imu = pd.read_csv('imu.csv', sep =',', comment = '@',  usecols=['timestamp', 'orientation.x'])

# imu_time, imu_ang = zip(*[[hhmmss_to_s(float(datetime.utcfromtimestamp(i[0]/1000).strftime('%H%M%S.%f'))), i[1]] 
#                                                                  for i in imu.values.tolist()])
# imu_time = list(imu_time)
# print(type(imu_time))  
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



