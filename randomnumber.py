import random

print("Guessing Game")
lower_number=int(input("Enter the starting range: "))
higher_number=int(input("Enter the ending range: "))
random_int=random.randint(lower_number,higher_number)
number_to_be_guessed=input(f"Enter a number between {lower_number} and {higher_number}: ")
if(number_to_be_guessed==random_int):
    print("You have guessed the number correctly")
else:
    print("You have not guessed the number correctly")

