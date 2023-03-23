'''
                                     MOUSE MOVING BOT
'''
import pyautogui as pag
import random
import time

while True:
    x=random.randint(600,700)  #  These are just the coordinates on monitor /
    y=random.randint(200,600)  #   Pixel values
    pag.moveTo(x,y,0.5) #0.5 is the speed with which the mouse moves
    time.sleep(3)