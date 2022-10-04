import pigpio
import time

pin_num = 16
counter = 0
flag = False

pi=pigpio.pi()

pi.set_mode(pin_num, pigpio.INPUT)
#pi.set_pull_up_down(pin_num, pigpio.PUD_UP)

while True:
    sw = pi.read(pin_num)
    if sw == 0:
        print('on')
        if flag == False:
            counter = 0
            flag = True
    if sw == 1:
        print('off')
        if flag == True:
            counter = 0
            flag = False
    counter += 1
    print(counter)
    