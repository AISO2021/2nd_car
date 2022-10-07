#!/usr/bin/python
# -*- coding: utf-8 -*-

import pigpio
import time

DIRpin = 6 #DIRのピン 物理(31)
PWMpin = 12 #PWMのピン 物理(32)

Pulsepin = 16 #pulseを受け取る 物理(36)

Freq = 100000

pi = pigpio.pi()

pi.set_mode(DIRpin, pigpio.OUTPUT)
pi.set_mode(PWMpin, pigpio.OUTPUT)
pi.set_mode(Pulsepin, pigpio.INPUT)

print("[INFO]\nPin Setup Completed!")

def terminate():
    try:
        pi.write(DIRpin, 0)
        pi.write(PWMpin, 0)
    except Exception:
        pass
    finally:
        print("Terminated!")
        pi.stop()

def duty2per(duty):
    return int(duty * 1000000 / 100.) # duty 0~1M

def motor(sw):
    if sw == 1:
        print("Motor ON")
        pi.write(DIRpin, 0)
    
    elif sw == 0:
        print("Motor OFF")
        pi.write(DIRpin, 1)


if __name__ == '__main__':
    print("In The Main Function!")

    pi.hardware_PWM(PWMpin, Freq, duty2per(30))

    try:
        while True:
            motor(1)
            time.sleep(5)
            motor(0)
            time.sleep(5)

    except (KeyboardInterrupt):
        terminate()
        exit()




    