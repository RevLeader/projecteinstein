from constant import divider, separator
import json

#function for taking user's info
def get_user_info():
    
    #defining items to loop through
    fields = ["name", "age", "contact", "location"]
    user_data = {} #initializin it so to store the info in it later

    print()
    #looping through the list
    for field in fields:
        while True:
            value = input(f"Enter your {field}: ").strip() #taking input for each field

            if field in ("name", "location"):
                value = value.upper()

            #if user types only spaces and not a value
            if not value:
                print(f"\n{field.capitalize()} cannot be empty, try again!")
                continue

            if field == "age":
                try:
                    value = int(value)
                except ValueError:
                    print("\nAge must be a number!")
                    continue

            if field == "name":
                #checking if naqme has already has already been registered or not
                try:
                    with open("school_system.json", "r") as file:
                        all_students = json.load(file)

                except FileNotFoundError:
                    all_students = []

                found = False
                for student in all_students:
                    if sorted(value.split()) == sorted(student["name"].split()):
                        found = True
                        break

                if found:
                    print("\nStudent already registered!")
                    print("Do you still wish to continue? If it was you who has registered earlier, type NO, otherwise type YES\n")

                    restart = False
                    while True:
                        choice = input("Enter YES/NO: ").upper()

                        if choice == "NO" or choice == "N":
                            restart = True
                            break

                        elif choice == "YES" or choice == "Y":
                            print("Name registered\n")
                            break

                        else:
                            print("Invalid input, try again!")

                    if restart:
                        continue

                #checking if name is less than one word
                if len(value.split()) < 2:
                    print("\nPlease enter your full name!")
                    continue
            if field == "contact":
                #checking if the contact entered is actually all numbers
                if not value.isdigit():
                    print("\nNumber must be an interger(0-9)")
                    continue

                    #checking if the entered number starts with 0
                if not value.startswith("0"):
                    print("\nNumber must start with 0")
                    continue
                
                #checking if number is not less or more than 10
                if len(value) != 10:
                    print("\nNumber must be exactly 10 digits")
                    continue

            user_data[field] = value
            break #done with this field, move to the next
    return user_data #returning user_data after successful entering


#function for confirming user's info
def confirm_userinfo():
    user_data = get_user_info()

    if user_data is None:
        return

    try:
        with open("school_system.json", "r") as file:
            all_students = json.load(file)
    except FileNotFoundError:
        all_students = []

    # display for review
    print("\n")
    print(f"{'-' * 4} Here are your details. Please Review {'-' * 5}")
    print(f"{divider}")
    print(f"Name:     {user_data['name']}")
    print(f"Age:      {user_data['age']}")
    print(f"Contact:  {user_data['contact']}")
    print(f"Location: {user_data['location']}")
    print(divider)

    confirmation_list = ["confirm", "edit", "cancel"]
    print("\n")
    for index, proceed in enumerate(confirmation_list, start=1):
        print(f"{index}. {proceed.capitalize()}")

    confirmation = input(f"\nPlease choose an option (1-{len(confirmation_list)}) to proceed: ")

    if confirmation == '1':
        all_students.append(user_data)  # save the student
        with open("school_system.json", "w") as file:
            json.dump(all_students, file, indent=4)
        print("Congratulations 🎉🎊! Your registration was successful.")

    elif confirmation == '2':
        result = edit_studentinfo(user_data)

        if result is None: 
            confirm_userinfo()  #user chose retype all info
        else:
            all_students.append(user_data)
            with open("school_system.json", "w") as file:
                json.dump(all_students, file, indent=4)
            print("Congratulations! Your registration was successful.🎊")


    else:
        return

#function for editing student info
def edit_studentinfo(user_data):
    
    #options the user can choose from to edit
    fields = ["name", "age", "contact", "location"]
    fields2 = ["done editing", "retype all information"] #the rest of the options from fields
    conlen = len(fields) + 1 #a variable determing the lenght of fields so next options get the next number right

    while True:
        try:
            print()
            for index, data in enumerate(fields, start=1):
                print(f"{index}. {data.capitalize()}")
            
            for index, data in enumerate(fields2, start=conlen):
                print(f"{index}. {data.capitalize()}")
            print("\n")

            #user choosing what to edit
            choice = int(input(f"Choose one of the above options(1-{conlen + 1}) you would like to edit" \
                            " to continue: "))
            if choice == conlen:
                return user_data #exits the function with success
            
            elif choice == conlen + 1:
                return None
            
            elif 1 <= choice <= len(fields):
                chosen_field = fields[choice - 1]

                if chosen_field == 'age':
                    user_data[chosen_field] = int(input(f"Enter new {chosen_field}: "))
                else:
                    user_data[chosen_field] = input(f"Enter new {chosen_field}: ").upper()

                print("\n")
                print(f"{'-' * 4} Here are your details. Please Review {'-' * 5}")
                print(f"{divider}")
                print(f"Name:     {user_data['name']}")
                print(f"Age:      {user_data['age']}")
                print(f"Contact:  {user_data['contact']}")
                print(f"Location: {user_data['location']}")
                print(divider)

            else:
                print("\nInvalid input. Please try again!")
        except Exception as e:
            print(e)



#function for searching for a student
def search_forstudent():
    search = input("Please enter full name of student(eg, Kofi): ").upper()

    try:
        #reading all the students info to search from
        with open("school_system.json", "r") as file:
            all_students = json.load(file)

        #assuming no student has been found
        found = False

        #looping through all students
        for student in all_students:
            #using in not == specifically so that you can type the 1st three letters and can get
            #a match if you don't remember the whole name
            if search in student['name']:
                found = True
                print()
                print("Student Found! Here are the details:")
                print(f"Name:       {student['name']}")
                print(f"Location:   {student['location']}")

        #this runs only if no student is found 'cause if a student is found, the found 
        #inside  the if statement will be true and when it gets here, not makes it false so it does't run
        if not found:
            print("No student found with that name. Please try again")

    except FileNotFoundError:
        print("\nOoops 🙊. No student registered yet! Try again later")
    
    except Exception as e:
        print(e)
        