import random

print("Welcome to the number guessing game.")
a = int(input("Write the first number of your range. \n >> "))
b = int(input("Write the last number of your range. \n >> "))
print("This is player1 chance.")
print("Guess your number.")
#print(number)
number = random.choice(range(a, b))
number_of_chances = 0
number_of_chance = 0
while True:
    p1 = int(input(">> "))
    if p1 > number:
        print("You entered a big number. Please enter a small number.")
        number_of_chances += 1
        continue
    elif p1 < number:
        print("You entered a small number. Please enter a greater.")
        number_of_chances += 1
        continue
    else:
        print("You guess it right.")
        number_of_chances += 1
        break

print("Player2 turn now.")
a = int(input("Write the first number of your range. \n >> "))
b = int(input("Write the last number of your range. \n >> "))
numbers = random.choice(range(a, b))
print(numbers)
while  True:
    p2 = int(input(">> "))
    if p2 > numbers:
        print("You entered greater number. Please enter a small number.")
        number_of_chance += 1
        continue
    elif p2 < numbers:
        print("You entered a small number. Please enter a greater number.")
        number_of_chance += 1
        continue
    else:
        print("You guess it right.")
        number_of_chance += 1
        break

if number_of_chance < number_of_chances:
    print("Player2 won. Player1 lost.")
elif number_of_chances < number_of_chance:
    print("Player1 won. Player2 lost.")
else:
    print("There is a tie between player1 and player2.")

print(f"Player1 won {number_of_chances} and Player2 won {number_of_chance}")