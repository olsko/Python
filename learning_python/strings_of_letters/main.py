from string import ascii_letters
import random
if __name__ == "__main__":
    num_letters = 1000
    num_strings = 1000
    string_list = open("string_list" + str(num_letters) + ".txt", "w")
    for i in range(num_strings):
        string = ""
        for e in range(num_letters):
            letter = random.SystemRandom().choice(ascii_letters)
            string += letter
        string_list.write(str(i + 1) + " " + string + "\n")