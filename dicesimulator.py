import random

number_of_dice=int(input("How many dice do you want to roll? "))
dice_rolls=[0]*number_of_dice
for i in range(0,number_of_dice):
    #print(i)
    dice_rolls[i]=random.randint(1,6)
print(dice_rolls)
