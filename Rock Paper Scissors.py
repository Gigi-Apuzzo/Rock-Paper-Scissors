import random
ai = ["r","p","s"]

ai = random.choice(ai)
print("Welcome to rock paper scissors")
choice = input("Choose between 'r', 'p' or 's': ")

if choice == ai:
    print("The computer chose,", ai)
    print("Draw")

if choice == 'r' and ai == 'p':
    print("The computer chose,", ai)
    print("The computer won")

if choice == 'p' and ai == 'r':
    print("The computer chose,", ai)
    print("You win!")

if choice == 'p' and ai == 's':
    print("The computer chose,", ai)
    print("The computer won")

if choice == 's' and ai == 'p':
    print("The computer chose,", ai)
    print("You win!")

if choice == 'r' and ai == 's':
    print("The computer chose,", ai)
    print("You win!")

if choice == 's' and ai == 'r':
    print("The computer chose,", ai)
    print("The computer won")