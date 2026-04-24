try:
    user_name = input("Enter your full name: ").capitalize()
    user_grade = int(input("Enter your grade: "))

except Exception as e:
    print(f"A wrong value was entered, please try again: {e}")

else:
    # "a" mode so grades keep adding up each run
    with open("grades.txt", "a") as file:
        file.write(f"{user_name}: {user_grade}\n")

    # Read back the whole file to see all saved grades
    with open("grades.txt", "r") as file:
        print("\n--- All Grades ---")
        print(file.read())