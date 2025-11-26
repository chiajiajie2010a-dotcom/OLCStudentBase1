# password = "password123"
# tries = 5
# for i in range(5):
#     inputpassword = input("please enter your password")
# if password == inputpassword:
#     print("Access Granted!")
# else:
#     tries = i - 1
#     print(f"access denied! Tries left {tries}")

# password = "password123"
# updatedtries = 3
# status = False
# while not status:
#     inputpassword = input("please enter your password")
#     if inputpassword == password:
#         print("Access Granted")
#         status = True
#     else:
#         print(f"Please Try again. Tries Left {updatedtries}")  
#         updatedtries -= 1
#         if updatedtries == 0:
#             print("Account locked")
#             status = True 

        


# password = "password123"
# updatedtries = 0

# while True:
#     inputpassword = input("please enter your password")

#     if inputpassword == password:
#         print("Access Granted")
#         break
#     else:
#         print("Access Denied")
#         updatedtries += 1

#         if updatedtries == 3:
#             print("Account Locked out")
#             break

###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 8: Pass/Fail Checker
# Write a program to check if a student's score is a pass or 
# fail. Passing marks are 50 and above. Example: Input = 65.
# Output: "Pass."
# grades = int(input("Please enter your marks:"))
# passing = 50 
# status = False 
# while not status:
#     if grades < passing:
#         print("you failed")
#         status = True  
#     else:
#          print("you passed!")
#          status = True  




# marks = 0 
# import random


# #what is 20 + 30 
# for i in range(10):
#     num1 = random.randint(20,50)
#     num2 = random.randint(20,50)
#     answer = int(input(f"what is {num1} + {num2}:"))
#     if answer == num1 + num2:
#         marks += 1
#         print(f"Correct! Marks : {marks}")
#     else:
#         marks -= 1
#         print(f"wrong! marks : {marks}")
# if marks < 5:
#     print(f"go see the principal!, You got {marks}/10")
# else:
#     print(f"you Passed! you got {marks}/10")        














# marks = 0
# import random
# for i in range(10):
#     num1 = random.randint(20,50)
#     num2 = random.randint(20,50)
#     answer = int(input("Please put in the answer!"))
#     if answer == num1 + num2:
#         marks += 1
#         print(f"Correct! Marks: {marks}")
#     else:
#         marks -= 1
#         print(f"Wrong! Marks: {marks}")
# if marks < 5:
#     print(f"go see the principal. Marks : {marks}")
# else:
#     print("you passed! marks: {}".format(marks))



# import random
# chances = 7
# number = random.randint(1,100)
# while True: 
#     inputnumber = int(input("please enter your number you guess:"))
#     if inputnumber > number:
#         chances -= 1 
#         print(" Your guess is over the random number. Tries left: {}".format(chances))
#     elif inputnumber < number:
#         chances -= 1 
#         print("your guess is below the random number. Tries left: {}".format(chances))
#     else:
#         print("Your number is correct")
#         break 
#     if chances == 1:
#         if number % 2 == 0:
#             print("Hint: The number is EVEN!")
#         else:
#             print("Hint: The number is ODD!")
#     if chances == 0:
#         print("Game Lost! number was {}".format(number))
#         break

# #------------------------------------------------------------

# # Exercise 9: Finding the Largest of Three Numbers
# # Write a program to find the largest of three numbers.
# # Example: Input = 4, 7, 2. Output = "The largest is 7."
# # number = []
# # for i in range(3):
# #     numbers = input("please enter 3 numbers")
# #     number.append(numbers)
# # print(f"the largest number is {max(number)}")





# #------------------------------------------------------------
# # Exercise 10: Leap Year Checker
# # Write a program to check if a year is a leap year.
# # Example: Input = 2024. Output = "Leap year."






# #------------------------------------------------------------
# # Exercise 11: Age-Based Group Assignment
# # Write a program to categorize a person into groups based 
# # on age: Child (0-12), Teen (13-19), Adult (20+).
# # Example: Input = 15. Output = "Teen."






# #------------------------------------------------------------
# # Exercise 12: Grade Checker
# # Write a program to assign a grade based on marks:
# # >= 90: A, >= 75: B, >= 60: C, < 60: D.
# # Example: Input = 85. Output = "Grade B."






# #------------------------------------------------------------
# # Exercise 13: Even/Odd Checker
# # Write a program to check if a number is even or odd.
# # Example: Input = 4. Output = "Even number."






# # Recap and Warm up - DO THIS

# # write a program to help categorise how much bus fare to pay

# # ask user to input an age

# # check if age is a valid number # <str>.isdigit()

# # use if, elif and else
# # age < 7, free
# # between 7 to 12, $2.00
# # between 13 to 21, $4.00
# # between 22 to 60, $10.00
# # 61 and above, $1.00

# # Print out the correct fare according to the age.

fee = 0.00
while True:
    age = input("please enter your age")
    #if not age.isdigit() == True:
    if not age.isdigit():
        print("Please put in a integer not a string")
    else:
        age = int(age) # convert here

        if int(age) < 7:
            print("your bus fare is ${}".format(fee))
            break
        elif int(age) >=7 and int(age) <= 12:
            fee += 2 
            print("your bus fare is ${}".format(fee))
            break
        elif int(age) >= 13 and int(age) <=21:
            fee += 4
            print("your bus fare is ${}".format(fee))
            break
        elif int(age) >= 22 and int(age) <=60:
            fee += 10
            print("your bus fare is ${}".format(fee))
            break
        else:
            fee += 1
            print("your bus fare is ${}".format(fee))
            break
