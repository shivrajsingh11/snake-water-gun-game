import random

print("===== Snake Water Gun Game =====")
print("s = Snake")
print("w = Water")
print("g = Gun")

computer = random.choice(['s', 'w', 'g'])
user = input("Enter your choice: ")

print("Computer chose:", computer)

if user == computer:
    print("Match Draw")

elif user == 's' and computer == 'w':
    print("You Win! Snake drinks Water")

elif user == 'w' and computer == 'g':
    print("You Win! Water drowns Gun")

elif user == 'g' and computer == 's':
    print("You Win! Gun kills Snake")

elif user == 'w' and computer == 's':
    print("Computer Wins! Snake drinks Water")

elif user == 'g' and computer == 'w':
    print("Computer Wins! Water drowns Gun")

elif user == 's' and computer == 'g':
    print("Computer Wins! Gun kills Snake")

else:
    print("Invalid Input")