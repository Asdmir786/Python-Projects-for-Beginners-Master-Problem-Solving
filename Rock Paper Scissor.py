# • Modify the game so that the first player (or computer) to win two out of three 
# rounds is declared the overall winner. This adds a competitive aspect to the 
# game. 

# • Keep a tally of how many times the player wins, loses, or ties with the 
# computer. Display these statistics at the end of the game. 

# • Add an option for two players to play against each other, taking turns to input 
# their choices. The program should then determine the winner based on their 
# inputs.
rock = chr(0x270A)      # ✊
paper = chr(0x270B)     # ✋
scissors = chr(0x270C)  # ✌

import random
import time

# ========= Experimental =========
from playsound3 import playsound
from soundplay import playsound





rpc = {"r","p","s"}
rounds = 1
PlayerPoints = 0
ComputerPoints = 0
DrawPoints = 0

def win():
    global PlayerPoints
    PlayerPoints += 1
    print("You Win!")
def lose():
    global ComputerPoints
    ComputerPoints += 1
    print("You Lose!")
def draw():
    global DrawPoints
    DrawPoints += 1
    print("Draw!")
def TellRoundNumber():
    global rounds
    print(f"Round No. {rounds}.")
def Logic(userChoice,compChoice):
     # All Draw Scenarios
        if userChoice == "r" and compChoice == "r":
            print(f"You chose {rock}")
            print(f"Computer chose {rock}")
            draw()
        elif userChoice == "p" and compChoice == "p":
            print(f"You chose {paper}")
            print(f"Computer chose {paper}")
            draw()
        elif userChoice == "s" and compChoice == "s":
            print(f"You chose {scissors}")
            print(f"Computer chose {scissors}")
            draw()
        # All Win Scenarios For Player
        elif userChoice == "r" and compChoice == "s":
            print(f"You chose {rock}")
            print(f"Computer chose {scissors}")
            win()
        elif userChoice == "p" and compChoice == "r":
            print(f"You chose {paper}")
            print(f"Computer chose {rock}")
            win()
        elif userChoice == "s" and compChoice == "p":
            print(f"You chose {scissors}")
            print(f"Computer chose {paper}")
            win()
        # All Lose Scenarios For Player
        elif userChoice == "r" and compChoice == "p":
            print(f"You chose {rock}")
            print(f"Computer chose {paper}")
            lose()
        elif userChoice == "p" and compChoice == "s":
            print(f"You chose {paper}")
            print(f"Computer chose {scissors}")
            lose()
        elif userChoice == "s" and compChoice == "r":
            print(f"You chose {scissors}")
            print(f"Computer chose {rock}")
            lose()
        else:
            print("Enter r,p or s not BS!")
            return

def SinglePlayerRPC():
    global rounds

    while True:
        TellRoundNumber()
        userChoice = input("Rock, paper, scissors? (r/p/s): ")
        compChoice = random.choice(rpc)

        Logic(userChoice,compChoice)
        while rounds != 3:
            ContinueOrNot = input(f"Continue? (Round No.{rounds}) (y/n): ").lower().strip()
            if ContinueOrNot == "y":
                rounds += 1
                break
            elif ContinueOrNot == "n":
                exit()
            else:
                print("Enter Either y or n.")
        else:
            if PlayerPoints > ComputerPoints:
                print(f"In 3 Rounds You have won {PlayerPoints} Rounds and the Computer has won only {ComputerPoints} Rounds (Draws: {DrawPoints}), so, you WIN. GYATT DAIYMM")
                # Play sound asynchronously
                playsound(r'c:\Users\Asmir Alam\Desktop\rizz-sounds.mp3')
            elif ComputerPoints > PlayerPoints:
                print(f"In 3 Rounds You have won only {PlayerPoints} Rounds and the Computer has won {ComputerPoints} Rounds (Draws: {DrawPoints}), so, you LOSE. NOT GYATT DAIYMM")
                # Play sound asynchronously
                playsound(r'c:\Users\Asmir Alam\Desktop\sad violin.mp3')
            elif PlayerPoints == ComputerPoints:
                print(f"In 3 Rounds You have won only {PlayerPoints} Rounds and the Computer has won {ComputerPoints} Rounds (Draws: {DrawPoints}), so, IT'S A BLOOODY DRAW.GYYYYYAAAAAAATTTTTTTTT DAIYMM")  
                # Play sound asynchronously
                playsound(r'c:\Users\Asmir Alam\Desktop\juice-pilado.mp3')
            time.sleep(20)
            break

