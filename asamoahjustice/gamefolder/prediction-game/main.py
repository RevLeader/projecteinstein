import random

numbers = list(range(1, 21))

def main():

    #giving the use a clue of what the game is about
    print("This is the Guessing Game🤷, the second player(the computer) chooses a random number between 1-20(inclusive)"
    "and if you guess right, you win, else the computer wins. Good luck!🫡\n")
    
    #using indefinite loop to keep the program running unless told otherwise
    while True:

        #calling made choice function
        computer_choice = made_choice(numbers)

        #taking user's choice
        user_choice = input(f"Enter any of these values {numbers} or type stop or exit to close the program: \n")

        #checking if the user typed stop or exit
        if user_choice == "stop" or user_choice == "exit":
            break #stopping the loop if user types stop or exit
        
        else:
            user_choice2 = int(user_choice)

        #calling check function
        check_call = check(numbers, user_choice2)


        print(f"Computer chose: {computer_choice} and you chose {user_choice2}\n")

        results = resulter(user_choice, computer_choice)
        print(f"{results}\n")


#a function for looping if wrong value if entered
def check(numbers, user_choice2):
    while user_choice2 not in numbers:
        user_choice2 = int(input(f"Please enter a valid input in one of these: {numbers}: "))
    
    return user_choice2

#fucntion for making computer's choice
def made_choice(numbers):
   return random.choice(numbers)

    
#function for checking who won
def resulter(user_choice2, computer_choice):
    if user_choice2 == computer_choice:
        return "you won!"
    else:
        return "computer won!"
    
#calling the main function
main()