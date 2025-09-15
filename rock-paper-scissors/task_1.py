import random
print("==" * 20)
print("Welcome to the Rock Paper Scissors game")
print("==" * 20)
def main():
    choice = {
    "choices": ["rock", "paper", "scissors"],
    "choice_no": [1,2,3]
    }   
    while True:
        # collecting user game choice
        print("Enter 1 to pick \"Rock\"")
        print("Enter 2 to pick \"Paper\"")
        print("Enter 3 to pick \"Scissors\"")
        print("--" * 10)
        user_game = int(input("Enter your choice: "))
        comp_game = int(random.choice(choice["choice_no"]))

        # user and computer choice output
        print(f"Your choice is {choice['choices'][user_game - 1]}")
        print("--" * 10)
        print(f"Computer choice is {choice['choices'][comp_game - 1]}")
        print("--" * 10)
        
        # conditions
        if user_game not in choice["choice_no"]:
            print("Invalid choice, try again")
            continue
        
        elif user_game ==  comp_game:
            print("The game is a tie, try again")
            
        elif (user_game == 1 and comp_game == 3) or \
            (user_game == 2 and comp_game == 1) or \
            (user_game == 3 and comp_game == 2):
            print("Congratulations you won!")
            print("--" * 10)
            
        else:
            print("Computer wins, try again")
        
        # exit the game
        exit_game = int(input("Enter 1 to quit the game or 2 to continue: "))
        if exit_game == 1:
            print("Thank you for playing the game!")
            break
        continue


main()