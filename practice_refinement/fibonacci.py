# Task 2
  # A Fibonacci sequence is the integer sequence of 0, 1, 1, 2, 3, 5, 8....
  # The first two terms are 0 and 1.
  # All other terms are obtained by adding the preceding two terms.
  # The following program outputs the first five terms in the Fibonacci sequence.

#   n1 = 0
#   n2 = 1
#   nterms = 5
#   for i in range(nterms):
#       print(n1)
#       nth = n1 + n2
#       n1 = n2
#       n2 = nth

  ###########################################################
  # 6. Edit the program so that it works for any number of terms.
  # The program must display a suitable input message.
  # [1]
  ###########################################################
  # Copy + Paste & Write your code here
 
# n1 = 0
# n2 = 1
# nterms = int(input("how many terms do you want :"))
# for i in range(nterms):
#     print(n1)
#     nth = n1 + n2
#     n1 = n2
#     n2 = nth
  





  ###########################################################
  # 7. Edit the program to only accept a positive integer to be input.
  # A suitable error message must be displayed if the nterms
  # is not in the range. The program must loop until a valid nterms is input.
  # [3]
  ###########################################################
  # Copy + Paste & Write your code here
# n1 = 0
# n2 = 1
# status = False
# while not status:
#     nterms = int(input("how many terms do you want :"))
#     if nterms < 0:
#         print("try again. Please put a positive integer")
#     else:
#         for i in range(nterms):
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
#             status = True 




  ###########################################################
  # 8. Edit the program to store the Fibonacci sequence in a list.
  # Display the list at the end of program.
  # [3]
  ###########################################################
  # Copy + Paste & Write your code here

# list = []
# n1 = 0
# n2 = 1
# status = False
# while not status:
#     nterms = int(input("how many terms do you want :"))
#     if nterms < 0:
#         print("try again. Please put a positive integer")
#     else:
#         for i in range(nterms):
#             list.append(n1)
#             print(n1)
#             nth = n1 + n2
#             n1 = n2
#             n2 = nth
            
#             status = True 
# print(list)






  ###########################################################
  # 9.
  # Edit the program to allow user to input another positive integer
  # and display if the integer is in the first hundredth terms of
  # the Fibonacci sequence. You do not need to validate the input.
  # [3]
  ###########################################################
  # Copy + Paste & Write your code here
list = []
checknum = int(input("enter a integer to check if it is in the 100 term of fibonacci"))
n1 = 0
n2 = 1
status = False
while not status:
    nterms = 100
    if nterms < 0:
        print("try again. Please put a positive integer")
    else:
        for i in range(nterms):
            list.append(n1)
            print(n1)
            nth = n1 + n2
            n1 = n2
            n2 = nth
            
            status = True 
print(list)
if checknum in list:
    print(checknum, " is in within the 100th term of fibonacci")
else:
    print("it is not in the range of the 100th term")

  