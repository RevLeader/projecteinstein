import json
from constant import divider, separator
from student import confirm_userinfo, search_forstudent
from school import show_courses, show_schoolinfo, show_paymentplans

#welcome message
print(f"\n{separator}")
print("Welcome to future leaders academy.".title())
print("Please select an option below to proceed: ".title())
print(f"{separator}\n")


def main():

    while True:
        print("\nAvailable options to choose from".title())

        #available options to choose from
        options = ["register for a course", "about the school", "courses Offered", "payment plans", "search for a student", "exit"]

        for index, option in enumerate(options, start=1):
            print(f"{index}. {option.title()}")

        #taking user's choice for the above options
        user_choice = input(f"\nPlease choose an option(1-{len(options)}) from above to procede: ").strip()

        #logics for each of the above options
        if user_choice == '1':
            confirm_userinfo()

        elif user_choice == '2':
            show_schoolinfo()
            input("\nPress any key to continue: ")
        elif user_choice == '3':
            show_courses()
            input("\nPress any key to continue: ")
        elif user_choice == '4':
            print("\nThis feature is currently in development, please check back later. " \
            "Thank you")
        elif user_choice == '5':
            search_forstudent()
            input("\nPress any key to continue: ")
        elif user_choice == '6':
            print("\nThank you for visiting Future Leaders Academy. Goodbye!👋")
            input("\nPress any key to continue: ")
            break
        else:
            print("\nInvalid input. Please try again by entering  a number from 1-5")

main()