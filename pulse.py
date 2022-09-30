import pigpio
import time
import threading
import rospy

pulse_R=16
pulse_L=26
pi=pigpio.pi()
pi.set_mode(pulse_R,pigpio.OUTPUT)
pi.set_mode(pulse_L,pigpio.OUTPUT)
print("start")
starttime_R=time.time()
stoptime_R=time.time()
starttime_L=time.time()
stoptime_L=time.time()
if pi.read(pulse_R)==0:
    starttime_R=time.time()
elif pi.read(pulse_R)==1:
    stoptime_R=time.time()
    print("recognize right")
elif pi.read(pulse_L)==0:
    starttime_L=time.time()
elif pi.read(pulse_L)==1:
    stoptime_L=time.time()
    print("recognize left")
else:
    print("nothing")
totaltime_R=starttime_R-stoptime_R
totaltime_L=starttime_L-stoptime_L
    
