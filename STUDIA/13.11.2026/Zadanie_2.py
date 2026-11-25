

def encrypt(message, shift,):
    result = ""
    
    for index in range(len(message)):
        
        if message[index] == " ":
            result += " "
        
        else:
            char = ord(message[index])
            encrypted_char = char + int(shift)
            result += chr(encrypted_char)
    return result

def decrypt(message, shift):
    result = ""
    
    for index in range(len(message)):
        if message[index] == " ":
            result += " "
        else:
            char = ord(message[index])
            encrypted_char = char - int(shift)
            result += chr(encrypted_char)
    return result


print(encrypt("secret message", 3))

print(decrypt(encrypt("secret message", 3), 3))

