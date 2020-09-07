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
#       print('.')
        input=GPIO.input(10)
#       print ("input:",input)
        if ((not prev_input) and input):
                print("button pressed")
                os.system("python3 last_tg.py")
#               os.system('ssh pi-star@py7slb.local ./deltg.sh')
        prev_input=input
        time.sleep(0.05)
