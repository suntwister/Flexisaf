game_disp = [" " for _ in range(9)]

# printing the game display
def print_game():
    print("\n")
    for i in range(3):
        print("| " + " | ".join(game_disp[i*3:(i+1)*3]) + " |")


# we want to check for draw
def draw():
    return " " not in game_disp

# function for the winner
def winner(user):
    winning = [
        [0,1,2], [3,4,5], [6,7,8],  # for rows win
        [0,3,6], [1,4,7], [2,5,8],  # for columns win
        [0,4,8], [2,4,6]            # for diagonals win
    ]

    for win in winning:
        if all(game_disp[i] == user for i in win):
            return True
    return False

# main function

def main():
    current_player = "X"
    print("Welcome to Tic-Tac-Toe (2 players)")
    print_game()

    while True:
        try:
            move = int(input(f"Player {current_player}, choose a position (1-9): ")) - 1
            if move >= 0 and move < 9 and game_disp[move] == " ":
                game_disp[move] = current_player
                print_game()

                if winner(current_player):
                    print(f"Player {current_player} wins!")
                    break
                if draw():
                    print("It's a draw!")
                    break

                # Switch player
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1-9.")

if __name__ == "__main__":
    main()

