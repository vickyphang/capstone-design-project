import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(18, GPIO.OUT)
GPIO.output(18, GPIO.HIGH)

def ModulKontainerOff():
	GPIO.output(18, GPIO.LOW)
	time.sleep(1)

def ModulKontainerOn():
	GPIO.output(18, GPIO.HIGH)
	time.sleep(1)
	kontainer = 1
	return kontainer