# Task 2

# The following program allows the weights of 15 bags of rice to be input. 
# The correct weight for each bag of rice must be 
# between 4.9 kg and 5.1 kg inclusive.

# bags_rice = 15
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")    

# 7       Edit the program so that it:
# a.       Accepts the weights for only 10 bags of rice.
# [1] ## T.David: Correct 1 mark
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     if bag_weight < lower_bound:
#         print("The bag of rice is underweight")    


# b.       Prints out the message “The bag of rice is the correct weight” 
# when a weight entered is between 4.9kg and 5.1 kg inclusive.
# [2]  ## T.David: Correct 2 mark
# bags_rice = 10
# upper_bound = 5.1
# lower_bound = 4.9
# for count in range(bags_rice):
#     bag_weight = float(input("Enter the weight of the bag of rice "))
#     if bag_weight > upper_bound:
#         print("The bag of rice is overweight")
#     elif bag_weight < lower_bound:
#         print("The bag of rice is underweight")  
#     else:
#         print("The bag of rice is correct weight")  

# c.       Prints out the number of bags of rice that were underweight, 
# as well 1as the number that were overweight, after the weights of all 
# the bags have been entered.
# [5]# number = 0

under = 0
over = 0
bags_rice = 10
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))


    if bag_weight > upper_bound:
            over += 1
            print("The bag of rice is overweight")
        
    elif bag_weight < lower_bound:
        under +=1
        print("The bag of rice is underweight")  
    else:
        print("The bag of rice is correct weight") 
print("there are {} overweight bags, {} underweight bags".format(over,under))
    

# d. Edit your program so that it works for any number of bags of rice.
# [2]
# Save your program.
under = 0
over = 0
bags_rice = int(input("please enter the number of bags you want to check: "))
upper_bound = 5.1
lower_bound = 4.9
for count in range(bags_rice):
    bag_weight = float(input("Enter the weight of the bag of rice "))

    if bag_weight > upper_bound:
            over += 1
            print("The bag of rice is overweight")
        
    elif bag_weight < lower_bound:
        under +=1
        print("The bag of rice is underweight")  
    else:
        print("The bag of rice is correct weight") 
print("there are {} overweight bags, {} underweight bags".format(over,under))
    
