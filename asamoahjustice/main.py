import random

#creating the function
def main():

    #defining various states
    state = ['rock', 'papper', 'scissors']

    #taking user_input
    user_input = input('Enter a valid input from the list state: ')

    #calling the function take_userinput() in main() and assigning it to human
    human = take_userinput(user_input, state)

    #calling make_computer_choice(state) and storing it in computer_choice
    computer_choice = make_computer_choice(state)

    #printing computer choice
    print(computer_choice)

    #calling the check_result
    winner = check_result(computer_choice, user_input)
    print(winner)

def take_userinput(user_input, state):
    while user_input not in state:
        user_input = input('Enter a valid choice(rock, paper or scissors): ')
    return user_input

#a function taking and storing computer's choice
def make_computer_choice(state):

    #usign random to generate computer's choice based on lists in state
    computer_choice = random.choice(state)

    #returning computer_choice
    return computer_choice

#checking computer choice and human choice
def check_result(computer_choice, user_input):

    #checking conditions

    if computer_choice == 'scissors' and user_input == 'papper':
        return 'computer won'
    elif computer_choice=='papper' and user_input=='scissors':
        return 'you won'

    elif computer_choice == 'rock' and user_input == 'scissors':
        return 'computer won'
    elif computer_choice=='scissors' and user_input=='rock':
        return 'you won'

    elif computer_choice == 'rock' and user_input == 'papper':
        return 'you won'
    elif computer_choice=='papper' and user_input=='rock':
        return 'computer won'

    else:
        return 'it a  tie'
main()