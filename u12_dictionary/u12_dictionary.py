# menu = {"hamburger" : "$2.00", "fries" : "$1.00" , "pasta" : "$3.50"}

# # retrieve a value from dictionery
# priceham = menu["hamburger"]
# print(priceham)

# # change the value of a key 
# menu["hamburger"] =  "$20.00"

# print(menu)

# # add new item to dictionery
# menu["pizza"] = "30.00"

# print(menu)

# ## delete an item 
# del menu["fries"]
# print(menu)

# # loop through dictionery 
# for food , price in menu.items():
#     print(f"{food} : {price}")

# ### to ask customer what they want to eat 
# # choice = input("please enter what you want to eat? ")
# # if choice in menu:
# #     # means iems exist
# #     print(f"{choice} is {menu[choice]}")
# # else:
# #     print(f"sorry, We don't sell {choice}")

# # ### ask for a key and value and add to dictionery
# # newfood = input("Food to add to menu:")
# # newprice = input('Price for the new food:')

# # menu[newfood] = newprice

# # print(menu)



# choice = input("please enter what you want to eat? ")
# if choice in menu:
#     # means iems exist
#     print(f"{choice} is {menu[choice]}")
# else:
#     reply = input("It does not exist on our menu, Add it to menu? Y/N")
#     if reply.upper() == "Y":
#         menu[choice] = "20.00"
    











# dict1 = {"hamburger": 5, 
#          "pasta": 10, 
#          "fries": 2}

# # add / amend
# dict1["hamburger"] = 10

# # for key,value in dict1.items():
# #     print(key)
# #     print(value)

# # for key in dict1:
# #     print(key) # key
# #     print(dict1[key]) # value

# def oddoreven(num):
#     if num % 2 == 0:
#         print("even")
#     else:
#         print("odd")



# ###########################################################
# # Part 2. IN-CLASS Practice Exercises

# # In-Class Exercise 1: Student Grades Analysis
# # Scenario: A teacher needs to analyze student performance.
# # Create a dictionary with student names as keys and grades as values.
# students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# # Task 1: Identify and print the name of the highest scoring student.
# # maxnum = 0
# # maxname = ""
# # # for i in students:
# # for name, score in students.items():
# #     # if students[i] > maxnum:
# #     if score > maxnum
# #         # maxnum = students[i]
# #         maxnum = score
# #         # maxname = i
# #         maxname = name
# # print(maxname,maxnum)

# # max = 1111 # override the max()
# # max()

# #------------------------------------------------------------
# # Task 2: Calculate and display the number of students scoring above 80.
# maxnum = 0
# count = 0 
# maxname = ""
# # for i in students:
# for name, score in students.items():
#     # if students[i] > maxnum:
#     if score > 80:
#         count += 1 
#         print(name, count)



# #------------------------------------------------------------
# # Task 3: Update all grades by adding 5 points as a bonus.
# maxnum = 0
# count = 0 
# maxname = ""
# # for i in students:
# # for name, score in students.items():
# for name in students:
#     students[name] += 5
#     # if students[i] > maxnum:
# print(students)
    





# ######################################################
# # Question 2:
# # The school's swimming coach has recorded the 50m freestyle 
# # swim times (in seconds) for 15 swimmers. 
# # Using the list provided, find and display the fastest and slowest swim times, 
# # along with their swim lane position in the list.

# # Assume that the first item in the list is swim lane position 1.
# #####################################################
# swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
#               30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# # Answer for Question 2 here

# fastestname = swim_times[0]
# slowestname = swim_times[0]
# for i in swim_times:
#     if i <fastestname:
#         fastestname = i

#     if i > slowestname:
#         slowestname = i


# A student is writing a program to note down 
# the favourite sports of each of his classmates.
# the program will help check how many students like a certain sport.



# Write a program that will 
# -------------------------------------------------
# 1. ask how many students there are in the class

# -------------------------------------------------
# 2. for each student, ask what is their favourite sport
	# 2a. Add the sport into a list

