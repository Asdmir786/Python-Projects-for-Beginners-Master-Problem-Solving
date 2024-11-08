# • Allow the user to specify the minimum and maximum values for the number 
# range before the game starts. This gives the player more control over the 
# difficulty level. 
# • Implement a feature that limits the number of guesses a player can make. If 
# the player runs out of attempts, the game should end, and the correct number 
# should be revealed. 
# • Add a feature that keeps track of the fewest attempts it took to guess the 
# number correctly. The program should display this "best score" at the end of 
# each game.
import random

# AI
while True:
    try:
        # Ask for minimum value
        minimum_value = int(input("Give Minimum Value (e.g., 1, 2, etc.): "))
        
        # Enter loop for maximum value only after minimum is successfully provided
        while True:
            try:
                # Ask for maximum value
                maximum_value = int(input("Give Maximum Value (e.g., 1, 2, etc.): "))
                
                # Check if maximum is greater than minimum
                if maximum_value <= minimum_value:
                    print("Bruh, Mastian kyun kr rha hai?")
                else:
                    # Valid input; exit both loops
                    break
            except ValueError:
                # Handle invalid input for maximum value only
                print("Please enter a valid number for the maximum value.")
        
        break  # Exit the outer loop when both values are valid
        
    except ValueError:
        # Handle invalid input for minimum value only
        print("Please enter a valid number for the minimum value.")


lives = 15
RandomChosenNumber = random.randint(minimum_value, maximum_value)
attempts = 0
while lives != 0: 

    while True: 
        try:
            userNumber = int(input(f"Guess The Number Between 1 and 100(live(s): {lives}): "))
            break
        except ValueError:
            print("Please enter a valid number.")
    lives -= 1
    attempts += 1
    if userNumber > RandomChosenNumber: 
        print("Too high!")
    elif userNumber < RandomChosenNumber:
        print("Too low!")
    elif userNumber == RandomChosenNumber:
        print(f"Congratulations! You guessed the number with {lives} left and in {attempts} attempts.")
        break
    else:
        print("Please enter a valid number.")
    if lives == 0:
        print(f"Lmao, You Lost even after 15 tries. The Number was {RandomChosenNumber}.")

with open("Attemps Score Counter.txt","a") as f1:
    f1.write(f"{attempts}\n")
    f1.close()
# AI
with open("Attemps Score Counter.txt","r") as f1:
    best_score = [int(line.strip()) for line in f1]
# 50% AI
main_best_score = min(best_score)

print(f"Best Attempts: {main_best_score}")
