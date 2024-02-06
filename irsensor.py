import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)

def deteksibotol():
    while True:
        val = GPIO.input(11)
        print(val)
        if val == 0:
            print("detected")
            return False
        time.sleep(0.2)
    GPIO.cleanup()

def deteksibotol2():
    val = GPIO.input(11)
    if val == 0:
        botol = 1
        print("detected")
        return botol