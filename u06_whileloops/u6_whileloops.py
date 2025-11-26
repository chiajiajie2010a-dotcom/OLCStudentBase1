# # use the while loop and print out numbers from 0 to 5
# count = 0
# while count < 6:
#     print(count)
#     count += 1

# # use the while loop and print out numbers from 1 to 5
# count = 1
# while count < 6:
#     print(count)
#     count += 1

# # use the while loop and print out multiples of 5 from 5 to 50
# count = 5
# while count < 51:
#     print(count)
#     count += 5

# # use the while loop and print out numbers from 10 to 1
# count = 10
# while count > 0:
#     print(count)
#     count -= 1


#------------------------------------------------------------
# Exercise 6: While True + break 
# Repeatedly ask for integers and add them to a total.
# Stop when user enters "END" (case-insensitive).
# Print total after stopping.
# Sample Inputs: 10, 20, 5, END
# Example Output: Total = 35
# #------------------------------------------------------------
# while True:
#     inputnumber = input("Please enter a number: ")

#     if inputnumber.upper() == "END":
#         break    # stop the loop

#     # convert input to integer and add to total
#     total += int(inputnumber)

# print("Total =", total)



while True:
    age = input("Enter your age:")
    if age.isdigit():
        age = int(age)

        if age > 16:
            print("you go to JC or poly")
        elif age > 12:
            print("You go to secondary school")
        elif age > 6:
            print("you go to primary school")
        else:
            print("you are too young")
        break
    else:
        print("this is not a number")



