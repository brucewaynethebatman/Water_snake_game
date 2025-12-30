'''snake = 1
water = -1
gun = 0'''

import random
computer = random.choice([1,-1,0])
Your_choice = input("Enter your choice: ")
option_dic = {"s": 1, "w": -1, "g":0}

choice = option_dic[Your_choice]

reverseDict = {1:"snake", -1:"water", 0:"gun"}

print(f"Your choice: {reverseDict[choice]}\nComputer choose: {reverseDict[computer]}")

if computer == choice:
    print("Match Draw!")

else: 
    if computer == 1 and choice == -1:
        print("Computer Won!")
    elif computer == 1 and choice == 0:
        print("You Won!")
    elif computer == -1 and choice == 1:
        print("Computer Won!")
    elif computer == -1 and choice == 0:                        #snake = 1, water = -1, gun = 0                            
        print("You Won!")
    elif computer == 0 and choice == 1:
        print("Computer Won!")
    elif computer == 0 and choice == -1:
        print("You Won!")
    else:
        print("something went wrong!")






