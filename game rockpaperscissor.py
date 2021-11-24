import random

my_wins = 0
your_wins = 0

def Choose_Option():
    user_choice = input("LETS PLAY-Choose Rock, Paper or Scissors: ")
    if user_choice in ["Rock", "rock", "r", "R"]:
        user_choice = "r"
    elif user_choice in ["Paper", "paper", "p", "P"]:
        user_choice = "p"
    elif user_choice in ["Scissors", "scissors", "s", "S"]:
        user_choice = "s"
    else:
        print("LETS PLAY FAIR THATS INVALID ")
        Choose_Option()
    return user_choice
 
def Computer_Option():
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2:
        comp_choice = "p"
    else:
        comp_choice = "s"
    return comp_choice


while True:
  
    
    user_choice = Choose_Option()
    comp_choice = Computer_Option()

  
    
    if user_choice == "r":
        if comp_choice == "r":
            print("You chose rock. I chose rock. Lets dismiss the round.")
        
        elif comp_choice == "p":
            print("You chose rock.I chose paper. You lose.")
            my_wins += 1
            
        elif comp_choice == "s":
            print("You chose rock. I chose scissors. You win.")
            your_wins += 1

    elif user_choice == "p":
        if comp_choice == "r":
            print("You chose paper.I chose rock. You win.")
            your_wins += 1
        
        elif comp_choice == "p":
            print("You chose paper.I chose paper. Lets dismiss the round.")
            
            
        elif comp_choice == "s":
            print("You chose paper. I chose scissors. You lose.")
            my_wins += 1

    elif user_choice == "s":
        if comp_choice == "r":
            print("You chose scissors. I chose rock. You lose.")
            my_wins += 1
        
        elif comp_choice == "p":
            print("You chose scissors.I chose paper. You win.")
            your_wins += 1
            
        elif comp_choice == "s":
            print("You chose scissors. I chose scissors. Lets dismiss the round.")

  
    print("Your wins: " + str(your_wins))
    print("My wins: " + str(my_wins))
    
    
    user_choice = input("Do you want to play again? (y/n)")
    if user_choice in ["Y", "y", "yes", "Yes"]:
        pass
    elif user_choice in ["N", "n", "no", "No"]:
        break
    else:
        break
