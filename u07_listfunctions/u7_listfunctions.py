# # string variable
# # integer, float
# # boolean >> True False

# # List
# ###################################################
# # Part 1: Learning Exercises

# # Exercise 1: Accessing List Elements by Index
# # Write a program to access and print the first, second, and last 
# # elements of a list using indexing.
# lists =[]
# for i in range(5):
#     list = input("what do u want to put in a list: ")
#     lists.append(list)
# print(lists[3])

# fruits = ["apple", "orange", "banana","durian"] # my list
# print(fruits[2]) # retrieve a specific value from the list
# fruits[3] = "pineapple" #replce value in list
# print(fruits)
# del fruits[0] #remove item from list 
# print(fruits)
# fruits.remove("orange") #remove items using name 
# print(fruits)
# fruits.append("blehhhh") #adds to a list
# print(fruits)

# count = len(fruits)
# print(count)

# for i in fruits:

# #------------------------------------------------------------
# # Exercise 2: Adding Elements to a List
# # Write a program to add an element to the end of a list using 
# # append(), and add another element at a specific index using 
# # insert().


# fruits.append("durian") # add a new item to the list, adds at the back

# fruits.insert(1, "grapes") # add at specific position





# #------------------------------------------------------------
# # Exercise 3: Using del() to Remove an Element by Index
# # Write a program to delete an element at a specific index.
# # Example: Remove the second color.

# del(fruits[1]) # deleting by the index



# #------------------------------------------------------------
# # Exercise 4: Using remove() to Remove an Element by Value
# # Write a program to remove a specific element by its value.
# # Example: Remove "green" from the list.
# # colors = ["red", "green", "blue", "yellow"]
# # colors.remove("green")  # Remove by value
# # print("Colors after removal: {}".format(colors))

# # fruits.remove("durian")

# # while True:
# #     if "durian" in fruits:
# #         fruits.remove("durian")
# #     else:
# #         break



# #------------------------------------------------------------
# # Exercise 5: Using pop() to Remove and Retrieve an Element
# # Write a program to remove the last element of a list using pop().
# # Example: Remove and print the last color.
# # colors = ["red", "green", "blue", "yellow"]
# # removed_color = colors.pop()  # Remove the last element
# # print("Removed color: {}".format(removed_color))
# # print("Colors after pop: {}".format(colors))

# lastfruit = fruits.pop() # removes last one and assign to variable
# print(fruits)




# #------------------------------------------------------------
# # Exercise 6: Modifying Elements in a List
# # Write a program to change the second element in a list to "pink."
# # colors = ["red", "green", "blue"]
# # colors[1] = "pink"  # Modify value at index 1
# # print("Modified colors: {}".format(colors))
# print(lastfruit)
# fruits[3] = "spikyfruit" # change the value
# print(fruits)

# #------------------------------------------------------------
# # Exercise 7: Membership Check
# # Write a program to check if "blue" is in the list.
# # colors = ["red", "green", "blue"]
# # if "blue" in colors:
# #     print("Blue is in the list.")
# # else:
# #     print("Blue is not in the list.")

# # validation check - existence check
# checkfruit = input("Enter a fruit name: ")
# if checkfruit in fruits:
#     print(f"{checkfruit} is in the list")
# else:
#     print(f"{checkfruit} is not in the list")

# #------------------------------------------------------------

# ##### to loop through every single item
# for i in fruits:
#     print(i)

# # for i in range(5): 








# A friend matching company wishes to develop an application that helps its users to find friends. It does this by searching through its user database and pairing users with the same hobbies or personalities to one another.

# Open the file FRIENDS.ipynb

# It shows the following program that contains the names and profiles of the users. The program allows the user to:

# input a new name

# input whether they want to add a name and profile to the dictionary.

# For all the sub-tasks in Task 1, you can assume that all user inputs are valid.
# userbase = {
# "Name": ['Gender', 'Personality', 'Hobby'],
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"], 
# "David": ["Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"],
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": ["Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading"],
# "John": ["Male", "Extroverted", "Travel"]
# }
# Save the file as:

# TASK1_<your name>_<class>_<index number>.ipynb

# For each of the sub-tasks, begin in a new code cell and add a comment using the hash symbol '#' at the beginning of your code to indicate the sub-task that the program code belongs to.

# For example:

# #Task 1.1
# userbase = {
# "Alice": ["Female", "Extroverted", "Travel"],
# "Bob": ["Male", "Introverted", "Coding"],
# "Carol": ["Female", "Extroverted", "Photography"], 
# "David": ["Male", "Introverted", "Coding"],
# "Emily": ["Female", "Extroverted", "Travel"],
# "Frank": ["Male", "Kind", "Volunteering"],
# "Grace": ["Female", "Kind", "Reading"],
# "Henry": ["Male", "Kind", "Music"],
# "Ivy": ["Female", "Introverted", "Reading"],
# "John": ["Male", "Extroverted", "Travel"]
# }

# name = input("Please enter the name of a user: ")

# if name in userbase:
#     print(f"The profile for {name} is {userbase[name]}")
# else:
#     add = input ("Would you like to add a new entry? (Y/N): ")






# # Program Code

# # Task 1.1

