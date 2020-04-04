from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


def hhmmss_to_s(RMC_time):
    h = float(str(RMC_time)[0:2])
    m = float(str(RMC_time)[2:4])
    s = float(str(RMC_time)[4:])
    sec = 3600*h + 60*m + s
    return sec


def nearest(lst, target, delta_t):
    if len(lst) != 0:
        t = min(lst, key=lambda x: abs(x-target))
        if abs(target - t) > delta_t:
            return None
        else:
            return t
    else: 
        return None


def angle_control(data):
    rad_data = []
    for i in data:           
        if i > 180 and i < 360:
            rad_data.append(i - 360)
        else:
            rad_data.append(i)
    return rad_data


def mid_near(lst, last, delta_t):
    near_list = []
    for i in range(1, 50):
        f = lst[lst.index(last) - i]
        if abs(last - f) > delta_t:
            break
        near_list.append(lst.index(last) - i)
    return near_list


def median_value(value, time_data, ang_data, time):
    x = [ang_data[i] for i in mid_near(time_data, value, time)]
    if len(x) > 0:
        med = np.median(angle_control(x))
        if med < 0:
            med += 360
    return med        


def t_dict(nmea_file, imu_file, near_time_NMEA, near_time_IMU, median_time):
    imu = pd.read_csv(imu_file, sep =',', comment = '@',  usecols=['timestamp', 'orientation.x'])
    imu_time, imu_ang = zip(*[[hhmmss_to_s(float(datetime.utcfromtimestamp(i[0]/1000).strftime('%H%M%S.%f'))), 
                                                                i[1]] for i in imu.values.tolist()])
    nmea = open(nmea_file)
    nmea_data = []
    for line in nmea.readlines(): 
        nmea_data.append(line.split(','))   
    RMC_time = []
    RMC_ang = []
    time_dict = {}
    time_dict_2 = {}
    log = []
    for line in nmea_data:
        if line[0] == '$GNRMC' and float(line[1]) < 101631.00:
            line_1 = float(line[1])
            if line[8] != '':
                line_8 = float(line[8])
                RMC_time.append(hhmmss_to_s(line_1))
                RMC_ang.append(line_8)
            if line[8] == '':
                near = nearest(RMC_time, hhmmss_to_s(line_1), near_time_NMEA)    #15
                if near != None:       
                    if time_dict.get(near) == None:
                        if len(time_dict) != 0:
                            ang_nmea = median_value(time_nmea, RMC_time, RMC_ang, median_time)   #1.2
                            ang_imu = imu_ang(imu_time.index(nearest(imu_time, time_nmea, near_time_IMU))) #0.2
                            delta = ang_nmea - ang_imu
                            for n in log:
                                new_ang = imu_ang(imu_time.index(nearest(imu_time, n, near_time_IMU))) + delta
                                time_dict_2.update({n:new_ang})                        
                        log.clear()
                    log.append(hhmmss_to_s(line_1))
                    time_dict.update({near:tuple(log)})
                    time_nmea = near
    return time_dict_2

