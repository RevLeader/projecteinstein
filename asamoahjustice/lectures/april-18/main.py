#1. division by zero
# print(10/0)

#2. wrong value type
# number = int("hello, world")

#3. list index that doesn't exist
# my_list = [1, 2, 3]
# print(my_list[10])

#4. variable that doesn't exist
# print(ghost_variable)

#using try and except to handle errors
# try: 
#     number = int(input("Enter a number: "))
#     result = 10 / number

# #can use Exception to catch any errors if unsure of the error type
# except Exception as e:
#     print("⚒️ You can't divide by zero!")

# except ValueError:
#     print("⚒️ That's not a valid number!")

# #adding else and finally
# else:
#     print(f"Success! Result is {result}")

# finally:
#     print("This always runs no matter what.")

#PART 3
#creating the file with open
# with open("my_notes.txt", "w") as file:
#     file.write("Python is awesome\n")
#     file.write("I am learning exceptions\n")
#     file.write("Files are cool\n")

# print("File created!")

# reading the file back
# with open("my_notes.txt", "r") as file:
#     content = file.read()
#     print(content)

# with open("my_notes.txt", "r") as file:
#     for line in file:
#         print(line.strip())

# #read line by line
# with open("my_notes.txt", "r") as file:
#     for a in file:
#         print(a.strip()) #.strip removes the extra newline

# line = "Python is awesome\n"  # simulate a line from a file

# print("Without strip:")
# print(repr(line))        # repr() shows hidden characters

# print("With strip:")
# print(repr(line.strip()))

#PART 4
#append(add to the file without deleting it)
# with open("my_notes.txt", "a") as file:
#     file.write("Appending a new line!\n")

# # print("line added!")

# with open("my_notes.txt", "r") as file:
#     content = file.read()
#     print(content.strip())

#PART 5: Putting it all together
# try:
#     with open("my_notes.txt", "r") as file:
#         print(file.read())
# except Exception as e:
#     print(f"Something went wrong: {e}")