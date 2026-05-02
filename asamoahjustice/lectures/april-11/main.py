# n=0
# while n<7:
#     print('code everyday')
#     n+=1

#for loops

# for n in 'hello':
#     print(n)
#     print('hello')

#task1
# def print_name():

#     #taking user's name
#     name = input('Enter a name: ').strip().lower()

#     while len(name) < 7:
#         print('the name is less than 7')
#         name = input('Enter a name: ')
#     print(name)

# print_name()

#task 2
# def cal():
#     user_num = int(input('Enter a number: '))

#     while user_num % 2 == 0:
#         print('the program stops only when you enter and odd number')
#         user_num = int(input('Enter a number: '))

#     print(user_num)

# #calling the function
# cal()

#LISTS
# fruits = ['mango', 'pawpaw', 'orange', 'guava', 'apple']
# vege = list(fruits)
# fruits[2] = 'watermelon'

# # print(fruits[1:5])
# # print(fruits[-1])
# # print(fruits[len(fruits)-1])
# # print(len(fruits))

# print(fruits)
# print(vege)

items = ['carrot', 'onion', 'pixar', 'pixels', 'tomato', 'yam', 'vegetables', 'potato']

for n in items:
    print(n)