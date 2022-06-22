message = "This is a reverse cipher."
result = "" 
i = len(message) - 1

while i >= 0:
   result += message[i]
   i -= 1
print("The cipher text is : " + result)