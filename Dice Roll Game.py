# • Modify the program so the user can specify how many dice they want to roll. 
# Add a feature that keeps track of how many times the user has rolled the dice 
# during the session. This will require a counter that increments each time the 
# dice are rolled.
import random

while True:
    while True:
        try:
            rolldicecount = int(input("How many dice Do you want to roll?\n: "))
        except ValueError:  
            print("Enter a Number")
            continue
        if rolldicecount > 0:
            break
        else:
            print("Enter a number greater than 0. ")
    userinput = input("Roll the dice? (y/n): ").lower().strip()
    if userinput == "y":
        for i in range(1, rolldicecount+1):
            print(f"{random.randint(1, 6+1)}, {random.randint(1, 6+1)} x {i}")
        dicerolled = 0
        dicerolled += 1
    elif userinput == "n":
        print("Thanks for playing!")
        print(f"You have rolled the dice {dicerolled} time(s).")
        break
    else:
        print("Invalid choice!")
        