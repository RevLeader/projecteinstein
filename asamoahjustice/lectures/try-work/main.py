def main():
    while True:
        print("=" * 45)
        print("\n---- Welcome TO Future Leaders Accademy ----\n")
        print("1. Register")
        print("2. About the school".title())
        print("3. course Offered".title())
        print("4. payment plans".title())
        print("Exit")
        print("\n=" * 45)

        choice = input("Enter one of the options above(1-5): ")
    
        if choice == '1':
            take_input()

        elif choice == '2':
            school_info():

        elif choice == '3':
            course()

        elif choice == '4':
            payment_plans()

        elif choice == '5':
            print("\nThank you for visiting Future Leaders Accademy. Visite again later")
            break
        else:
            print("Please enter a valid choice from 1-5")


def take_input():
    try:
        name = input("Enter your name: ")
        age = int(input("Enter your age: "))
        number = float(input("Enter your number: "))
# main()