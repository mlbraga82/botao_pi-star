import os
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
#GPIO.setup(10, GPIO.IN)
#GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
prev_input=0
print ("Entrando no modo loop...")
while True:
        input=GPIO.input(10)
        if ((not prev_input) and input):
                os.system("python3 last_tg.py")
        prev_input=input
        time.sleep(0.05)
