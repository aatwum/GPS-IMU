time = '010504.254'

def hhmmss_to_s(RMC_time):
    h = float(str(RMC_time)[0:2])
    m = float(str(RMC_time)[2:4])
    s = float(str(RMC_time)[4:])
    sec = 3600*h + 60*m + s
    return sec
print(hhmmss_to_s(time))    