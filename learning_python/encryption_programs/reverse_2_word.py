
def rev_message(message):
    result = ""
    words = message.split(" ")
    for i in words:
        word = "".join(i)
        word = word[::-1]
        result += word + " "
    return result

if __name__ == "__main__":
    print(rev_message(input("Enter your message: ")))