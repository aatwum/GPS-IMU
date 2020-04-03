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
        t = min(lst, key=lambda x: abs(hhmmss_to_s(x)-hhmmss_to_s(target)))
        if abs(hhmmss_to_s(target) - hhmmss_to_s(t)) > delta_t:
            return None
        else:
            return t
    else: 
        return None


def angle_control(data):
    rad_data = []
    for i in range(len(data)):           
        if data[i] > 180 and data[i] < 360:
            rad_data.append(data[i] - 360)
        else:
            rad_data.append(data[i])
    return rad_data


def mid_near(lst, last, delta_t):
    near_list = []
    for i in range(1, 100):
        f = lst[lst.index(last) - i]
        if last - f > delta_t:
            break
        near_list.append(lst.index(last) - i)
    return near_list


def t_dict(nmea_file, near_time):
    nmea = open(nmea_file)
    nmea_data = []
    for line in nmea.readlines(): 
        nmea_data.append(line.split(','))   
    RMC_time = []
    RMC_ang = []
    time_dict = {}
    log = []
    for line in nmea_data:
        if line[0] == '$GNRMC' and float(line[1]) < 101903.00:
            if line[8] != '':
                RMC_time.append(float(line[1]))
                RMC_ang.append(float(line[8]))
            if line[8] == '':
                near = nearest(RMC_time, float(line[1]), near_time)    #15
                if near != None:
                    if time_dict.get(near) == None:
                        log.clear()
                    log.append(line[1])
                    time_dict.update({near:tuple(log)})
    return time_dict, RMC_time, RMC_ang