# # def hello():
# #     print("Hello, How are you?")
# #     return 
# # print(hello())

# # def greet(yourname):
# #     print(f"hello{yourname}, How are you?")
# #     print(f"My name is {myname}")
# # greet("yu Yang","David")

# # length = int(input("please enter a length"))
# # breath = int(input("please enter a breath"))   
# def area_of_rectangle(length, breath):
#     area = length * breath
#         print(area)
#     return area 
# rect1 = area_of_rectangle(65,89)
# rect2 = area_of_rectangle(75,12)
# rect3 = area_of_rectangle(4,75)
# rect4 = area_of_rectangle(78,36)
# rect5 = area_of_rectangle(14,89)
# total = rect1 + rect2 + rect3 + rect4 + rect5




# Exercise 8: Simple Calculator
# Write a function that takes two numbers and an operator (+, -, *, /)
# and returns the result of the calculation.

# num1 =int(input("please eneter your desired number"))
# num2 =int(input("please eneter your desired number"))
# def addition(num1,num2):
#     result1 = num1 + num2
#     print(result1)
# def subtraction(num1,num2):
#     result2 = num1 - num2
#     print(result2)
# def multiplication(num1,num2):
#     result3 = num1 * num2
#     print(result3)
# def division(num1,num2):
#     result4 = num1 // num2
#     print(result4)
# choice = (input("please enter what choice you want, 1 for addition 2 for subtraction,3 for multiplication, 4 for division "))
# if choice == "1":
#     addition(num1,num2)
# elif choice == "2":
#     subtraction(num1,num2)
# elif choice == "3":
#     multiplication(num1,num2)
# else:
#     division(num1,num2)

def calculator(num1,num2,op):
    
    if operation == "+":
    # answer = num1 + num2
        return num1 + num2
    elif operation == "-":
        return num1 - num2 
    elif operation == "/":
        return num1 / num2
    else:
        return num1 * num2
    
    # return answer
num1 =int(input("please eneter your desired number"))
num2 =int(input("please eneter your desired number"))
operation = input("please put in the your desired operator (+,-, /, *)")
answer = calculator(num1, num2, operation)
print(f"{num1} {operation} {num2} = {answer}")

print(calculator(10, 5, "+"))
        
        


# Test the function with multiple operations.
# 
# print(calculator(10, 5, "-"))
# print(calculator(10, 5, "*"))
# print(calculator(10, 5, "/"))
