



# Task 5.1
# [3 marks]
# Edit the program to repeatedly prompt the organizer to enter a member's preferred sport. 
# The loop should stop when the organizer enters 'done'

# task 5.1 
# status = False 
# while not status:
#     sports = input("whats the members's favourite sport?")
#     if sports.lower()== "done":
#         status = True 



# Task 5.2
# [2 marks]
# Edit your program to convert each sport to lowercase and then store it into a list.

# task 5.2
# untitled_list = []
# status = False 
# while not status:
#     sports = (input("whats the members's favourite sport?").lower())
#     if sports.lower()== "done":
#         status = True 
#     else:
#         untitled_list.append(sports)
# print(untitled_list)





# Task 5.3
# [5 marks]
# Edit your program to display the number of members that prefer a specific sport. 
# The program must:

# Ask the organizer to input a sport to search for in the list.
# Output an appropriate message if the sport does not exist in the list. (i.e. nobody likes it)
# Output the sport and the number of members who prefer that specific sport.
# Your program must handle upper and lower case search queries 
# (i.e. users can type "SOCCER" to search for "Soccer"). Suitable input and output messages must be used.

# task 5.3
count = 0 
untitled_list = []
status = False 
while not status:
    sports = (input("whats the members's favourite sport?").lower())
    if sports.lower()== "done":
        status = True 
    else:
        untitled_list.append(sports)

search = (input("find a sport that you want: ").lower())
if search not in untitled_list:
    print("nobody likes this sport")
else:
    for sport in untitled_list:
        if sport == search:
            count += 1
    print(count,"likes this sports")


