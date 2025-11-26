# name = input(str("please enter your name:"))
# hobby = input(str("please enter your hobby:"))
# print(f" {name} likes {hobby}")

# var1 = "dog"
# var2 = "cat"
# var3 = var1 +var2

# var4 = 10
# var5 = 20 
# var6 = var4 + var5 

# num1 = int(input("enter Number 1:"))
# num2 = int(input("Enter number 2:"))
# result = num1 / num2
# print(round(result))


#------------------------------------------------------------
# Exercise 8: Area of a Circle with .format()
# Write a program to ask the user for the radius of a circle, convert it to
# a float, calculate the area using the formula (area = 3.14 * r^2), and
# display the result using .format(). Example:
# Input: radius = 7
# Output: "The area of the circle is 153.86."
# import math 
# radius = float(input("please enter your required radius"))
# def area_of_circle():
#     Area = 3.14 * radius **2
#     return Area
# print("The area of the circle is {}".format(area_of_circle()))




###########################################################
# Part 2. IN-CLASS Practice Exercises

# Exercise 7: Simulating Two Dice Rolls
# Write a program to simulate the roll of a 6-sided die two times
# and display the results. Example: Output = 4, 6.

# import random 
# roll1 = random.randint(1,6)
# roll2 = random.randint(1,6)
# print(roll1, roll2)




#------------------------------------------------------------
# Exercise 8: Floor Division for Groups
# Write a program to calculate how many full groups can be formed 
# and how many items are leftover. Example: 25 students divided 
# into groups of 4 = 6 groups and 1 leftover.

# students = 25

# groups = students // 4 # do a floor divide
# leftover = students % 4

# print(f"{students} students can be divided into {groups} groups of 4 with {leftover} without a group.")


#------------------------------------------------------------
# Exercise 9: Rounding for Fuel Costs
# Write a program to calculate the total cost of fuel rounded up 
# to the nearest dollar. Example: If the fuel cost is 47.89, the 
# total is 48.




#------------------------------------------------------------
# Exercise 10: Floor Division for Age Conversion
# Write a program to calculate someone's age in decades and 
# remaining years. Example: Age = 29 -> Decades = 2, Years = 9.
age = int(input("please enter your age"))
decades = age // 10 
leftover = age % 10 
print(f"Age = {age} -> Decades = {decades} , years = {leftover}")



#------------------------------------------------------------
# Exercise 11: Calculating Items in Boxes
# Write a program to calculate how many full boxes are needed to 
# pack items and how many items are leftover. Example: If there 
# are 53 items and each box holds 12, the output is:
# Full boxes = 4, Leftover = 5.

