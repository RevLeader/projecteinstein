# def main():
#    student_info = take_input()

# #function for taking input
# def take_input():
     
#     print("Hello, Welcome to Future Leaders Accademy. Pleaser Enter Your Details to continue\n")

#     #using try and except to take user's input so the program doesn't crash when invalid data is entered
#     try:
#         user_name = input("Enter your full name: ").upper().strip()
#         user_age = int(input("Enter your age: "))
#         user_contact = int(input("Enter your contact: "))
#         user_email = input("Enter your email: ")
#         user_fees = float(input("Enter your fees(GHS): "))
#         user_location = input("Enter your location: ").upper().strip()

#     except Exception as e:
#        print(f"an error occure: {e}")

#     else:
#         with open("school_system.txt", "w") as file:
#             print("\n")
#             print("--- Congratulations! Here are you're details. Confirm ---\n")

#             details = file.write(
#                 f"Name: {user_name}\n"
#                 f"Age: {user_age}\n"
#                 f"Contact: {user_contact}\n"
#                 f"Email: {user_email}\n"
#                 f"Fees: GHS{user_fees}\n"
#                 f"Location: {user_location}\n\n"
#             )
#         with open("school_system.txt", "r") as file:
#             print(file.read())   

# #giving the user a choice either to register or not
# def choose():
#     options = {
        
#     }

# # main()
import time
start = time.time()
n = 0
while n < 1000:
    print(n)
    n+= 1

end = time.time()
elapsed = end - start
print(int(elapsed))