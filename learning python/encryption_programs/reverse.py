message = "This is program to explain reverse cipher."
translated = "" #cipher text is stored in this variable
i = len(message)
print(i)
i = i - 1
print(i)
print(message[i])

while i >= 0:
   translated = translated + message[i]
   i = i - 1
print("The cipher text is : " + translated)