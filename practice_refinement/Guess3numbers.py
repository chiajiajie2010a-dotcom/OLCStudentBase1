# guess 3 digits 

status = False 
import random

secret_code = ""
for i in range(3):
    digit = str(random.randint(1, 5))
    secret_code = secret_code + digit

print("Guess the 3-digit number. Each digit is from 1 to 5: ")
print("You have 5 tries. Enter your guess (e.g. 123). ")

for attempts in range(5):
    while not status:
        player_guess = input("Please enter your guess: ")    
        if len(player_guess) == 3:
            break
        else:
            print("try again")
    count_accurate = 0


    for i in range(len(secret_code)):
        if secret_code[i] == player_guess[i]:
            count_accurate += 1

    print(f"You got {count_accurate} digits and positions correct")


    if player_guess == secret_code:
        print("You win")
        break
    else:
        print("Your guess was wrong")

else:
    print("You lose, code was {}".format(secret_code))
