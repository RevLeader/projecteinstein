#task 2
#name of user
# name = input('Enter your name: ')

# return(f'hello {name}')

#task 3
# taking input
# name = input('Enter your name: ').upper()

# return(f'Hello {name}')

#task 4
#taking users name in a function
# def call_name():
#     first_name = input("Enter your first name: ")
#     return {first_name}

#     last_name = input("Enter your last name: ")
#     return {last_name}
    

# #calling the function
# call_name()

#task 5
#weeks of the week
# week_days = 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'

# #creating the function for input collection
# def condition():
#     user_input = input('Enter a day of the week: ').lower().strip()

#     #checking for monday
#     if user_input == 'monday':
#         return f'today is {user_input}'
    
#     #checking for tuesday
#     elif user_input == 'tuesday':
#         return f'today is {user_input}'
    
#     elif user_input == 'wednesday':
#         return f'today is {user_input}'

#     elif user_input == 'thursday':
#         return f'today is {user_input}'

#     elif user_input == 'friday':
#         return f'today is {user_input}'

#     elif user_input == 'saturday':
#         return f'today is {user_input}'

#     elif user_input == 'sunday':
#         return f'today is {user_input}'

#     else:
#         return f'the day entered is not in {week_days}'
# print(condition())


#task 6 (building a calculator)
#using while loop to make the program run until told to stop

# def calculate():

#     while True:

#         c = input('Enter a mathematical operation or stop or end to close the program: ').strip().lower()

#         if c == 'stop' or c == 'end':
#             break #this stops the loop if the user types in stop or end

#         #taking inputs from the user
#         a = float(input('Enter a number: '))
#         b = float(input('Enter another number: '))

#         if c == 'add' or c == '+':
#             result =  a + b
#             print(f'the results of the operation is: {result}\n') 

#         elif c == 'sub' or c == '-':
#             print(f'the results of the operation is: {a} - {b}\n') 
        
#         elif c == 'div' or c == '/':
#             print(f'the results of the operation is: {a} / {b}\n') 
        
#         elif c == 'mult' or c == '*':
#             print(f'the results of the operation is: {a} * {b}\n') 
        
#         else:
#             print('please enter either add, sub, div, or mult\n') 

        
        

    
#calling the function 
# calculate()

#task 7
# n = 0
# while n < 7:
#     print(n)
#     n += 1

#function calling meow five times
# def calling():
#     call = 0
#     while call < 5:
#         print('meow')
#         call += 1
# calling()

import calendar
call = calendar.TextCalendar()
print(call.pryear(2026))

input("Press Enter to exit...")