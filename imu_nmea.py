from datetime import datetime
import csv
import pandas as pd 
import numpy as np
import os


def hhmmss_to_s(RMC_time, versa=False):
    if versa == False:
        h = float(str(RMC_time)[0:2])
        m = float(str(RMC_time)[2:4])
        s = float(str(RMC_time)[4:])
        sec = 3600*h + 60*m + s
        return sec
    if versa == True:   
        h = int(RMC_time//3600)
        m = int((RMC_time - 3600*h)//60)
        s = float(RMC_time - h*3600 - m*60)
        return round(float(str(h)+str(m)+str(s)), 2)

def nearest(time_data, target, time):
    if len(time_data) != 0:
        t = min(time_data, key=lambda x: abs(x-target))
        if abs(target - t) > time:
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


def mid_near(time_data, value, time):
    near_list = []
    for i in range(0, 50):
        f = time_data[time_data.index(value) - i]
        if abs(value - f) > time:
            break
        near_list.append(time_data.index(value) - i)
    return near_list


def median_value(value, time_data, ang_data, time):
    x = [ang_data[i] for i in mid_near(time_data, value, time)]
    if len(x) > 0:
        med = np.median(angle_control(x))
        if med < 0:
            med += 360
        return med        


def t_dict(nmea_file, imu_file, near_time_NMEA, near_time_IMU, median_time):

    base = os.path.splitext(nmea_file)[0]
    os.rename(nmea_file, base + ".csv")
   
    imu = pd.read_csv(imu_file, sep =',', comment = '@',  usecols=[0, 1])
    imu_time, imu_ang = zip(*[[hhmmss_to_s(float(datetime.utcfromtimestamp(i[0]/1000).strftime('%H%M%S.%f'))), 
                                                                i[1]] for i in imu.values.tolist()])
    imu_time, imu_ang = list(imu_time), list(imu_ang)
    #print([hhmmss_to_s(n, versa=True) for n in imu_time])
    
    nmea = open(base + ".csv")
    nmea_data = []
    for line in nmea.readlines(): 
        nmea_data.append(line.split(','))   
    RMC_time = []
    RMC_ang = []
    time_dict = {}
    time_new = []
    log = []
    for line in nmea_data:
        if line[0] == '$GPRMC':      # OR GNRMC !!
            print(line[0], line[1], line[8])
            line_1 = float(line[1])
            if line[8] != '' and float(line[8]) != 0:
                line_8 = float(line[8])
                RMC_time.append(hhmmss_to_s(line_1))
                RMC_ang.append(line_8)
            if line[8] == '' or float(line[8]) == 0:
                near = nearest(RMC_time, hhmmss_to_s(line_1), near_time_NMEA)    #15       
                if time_dict.get(near) == None:  #Fill last NaNs
                    if len(time_dict) != 0:
                        x = nearest(imu_time, time_nmea, near_time_IMU)
                        print('x = ', hhmmss_to_s(x, versa = True))
                        if x != None:
                            ang_nmea = median_value(time_nmea, RMC_time, RMC_ang, median_time)  #1.2
                            ang_imu = imu_ang[imu_time.index(x)] #0.2
                            delta = ang_nmea - ang_imu
                            for n in log:
                                y = nearest(imu_time, n, near_time_IMU)
                                print('y = ', hhmmss_to_s(y, versa = True))
                                if y != None:
                                    new_ang = imu_ang[imu_time.index(y)] + delta
                                    if new_ang > 360:
                                        new_ang -= 360
                                    elif new_ang < 0:
                                        new_ang += 360
                                    time_new.append([hhmmss_to_s(n, versa = True), new_ang])                        
                        print(log)
                        log.clear() 
                if near != None:      
                    log.append(hhmmss_to_s(line_1))
                    time_dict.update({near:log}) 
                    time_nmea = near   
    nmea.close()
    os.rename(base + ".csv", base + ".NMEA")         
    return time_new #, RMC_time, RMC_ang

