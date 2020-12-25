name = input("Please enter your name! ")
lastName = input("Please enter your lastname! ")
age = int(input("Please enter your age! "))
birthYear = int(input("Please enter your date of birth! "))

list1 = [name, lastName, age, birthYear]    # Or I can append with list1.append(...)

for i in list1:
    print(i)

if 0 < age < 18:
    print("You can't go out because it's too dangerous.")
elif age >= 18:
    print("You can go out the street.")
else:
    print("Wrong value for age!")
