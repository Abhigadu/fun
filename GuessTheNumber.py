#Purpose: To Generate a Random number between 1 & 20
#Author: Abhigadu
#Date: 9-May-2020

import random

CNumber=int(random.randint(1,20))
#print(CNumber)

print("Welcome to a small Game")
print("We have generated a random number between 1 and 20")
print("Your job is to guess it correctly")
user=input("Enter Your name: ")

#print(UNumber)
userexit = 0
count = 0


while userexit != 1:
    UNumber=int(input("Guess the Number: "))
    count+=1
    if UNumber == CNumber:
        print("You Guessed it correctly")
        print(str(user) + " you guessed the correct number in " + str(count) + " tries")
        choice=input("Do you want to play again ?(Y/N)")
        if choice == 'Y' or choice == 'y':
            CNumber=int(random.randint(1,20))
            userexit = 0
            count = 0
        else:
            userexit = 1
            print("Thank you for playing. I wrote this for my son Ishit Ronel")
            input("")

    elif UNumber < CNumber:
        print("The number you entered is less than our number")
    elif UNumber > CNumber:
        print("The number you entered is more than our number")