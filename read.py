import pigpio

pin_num = 16

pi=pigpio.pi()

pi.set_mode(pin_num, pigpio.INPUT)
pi.set_pull_up_down(pin_num, pigpio.PUD_UP)
print(pi.read(pin_num))