# Giraffe langauge
# vowels -> g
# ----------------
# dog -> dgg
# cat -> cgt

def translate(message):
    vowels = "aeiou"
    translation = ""
    for letter in message:
        if letter.lower() in vowels:
            if letter.isupper():
                translation += "G"
            else:
                translation += "g"
        else:
            translation += letter
    return translation
print(translate(input("Enter a message to translate: ")))