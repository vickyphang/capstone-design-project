import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13, GPIO.IN, pull_up_down = GPIO.PUD_UP)

def CekStockAir():
	StockAir = GPIO.input(13)
	return StockAir