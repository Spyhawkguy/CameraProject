#!/usr/bin/env python
from time import sleep
from gpiozero import Button
import subprocess
import os
import sys

os.chdir('/home/pi/CameraProject')

pButton = Button(17)
kButton = Button(15)

def preview():
    subprocess.Popen(["./preview"])
    
def shoot():
    subprocess.Popen(["./shoot"])
    
def killSwitch():
    subprocess.Popen(["./killSwitch"])

sleep(5)

preview()

while True:
    if pButton.value == 1:
        shoot()
        sleep(3)
        preview()
    if kButton.value ==1:
        killSwitch()
        sys.exit()
        


