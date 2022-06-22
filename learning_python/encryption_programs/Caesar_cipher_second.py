#Caesar cipher
#In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
#Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
#It is a type of substitution cipher in which each letter in the plaintext is replaced by a 
#letter some fixed number of positions down the alphabet.
#For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

#In my Caesar cipher shift number and direction can be changed.
import string
import collections

def encrypt(message, shift, direction):
    result = ""
    shift_direction = int(direction + shift)
    #declaring the alphabet and digits
    alphabet = string.ascii_letters
    alphabet_low = string.ascii_lowercase
    alphabet_up = string.ascii_uppercase
    digits = string.digits
    shifted_alphabet = collections.deque(string.ascii_letters)
    shifted_alphabet_low = collections.deque(string.ascii_lowercase)
    shifted_alphabet_up = collections.deque(string.ascii_uppercase)
    shifted_digits = collections.deque(string.digits)
    #shifting the alphabet and digits
    shifted_alphabet.rotate(shift_direction)
    shifted_alphabet_low.rotate(shift_direction)
    shifted_alphabet_up.rotate(shift_direction)
    shifted_digits.rotate(shift_direction)
    #shifting the message
    for index in range(len(message)):
        if message[index] in alphabet:
            if message[index] in alphabet_low:
                index_char_alph_low = alphabet_low.index(message[index])
                result += shifted_alphabet_low[index_char_alph_low]
            elif message[index] in alphabet_up:
                index_char_alph_up = alphabet_up.index(message[index])
                result += shifted_alphabet_up[index_char_alph_up]
        elif message[index] in digits:
            index_char_d = digits.index(message[index])
            result += shifted_digits[index_char_d]
        elif message[index] == " " :
            result += " "
    return result

            

print(encrypt(input("Enter your message: "), input("Enter amount of shifts: "), input("Enter - for right shift or enter for left shift: ")))