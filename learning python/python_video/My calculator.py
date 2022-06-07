
def calculator(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "^":
        return num1 ^ num2
    elif operator == "=":
        return num1 == num2
    else:
        return "Wrong operator."

print(calculator(int(input("Enter first number: ")), input("Enter operator: "), int(input("Enter second number: ")) ))