# -------------------------------------------------
# 3. After asking all the student's sport, 
	# Ask the user to enter a sport to check how many students like the sport.

# -------------------------------------------------
# 4. if the sport exist, print out how many people like the sport.
	# e.g. # 3 students like the sport

# -------------------------------------------------
# 5. if the sport does not exist, print out an appropriate message.

# ** Assume that all inputs given are in lower case and valid.
# ** the program will work for any number of students.



# sports = []
# count = 0
# students = int(input("how many students is there in your class : "))
# for i in range(students):
#     hobby = input("please enter your hobby")
#     sports.append(hobby)

# question = input("Enter a hobby that you want to see as majority :")
# if question not in sports:
#     print(f"{question} not does not exist")
# else:
#     for i in sports:
#         if i == question:
#             count += 1
# print(f"{count} students likes {question}")
        

#------------------------------------------------------------
# In-Class Exercise 2: Inventory Stock Management
# Scenario: A warehouse manager needs to manage product stock levels.
inventory = {"Apples": 50, "Bananas": 30, "Oranges": 20, "Grapes": 60}

# Task 1: Add a new product "Pineapples" with an initial stock of 40.

inventory["Pineapples"] = 40
print(inventory)


#------------------------------------------------------------
# Task 2: Find and print the total stock of all items combined.
# count = 0
# for items, stock in inventory.items():
#     count += stock
# print(f"stock left combined is {count}")




#------------------------------------------------------------
# Task 3: Identify and remove any product with stock below 25.
for items, stock in inventory.items():
    if stock < 25:
        del inventory[items]
print(inventory)



#------------------------------------------------------------
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Checked Out", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

#------------------------------------------------------------
# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies.



#------------------------------------------------------------
# Task 2: Update the status of "1984" to "Checked Out" if all copies are borrowed.




#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.






#------------------------------------------------------------
# In-Class Exercise 4: Customer Orders Tracking
# Scenario: A store tracks orders with customers and the items they purchased.
orders = {
    "John": ["Apples", "Bananas"],
    "Mary": ["Oranges", "Grapes"],
    "Alice": ["Bananas", "Pineapples"],
}

# Task 1: Add a new order for "Mark" who purchased "Apples" and "Oranges".





#------------------------------------------------------------
# Task 2: Count and print the total number of unique items purchased by all customers.



#------------------------------------------------------------
# Task 3: Identify customers who purchased "Bananas".



#------------------------------------------------------------




#------------------------------------------------------------
# Task 2: Find and print the total stock of all items combined.




#------------------------------------------------------------
# Task 3: Identify and remove any product with stock below 25.



#------------------------------------------------------------
# In-Class Exercise 3: Library Book Management
# Scenario: A librarian tracks the availability of books in a dictionary.
books = {
    "1984": {"status": "Available", "copies": 5},
    "Brave New World": {"status": "Checked Out", "copies": 0},
    "Fahrenheit 451": {"status": "Available", "copies": 2},
}

#------------------------------------------------------------
# Task 1: Add a new book "To Kill a Mockingbird" with 3 copies.



#------------------------------------------------------------
# Task 2: Update the status of "1984" to "Checked Out" if all copies are borrowed.




#------------------------------------------------------------
# Task 3: Print all books currently available along with their copy count.






#------------------------------------------------------------
# In-Class Exercise 4: Customer Orders Tracking
# Scenario: A store tracks orders with customers and the items they purchased.
orders = {
    "John": ["Apples", "Bananas"],
    "Mary": ["Oranges", "Grapes"],
    "Alice": ["Bananas", "Pineapples"],
}

# Task 1: Add a new order for "Mark" who purchased "Apples" and "Oranges".





#------------------------------------------------------------
# Task 2: Count and print the total number of unique items purchased by all customers.



#------------------------------------------------------------
# Task 3: Identify customers who purchased "Bananas".



#------------------------------------------------------------




    
    
