from imu_nmea import (t_dict)
from datetime import datetime
import shutil
import csv
import pandas as pd 
import numpy as np
import os


    # #list_to_csv
    # with open(base, 'w', newline='') as csv_file:
    #     csv_writer = csv.writer(csv_file)
    #     for item in nmea_edited:
    #         csv_writer.writerow(item)
#duple
# base = os.path.splitext(nmea_file)[0] + '_imu_edited' + '.csv'
# shutil.copyfile(nmea_file, base)

#list_to_csv
# with open('list_to_csv.csv', 'w', newline='') as csv_file:
    # csv_writer = csv.writer(csv_file)
    # for item in nmea_edited:
        # csv_writer.writerow([item])

# nmea_ed =  kill_dubs('test/050420/test_2/nmea_moded_for_tests.NMEA')
#print(nmea_ed)



#args: (nmea_file, imu_file, near_time_NMEA, near_time_IMU, median_time):
time_new = t_dict('test/050420/test_2/nmea_moded_for_tests.NMEA', 
                                                    'test/050420/test_2/imu_2.csv', 45, 0.2, 2)
pd.set_option("display.max_rows", None, "display.max_columns", None)
print(pd.DataFrame(time_new))    


#args: (nmea_file, imu_file, near_time_NMEA, near_time_IMU, median_time):
# dict_x, rmc_time, rmc_ang = t_dict('test/050420/test_2/nmea_moded_for_tests.NMEA', 
#                                                     'test/050420/test_2/imu_2.csv', 15, 0.4, 2)
# print(dict_x, '\n'*2, rmc_time, '\n'*2, rmc_ang)

#x = datetime.utcfromtimestamp(1586083722144/1000).strftime('%H%M%S.%f')


