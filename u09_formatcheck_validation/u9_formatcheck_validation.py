# '''
# Question 1 (Length Check):
# Write the input entry and validation code for a program that
# needs to accept a 4-digit OTP (One-Time Password)
# The OTP must be exactly 4 digits long

# If the input is invalid, your code should keep trying
# by asking for the input to be entered again.

# #########################################

# Sample output

# Enter OTP: 12
# Invalid input. The OTP must be exactly 4 digits.

# Enter OTP: 12345

# Invalid input. The OTP must be exactly 4 digits

# Enter OTP: 1234
# OTP accepted

# '''

def validation(otp):
    if not otp.isdigit():
        print("Please out in digits not numbers")
        return False

    if len(otp) != 4:
        print("Please put a 4 digit letter ")
        return False
    return True

while True:
    otp = input("please enter a 4 digit OTP")
    if validation(otp) != True:
        print("")
    else:
        print("You are logged in!")
        break