# # Edit the program so that it:

# # ⚫ searches the dictionary for the name input and outputs the profile of that name

# # asks the user whether the name is to be added as a new entry if the name is not found in the dictionary.

# # Save your program.

# # [2]

# # Task 1.2

# # Copy and paste your program from sub-task 1.1.

# # Edit the program so that if the user inputs "Y" for add, the program allows the user to input the name and profile of the person to the dictionary in the format "Name": ['Gender', 'Personality', 'Hobby']

# # Appropriate messages must be used to prompt the user to input each of the profile field.

# # Save your program.

# # [2]

userbase = {
"Alice": ["Female", "Extroverted", "Travel"],
"Bob": ["Male", "Introverted", "Coding"],
"Carol": ["Female", "Extroverted", "Photography"], 
"David": ["Male", "Introverted", "Coding"],
"Emily": ["Female", "Extroverted", "Travel"],
"Frank": ["Male", "Kind", "Volunteering"],
"Grace": ["Female", "Kind", "Reading"],
"Henry": ["Male", "Kind", "Music"],
"Ivy": ["Female", "Introverted", "Reading"],
"John": ["Male", "Extroverted", "Travel"]
}

name = input("Please enter the name of a user: ")

if name in userbase:
    print(f"The profile for {name} is {userbase[name]}")
else:
    add = input ("Would you like to add a new entry? (Y/N): ")

    if add.upper() == "Y":
        newname = input("What is your name? ")
        newgender = input("What is your Gender? ")
        newpersonality = input("What is your Personality? ")
        newhobby = input("What is your hobby? ")

        # add this to the dictionary
        newlist = [newgender, newpersonality, newhobby]

        userbase[newname] = newlist # add the new person into the dictionary

print(userbase) # testing to see output

# Task 1.3
# personality ={"Extroverted" :[] ,"Introverted" : [] , "Kind" : [], "Curious" : []}

# for name, profile in userbase.items():
#    # for each name, pull out personlity of that name 
#     current_personality = profile[1]

#     #pull out value from personalities
#     friends = personalities[current_personality] #
#     friends.append(name)
#     personalities[current_personality]
# print(personalities)



# Copy and paste your program from sub-task 1.2.

# Edit the program so that it:

# initialises a new dictionary variable called personalities which contains the personality types: "Extroverted", "Introverted", "Kind" and "Curious" as keys

# searches through userbase and adds the names of those with the same personality together, in personalities.

# allows the user to input a personality type

# prints out a message "[N1', 'N2', 'N3'] should be friends as they are all P4.", where N1, N2, N3 are to be replaced with the names of the persons and P4 to be replaced with the personality type input by the user.

# Save your program.



userbase = {
"Alice": ["Female", "Extroverted", "Travel"],
"Bob": ["Male", "Introverted", "Coding"],
"Carol": ["Female", "Extroverted", "Photography"]
}
personalities = {"Extroverted":[],"Introverted":[],"Kind":[],"Curious":[]}

for name, profile in userbase.items():

    # for each name, i pull the personality of that name
    curr_personality = profile[1]

    # pull out value from personalities
    friends = personalities[curr_personality] # 
    friends.append(name)

    personalities[curr_personality] = friends

print(personalities)









# friends =[]
# for i in range(5):
#     friend = input("please enter 5 of your friends name: ")
#     friends.append(friend)
# for name in friends:
#     print(f"Hello {name}")


# # Exercise 9: Summing Numbers in a List
# # Write a program to calculate the sum of numbers in a list.
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]
# count = sum(list1)
# print(count)
count = 0 
for i in list1:
    count += i
print(count)
average = count / len(list1)
print(average) 



#------------------------------------------------------------
# Exercise 10: Finding the Maximum and Minimum
# Write a program to find the largest and smallest numbers in 
# a list using max() and min().
# Challenge without using max or min()
list1 = [2944, 5490, 2357, 2619, 1177, 451, 8299, 2533, 4682, 6040,
         5972, 7532, 4382, 8311, 6664, 4918, 3656, 3769, 6179, 7720,
         1777, 7149, 2175, 8665, 4586, 5208, 320, 1314, 8950, 4884,
         756, 6196, 5935, 5291, 8619, 2630, 1831, 3127, 4698, 6291,
         2478, 5792, 9362, 7348, 8040, 3556, 598, 6187, 8959, 880,
         6601, 538, 3439, 8508, 8649, 5139, 8076, 78, 6776, 362,
         6368, 6460, 8604, 1763, 1713, 2354, 2167, 6612, 8149, 7961,
         4270, 5285, 7346, 5667, 2102, 900, 8063, 4577, 2285, 9592,
         5671, 537, 9777, 9421, 5455, 1241, 990, 3745, 8443, 4213,
         4183, 2463, 9562, 8137, 5101, 397, 6966, 9927, 7473, 4105]

# maximum = max(list1)
# minimum = min(list1)

# print((f"max value is {maxiumum} and min value is {minimum}"))

maxiumum = (list1[0])
minimum = (list1[0])
for num in list1:
    if num > maxiumum:
        maxiumum = num
    if num < minimum:
        minimum = num
print(f"max value is {maxiumum} and min value is {minimum}")