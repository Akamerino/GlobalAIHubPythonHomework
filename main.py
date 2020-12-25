name = input("What is your name? ")

print("Hello " + name, "Let's play hangman")

word = input("Enter a text to find: ")

guess = ''

turn = 10

length = len(word)
temp = 0

while turn > 0:

    char = input("Enter a char! ")

    if char in guess:
        print("You already said this character")
    else:
        guess = guess + char

        if char in word:
            print(char)
            for x in range(0,len(word)):
                if char == word[x]:
                    temp += 1
        else:
            print("Wrong character!")
            turn -= 1

    if temp == length:
        print("You found the word")
        break

if turn == 0:
    print("You've failed!")