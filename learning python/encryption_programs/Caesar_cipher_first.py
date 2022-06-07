#Caesar cipher
#In cryptography, a Caesar cipher, also known as Caesar's cipher, the shift cipher, 
#Caesar's code or Caesar shift, is one of the simplest and most widely known encryption techniques.
#It is a type of substitution cipher in which each letter in the plaintext is replaced by a 
#letter some fixed number of positions down the alphabet.
#For example, with a left shift of 3, D would be replaced by A, E would become B, and so on.

#My Caesar cipher will have right shift of 5.

alphabet = {
        "A": "F",
        "B": "G",
        "C": "H",
        "D": "I",
        "E": "J",
        "F": "K",
        "G": "L",
        "H": "M",
        "I": "N",
        "J": "O",
        "K": "P",
        "L": "Q",
        "M": "R",
        "N": "S",
        "O": "T",
        "P": "U",
        "Q": "V",
        "R": "W",
        "S": "X",
        "T": "Y",
        "U": "Z",
        "V": "A",
        "W": "B",
        "X": "C",
        "Y": "D",
        "Z": "E",
        " ": " ",
        "a": "f",
        "b": "g",
        "c": "h",
        "d": "i",
        "e": "j",
        "f": "k",
        "g": "l",
        "h": "m",
        "i": "n",
        "j": "o",
        "k": "p",
        "l": "q",
        "m": "r",
        "n": "s",
        "o": "t",
        "p": "u",
        "q": "v",
        "r": "w",
        "s": "x",
        "t": "y",
        "u": "z",
        "v": "a",
        "w": "b",
        "x": "c",
        "y": "d",
        "z": "e",
}

message = input("Enter a message to cypher: ")
cypher = ""

for letter in range(len(message)):
    cypher = cypher + alphabet[message[letter]]


print(cypher)