def CO_OP_RPC():

    # Variables
    playerTurn = ["Player 1","Player 2"]
    
    print(f"{playerTurn[0]}'s Turn:")

    while True:
        choices = ["r","p","s"]
        player1Choice = input("Rock, paper, scissors? (r/p/s): ").strip().lower()
        if player1Choice not in choices:
            print("Try Again, Only Input should be 'r','p', or 's'")
        else:
            break

    print(f"{playerTurn[1]}'s Turn:")

    while True:
        player2Choice = input("Rock, paper, scissors? (r/p/s): ").strip().lower()
        if player2Choice not in choices:
            print("Try Again, Only Input should be 'r','p', or 's'")
        else:
            break

    # Player 1 Win Scenarios
    if player1Choice == "r" and player2Choice == "s":
        print(f"{playerTurn[0]} chose {rock}.")
        print(f"{playerTurn[1]} chose {scissors}.")
        print(f"{playerTurn[0]} Wins.")
    elif player1Choice == "p" and player2Choice == "r":
        print(f"{playerTurn[0]} chose {paper}.")
        print(f"{playerTurn[1]} chose {rock}.")
        print(f"{playerTurn[0]} Wins.")
    elif player1Choice == "s" and player2Choice == "p":
        print(f"{playerTurn[0]} chose {scissors}.")
        print(f"{playerTurn[1]} chose {paper}.")
        print(f"{playerTurn[0]} Wins.")
    # Player 2 Win Scenarios
    elif player2Choice == "r" and player1Choice == "s":
        print(f"{playerTurn[0]} chose {scissors}.")
        print(f"{playerTurn[1]} chose {rock}.")
        print(f"{playerTurn[1]} Wins.")
    elif player2Choice == "p" and player1Choice == "r":
        print(f"{playerTurn[0]} chose {rock}.")
        print(f"{playerTurn[1]} chose {paper}.")
        print(f"{playerTurn[1]} Wins.")
    elif player2Choice == "s" and player1Choice == "p":
        print(f"{playerTurn[0]} chose {paper}.")
        print(f"{playerTurn[1]} chose {scissors}.")
        print(f"{playerTurn[1]} Wins.")
    # Draw Scenarios
    elif player1Choice == "r" and player2Choice == "r":
        print(f"{playerTurn[0]} chose {rock}.")
        print(f"{playerTurn[1]} chose {rock}.")
        print(f"Draw!")
    elif player1Choice == "p" and player2Choice == "p":
        print(f"{playerTurn[0]} chose {paper}.")
        print(f"{playerTurn[1]} chose {paper}.")
        print(f"Draw!")
    elif player1Choice == "s" and player2Choice == "s":
        print(f"{playerTurn[0]} chose {scissors}.")
        print(f"{playerTurn[1]} chose {scissors}.")
        print(f"Draw!")

    while True:
        wantsToContinueChoices = ['y','n']
        wantsToContinue = input("Do You want to Continue or not? (y/n): ").lower().strip()
        if wantsToContinue not in wantsToContinueChoices:
            continue
        else:
            break
    if wantsToContinue == "y":
        CO_OP_RPC()
    elif wantsToContinue == "n":
        return
    

print("Welcome to Rock Paper Scissor Game.")

while True:
    SGorCOOP = input("What do you want to play?\n1. Single Player\n2. Player vs Player? (sg/coop)\n: ").lower().strip()
    if SGorCOOP == "sg" or SGorCOOP == "coop":
        break
    else:
        continue

if SGorCOOP == "sg":
    SinglePlayerRPC()
elif SGorCOOP == "coop":
    CO_OP_RPC()