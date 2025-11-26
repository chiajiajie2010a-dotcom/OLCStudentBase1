menu = {"hamburger" : "$2.00", "fries" : "$1.00" , "pasta" : "$3.50"}

# retrieve a value from dictionery
priceham = menu["hamburger"]
print(priceham)

# change the value of a key 
menu["hamburger"] =  "$20.00"

print(menu)

# add new item to dictionery
menu["pizza"] = "30.00"

print(menu)

## delete an item 
del menu["fries"]
print(menu)

# loop through dictionery 
for food , price in menu.items():
    print(f"{food} : {price}")

### to ask customer what they want to eat 
# choice = input("please enter what you want to eat? ")
# if choice in menu:
#     # means iems exist
#     print(f"{choice} is {menu[choice]}")
# else:
#     print(f"sorry, We don't sell {choice}")

# ### ask for a key and value and add to dictionery
# newfood = input("Food to add to menu:")
# newprice = input('Price for the new food:')

# menu[newfood] = newprice

# print(menu)



choice = input("please enter what you want to eat? ")
if choice in menu:
    # means iems exist
    print(f"{choice} is {menu[choice]}")
else:
    reply = input("It does not exist on our menu, Add it to menu? Y/N")
    if reply.upper() == "Y":
        menu[choice] = "20.00"
    











dict1 = {"hamburger": 5, 
         "pasta": 10, 
         "fries": 2}

# add / amend
dict1["hamburger"] = 10

# for key,value in dict1.items():
#     print(key)
#     print(value)

# for key in dict1:
#     print(key) # key
#     print(dict1[key]) # value

def oddoreven(num):
    if num % 2 == 0:
        print("even")
    else:
        print("odd")



###########################################################
# Part 2. IN-CLASS Practice Exercises

# In-Class Exercise 1: Student Grades Analysis
# Scenario: A teacher needs to analyze student performance.
# Create a dictionary with student names as keys and grades as values.
students = {"Alice": 85, "Bob": 78, "Charlie": 92, "Diana": 88, "Eve": 76}

# Task 1: Identify and print the name of the highest scoring student.
# maxnum = 0
# maxname = ""
# # for i in students:
# for name, score in students.items():
#     # if students[i] > maxnum:
#     if score > maxnum
#         # maxnum = students[i]
#         maxnum = score
#         # maxname = i
#         maxname = name
# print(maxname,maxnum)

# max = 1111 # override the max()
# max()

#------------------------------------------------------------
# Task 2: Calculate and display the number of students scoring above 80.
maxnum = 0
count = 0 
maxname = ""
# for i in students:
for name, score in students.items():
    # if students[i] > maxnum:
    if score > 80:
        count += 1 
        print(name, count)



#------------------------------------------------------------
# Task 3: Update all grades by adding 5 points as a bonus.
maxnum = 0
count = 0 
maxname = ""
# for i in students:
# for name, score in students.items():
for name in students:
    students[name] += 5
    # if students[i] > maxnum:
print(students)
    





######################################################
# Question 2:
# The school's swimming coach has recorded the 50m freestyle 
# swim times (in seconds) for 15 swimmers. 
# Using the list provided, find and display the fastest and slowest swim times, 
# along with their swim lane position in the list.

# Assume that the first item in the list is swim lane position 1.
#####################################################
swim_times = [32.5, 30.1, 33.8, 29.6, 31.2, 34.0, 28.9, 
              30.4, 32.1, 27.5, 35.6, 31.8, 29.2, 33.0, 30.5]
# Answer for Question 2 here

fastestname = swim_times[0]
slowestname = swim_times[0]
for i in swim_times:
    if i <fastestname:
        fastestname = i

    if i > slowestname:
        slowestname = i
