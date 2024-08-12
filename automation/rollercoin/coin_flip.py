# -*- coding: utf-8 -*-
import pyautogui
import time

text = "Jeśli chodzi o towarzystwo, cenię sobie czas spędzony sam na sam z naturą, ale równie ważne jest dla mnie dzielenie tych doświadczeń z bliskimi przyjaciółmi lub rodziną. Ważne jest dla mnie, aby móc odprężyć się, zrelaksować i oderwać od codzienności"

# Set the typing speed in characters per second
typing_speed = 0.00001

# Wait for a few seconds to give time to switch to the target application
time.sleep(5)

# Type out the text character by character
for char in text:
        pyautogui.typewrite(char, interval=typing_speed)