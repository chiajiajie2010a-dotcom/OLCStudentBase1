# firstname = input("Please enter your first name: ").lower()
# lastname = input("Please enter your last name: ").lower()
# email_id = firstname[:3] + lastname + "@example.com"
# print("Your email ID is " + email_id)
# Task 2.1
# [2 mark]
# Edit the program to ensure that the email ID is created using the first letter of the first name and the last three characters of the last name. 
# Assume that the last name will always have at least 3 characters.

# firstname = input("Please enter your first name: ").lower()
# lastname = input("Please enter your last name: ").lower()
# email_id = firstname[0] + lastname[-3:] + "@example.com"
# print("Your email ID is " + email_id)



# Task 2.2
# [3 marks]
# After generating the email ID, ask the user to retype the email address to confirm they have noted it down correctly. 
# Edit the program to: Ask the user to re-enter the generated email address.
# Check that the entered email contains the '@' symbol and at least 1 dot.
# If the input does not contain '@', display an error message and prompt the user again.
# Check that the input email is the same as generated email.
# Repeat this until a valid format is entered.
firstname = input("Please enter your first name: ").lower()
lastname = input("Please enter your last name: ").lower()
email_id = firstname[0] + lastname[-3:] + "@example.com"
print("Your email ID is " + email_id)

re-enter = input("please enter the email given to y





# Task 2.3
# [5 marks]
# Edit the program to generate a random password for the user after confirming the email. The password must:

# Be exactly 8 characters long
# Contain at least one uppercase letter (ASCII codes 65 to 90)
# Contain at least one lowercase letter (ASCII codes 97 to 122)
# Contain at least one digit (ASCII codes 48 to 57)
# Display the generated password to the user after it is created.