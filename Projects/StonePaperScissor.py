import random

while True:
    player = input("Enter your move (s, p, sc): ")

    choices = ['stone', 'paper', 'scissor']
    computer = random.choice(choices)

    print("Computer chose:", computer)

    if player == 's' and computer == 'paper':
        print("You lose!")

    elif player == 'p' and computer == 'paper':
        print("It's a tie!")

    elif player == 'sc' and computer == 'paper':
        print("You win!")

    elif player == 's' and computer == 'stone':
        print("It's a tie!")

    elif player == 'p' and computer == 'stone':
        print("You win!")

    elif player == 'sc' and computer == 'stone':
        print("You lose!")

    elif player == 'p' and computer == 'scissor':
        print("You win!")

    elif player == 's' and computer == 'scissor':
        print("You lose!")

    elif player == 'sc' and computer == 'scissor':
        print("It's a tie!")

    else:
        print("Invalid move!")

    print("\nGame Over!")
    retry = input("Press Enter to play again, or type q to quit: ")

    if retry.lower() == 'q':
        break