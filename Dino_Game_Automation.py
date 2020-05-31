# -*- coding: utf-8 -*-
"""
Created on Sun May 24 17:44:53 2020

@author: Prabhanshu Aggarwal
"""

import pyautogui
from PIL import Image, ImageGrab
import time

def hit(key):
    pyautogui.keyDown(key)

def iscollide(data):
     for i in range(470,510):
         for j in range(225,250):
             if data[i,j]<100:
                 print("Jump")
                 return True
     return False
             
def iscollidebird(data): 
     for i in range(470,510):
         for j in range(190,220):
             if data[i,j]<100:
                 return True
     return False
                
if __name__=="__main__":
    print("Game Begins")
    time.sleep(3)
    hit("up")
    #Take image continuously
    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        if iscollide(data):
            hit('up')
            
        if iscollidebird(data):
            hit("down")
        
                 
       
    