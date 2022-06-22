secret_word = "giraffe"
guess = ""
tries = 3

while guess != secret_word and tries != 0:
    print("You have " + str(tries) + " tries left.")
    guess = input("Enter a secret word: ")
    tries -= 1
    if guess == secret_word:
        print("You win!")
    elif tries == 0:
        print("You lose")
