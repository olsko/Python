#The tap code, sometimes called the knock code, is a way to encode text messages on a letter-by-letter basis
#in a very simple way. The message is transmitted using a series of tap sounds, hence its name.
import os
from time import sleep

def tap_code(message):
    result = ""
    for char in message:
        row = int((ord(char) - ord('a')) / 5) + 1
        col = ((ord(char) - ord('a')) % 5) + 1
        
        if char == "k":
            row = 1
            col = 3
        
        if ord(char) >= ord('j') and col == 1:
            col = 6
            row = row - 1          
            col = col - 1
        
        if char != " ":
            dot_char = row * "." + " " + col * "."
        else:
            dot_char = " "
        
        result += dot_char + " | "
        
        return result

def start_2(option_choosed):
    if option_choosed == "1":
        print("Exited")
        sleep(2)
        clear()
    elif option_choosed == "2":
        clear()
        print(tap_code(input("Enter your message(all lowercase): ")))
        print(input(""))
        clear()
        return start_1()
    else:
        print("You must choose between 1 or 2")
        print(input(""))
        clear()
        return start_1()

def start_1():
    options = ["Exit", "Encryption"]
    for i in range(len(options)):
        print(str(i+1) + ":", options[i])
    start_2(input("Enter a number: "))

clear = lambda: os.system('cls')

start_1()