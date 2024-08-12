import pyautogui as pt
from time import sleep

def move_character(direction):
    if direction == "d":
        pt.keyDown("d")
        pt.keyUp("s")
    elif direction == "s":
        pt.keyDown("s")
        pt.keyUp("d")

def detect_line_change():
    if pt.locateCenterOnScreen("down.png", confidence=0.5):
        print("detected down change")
        move_character("s")
    elif pt.locateCenterOnScreen("up.png", confidence=0.5):
        print("detected up change")
        move_character("d")
    else:
        return None

sleep(4)
pt.mouseDown()
move_character("d")
while True:
    detect_line_change()
    