from imu_nmea import (hhmmss_to_s, nearest, angle_control, 
                                mid_near, median_value, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


#args: (nmea_file, imu_file, near_time_NMEA, near_time_IMU, median_time):
dict_x, rmc_time, rmc_ang = t_dict('test/050420/test_2/nmea_moded_for_tests.NMEA', 
                                                    'test/050420/test_2/imu_2.csv', 15, 0.4, 2)
print(dict_x, '\n'*2, rmc_time, '\n'*2, rmc_ang)

#x = datetime.utcfromtimestamp(1586083722144/1000).strftime('%H%M%S.%f')




