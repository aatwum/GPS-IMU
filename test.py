from imu_nmea import (hhmmss_to_s, nearest, angle_control, 
                                mid_near, median_value, t_dict)
from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


# args: (nmea_file, imu_file, near_time_NMEA, near_time_IMU, median_time):
x = t_dict('040420/nmea_2_del.NMEA', '040420/imu.csv', 15, 0.5, 1)
print(x)



