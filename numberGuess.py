import random

a = random.randint(1,10)

print(a)

print()
print("Welcome to the Guess the number!!!")
print("------------------------------------")
name = input("Please Type Your Name: ")
print(F"Hello, {name}, Please Choose A Difficulty")
print("------------------------------------")
print("1 = Baby Mode")
print("2 = Regular")
print("3 = Hard")
print("------------------------------------")
mode = input(int("Please Enter Difficulty: "))

##MODE SELECTION
if mode == 1:
    print("You Have Chosen Baby Mode!!!")
elif mode == 2:
    print("You Have Chosen Regular!!!")
elif mode == 3: 
    print("You Have Chosen Hard Mode!!!")
else
    print("Somthing Went Wrong...")

