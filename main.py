print("Welcome to Rock, Paper and Scissors game. \nR represents 'rock'\nP represents 'paper'\nS represents 'scissors'.")

from operator import truediv
import random

while True:

    game_choices = ['R', 'P', 'S']
    computer = random.choice(game_choices)
    player = None

    while player not in game_choices:
        player = input('Rock, Paper or Scissors: ').upper()

    if player == computer:
        print('Computer: ',computer)
        print('Player: ',player)
        print('It is a tie.')
    elif player == 'R':
        if computer == 'S':
            print('Computer: ',computer)
            print('Player: ',player)
            print('YOU WIN!')
        elif computer == 'P':
            print('Computer: ',computer)
            print('Player: ',player)
            print('YOU LOSE')
    elif player == 'P':
        if computer == 'R':
            print('Computer: ',computer)
            print('Player: ',player)
            print('YOU WIN')
        elif computer == 'S':
            print('Computer: ',computer)
            print('Player: ',player)
            print('YOU LOSE')
    elif player == 'S':
        if computer == 'P':
            print('Computer: ',computer)
            print('Player: ',player)
            print('YOU WIN')
        elif computer == 'R':
            print('Computer: ',computer)
            print('Player: ',player)
            print('YOU LOSE')


    play_again = input("Do you want to play again? \nPlease input Y for 'yes',\nPlease input N for 'no': ").capitalize()

    if play_again == 'N':
        break
print('Thanks for playing, Bye!')
