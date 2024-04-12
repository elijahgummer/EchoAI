import random

print("Welcome to the Guess the number!!!")
print("------------------------------------")
name = input("Please Type Your Name: ")
print(f"Hello, {name}, Please Choose A Difficulty")
print("------------------------------------")
print("1 = Baby Mode")
print("2 = Regular")
print("3 = Hard")
print("------------------------------------")
mode = int(input("Please Enter Difficulty: "))

##MODE SELECTION
##Based on Mode selected gives desired difficultys like more lives and a smaller
if mode == 1:
    print("You Have Chosen Baby Mode!!!")
    a = random.randint(1, 10)
    print(a)
    ##gives message to choose number once mode had been selected
elif mode == 2:
    print("You Have Chosen Regular!!!")
    a = random.randint(1, 50)
    print(a)
elif mode == 3:
    print("You Have Chosen Hard Mode!!!")
    a = random.randint(1, 100)
    print(a)
else:
    print("Somthing Went Wrong...")


guess = int(input("Guess the Number: "))


    ##FUNCTIONALITY TO DETERMINE WEATHER THE Answer equals the users answer
def WrongAnswer():
    print("Try Again...")
    guess = int(input("Guess the Number: "))
    
if guess == a:
    print("You Have guessed right")
elif guess != a:
    for 
    WrongAnswer()  
else:
    print("Somthing Went Wrong!!!")
