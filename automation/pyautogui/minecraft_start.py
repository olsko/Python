import win32gui, win32con, win32api
from time import sleep
import os
import pyautogui
os.startfile(r"C:\moje\aplikacje\minecraftlauncher\MinecraftLauncher.exe")
sleep(5)
print("Done")
hwnd = win32gui.GetForegroundWindow()
win32gui.ShowWindow(hwnd,win32con.SW_MAXIMIZE)
sleep(10)
pyautogui.click(1050,730)
sleep(10)