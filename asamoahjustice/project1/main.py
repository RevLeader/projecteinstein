
def main():
    while True:
        print("=" * 45)
        print("  Welcome to Future Leaders Academy")
        print("=" * 45)
        print("1. Register")
        print("2. About the School")
        print("3. Courses Offered")
        print("4. Payment Plans")
        print("5. Exit")
        print("=" * 45)

        choice = input("Enter your choice (1-5): ").strip()

        # checking what the user picked and calling the right function
        if choice == "1":
            take_input()
        elif choice == "2":
            school_info()
        elif choice == "3":
            courses()
        elif choice == "4":
            payment_plans()
        elif choice == "5":
            print("\nThank you for visiting Future Leaders Academy. Goodbye!")
            break
        else:
            print("\nInvalid choice. Please enter a number from 1 to 5.\n")


# this function handles student registration
def take_input():
    print("\n--- Student Registration ---\n")

    try:
        user_name = input("Enter your full name: ").upper().strip()
        user_age = int(input("Enter your age: "))
        user_contact = int(input("Enter your contact: "))
        user_email = input("Enter your email: ")
        user_fees = float(input("Enter your fees (GHS): "))
        user_location = input("Enter your location: ").upper().strip()

    except Exception as e:
        # if the user enters something wrong, show the error and don't crash
        print(f"\nAn error occurred: {e}. Please try again.\n")

    else:
        # save the details to a file then read and display them
        with open("school_system.txt", "w") as file:
            file.write(
                f"Name: {user_name}\n"
                f"Age: {user_age}\n"
                f"Contact: {user_contact}\n"
                f"Email: {user_email}\n"
                f"Fees: GHS{user_fees}\n"
                f"Location: {user_location}\n\n"
            )

        print("\n--- Congratulations! Here are your details. Confirm ---\n")
        with open("school_system.txt", "r") as file:
            print(file.read())


# basic info about the school
def school_info():
    print("\n--- About Future Leaders Academy ---\n")
    print("Future Leaders Academy is a top-tier institution dedicated")
    print("to providing quality education to students across Ghana.")
    print()
    print("Location  : Kumasi, Ashanti Region")
    print("Phone     : +233 24 000 0000")
    print("Email     : info@futureleaders.edu.gh")
    print("Hours     : Mon - Fri, 8:00am to 5:00pm")
    print()


def courses():
    print("\n--- Courses Offered ---\n")

    # each item is the course name and how long it takes
    course_list = [
        ("Software Engineering",       "2 Years"),
        ("Business Administration",    "3 Years"),
        ("Graphic Design",             "1 Year"),
        ("Data Science",               "2 Years"),
        ("Networking & Cybersecurity", "2 Years"),
    ]

    print(f"{'#':<5} {'Course':<30} {'Duration'}")
    print("-" * 45)

    # loop through the list and number each course
    for i, (course, duration) in enumerate(course_list, start=1):
        print(f"{i:<5} {course:<30} {duration}")
    print()


def payment_plans():
    print("\n--- Payment Plans ---\n")

    # storing each plan as a tuple: name, amount, and a short note
    plans = [
        ("Full Payment",    "GHS 5,000", "5% discount applied"),
        ("Termly Payment",  "GHS 1,800", "Per term, 3 terms a year"),
        ("Monthly Payment", "GHS 650",   "Per month, spread across 12 months"),
    ]

    for plan, amount, note in plans:
        print(f"  Plan   : {plan}")
        print(f"  Amount : {amount}")
        print(f"  Note   : {note}")
        print()


main()
