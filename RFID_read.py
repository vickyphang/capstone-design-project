import RPi.GPIO as GPO
from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522()

def bacaRFID():
	id = reader.read()
	print(id[0])
	return id[0]