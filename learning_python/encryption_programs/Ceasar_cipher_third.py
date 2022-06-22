#Caesar cipher
#In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
#Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
#It is a type of substitution cipher in which each letter in the plaintext is replaced by a 
#letter some fixed number of positions down the alphabet.
#For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

#This time I will use unicode codes.
import os
from time import sleep

def start_2(option_choosed):
    if option_choosed == "1":
        print("Exited")
        sleep(2)
        clear()
    elif option_choosed == "2":
        clear()
        print(encrypt(input("Enter your message: "), input("Enter amount of shifts: "), input("Enter - for right shift or + for left shift: ")))
        print(input(""))
        clear()
        return start_1()
    else:
        print("You must choose between 1 or 2")
        print(input(""))
        clear()
        return start_1()


def encrypt(message, shift, direction):
    result = ""
    for index in range(len(message)):
        char = ord(message[index])
        if direction == "right" or "+":
            encrypted_char = char + int(shift)
        else:
            encrypted_char = char - int(shift)
        encrypted_char = chr(encrypted_char)
        result += encrypted_char
    return result

def start_1():
    options = ["Exit", "Encryption"]
    for i in range(len(options)):
        print(str(i+1) + ":", options[i])
    start_2(input("Enter a number: "))

clear = lambda: os.system('cls')

start_1()


