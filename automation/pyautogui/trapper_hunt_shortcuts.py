import keyboard  # using module keyboard
from time import sleep
import pyautogui as pt
on = "on"
while True:
    if on == "on":
        for i in range(0,1000):
            i += 1
            pt.write(str(i)+ ". ")
            pt.hotkey('altright','A')
            pt.press('enter')
        break
        