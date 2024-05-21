import random

def game():
    user_input = input("what's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    print(f'oppo: {computer}')
    if user_input == computer:
        print('Draw')
    elif (user_input == 'r' and computer == 's') or (user_input == 'p' and computer == 'r') or (user_input == 's' and computer == 'p'):
        print('You win')
    else:
        print('You lost. Play again')

game()
