name = input("What is your name? ")

print("Hello " + name, "Let's play hangman")

word = input("Enter a text to find: ")

guess = ''

turn = 10

length = len(word)
temp = 0

while turn > 0:

    char = input("\nEnter a char! ")

    if char in guess:
        print("You already said this character")
    else:
        guess = guess + char

        if char in word:
            print(char)
            for x in range(0,len(word)):
                if char == word[x]:
                    temp += 1
                    print("You found one of the characters!")

                    for i in range(0,len(word)):
                        if word[i] in guess:
                            print(word[i], end="")
                        else:
                            print("_", end="")

        else:
            print("Wrong character!")
            turn -= 1

    if temp == length:
        print("\nYou found the word")
        break

if turn == 0:
    print("You've failed!")
