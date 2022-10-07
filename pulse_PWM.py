#!/usr/bin/python
# -*- coding: utf-8 -*-

from pickle import TRUE
import pigpio
import time
import threading

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


class Pulse(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.onr = 0
        self.st = False
        self.co = 0
        self.kill = False

    def count(self, on):
        while not self.kill:
            self.onr = on
            if self.onr == 0:
                if self.st == False:
                    self.co += 1
                    self.st = True
            if self.onr == 1:
                self.st = False

            return self.co


if __name__ == '__main__':
    print("In The Main Function!")

    pi.hardware_PWM(PWMpin, Freq, duty2per(30))
    p = Pulse()
    p.start()

    try:
        while True:
            motor(1)
            oho = p.count(pi.read(Pulsepin))
            print(oho)

            if oho == 42000:
                pi.hardware_PWM(PWMpin, Freq, duty2per(30))

    except (KeyboardInterrupt):
        terminate()
        p.kill = True
        exit()




    