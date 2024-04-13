import random

print("Welcome to the Guess the number!!!")
print("------------------------------------")
name = input("Please Type Your Name: ")
print("------------------------------------")
print(f"Hello, {name}, Please Choose A Difficulty")
print("------------------------------------")
print("1 = Baby Mode")
print("2 = Regular")
print("3 = Hard")
print("------------------------------------")

mode = int(input(f"Please Enter Difficulty, {name}: "))

print("------------------------------------")

##MODE SELECTION
##Based on Mode selected gives desired difficultys like more lives and a smaller
if mode == 1:
    print("------------------------------------")
    print("You Have Chosen Baby Mode!!! 👶👶")
    print("------------------------------------")
    a = random.randint(1, 10)
    lives = 3
    ##gives message to choose number once mode had been selected
elif mode == 2:
    print("------------------------------------")
    print("You Have Chosen Regular!!! 😎😎 ")
    print("------------------------------------")
    a = random.randint(1, 50)
    lives = 3
elif mode == 3:
    print("------------------------------------")
    print("You Have Chosen Hard Mode!!! 👹👹")
    print("------------------------------------")
    a = random.randint(1, 100)
    lives = 4
else:
    print("------------------------------------")
    print("Somthing Went Wrong...")
    print("------------------------------------")

guess = int(input("Guess the Number: "))

while guess != a and lives != 0:
    if guess > a:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You Have Guessed to High")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        guess = int(input("Guess the Number: "))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        lives = lives - 1
    elif guess < a:
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        print("You Have Guessed to Low")
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        guess = int(input("Guess the Number: "))
        print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
        lives = lives - 1

if guess == a:
    print("------------------------------------")
    print("You Guessed The Write Number You Won 🥳🎊")
    print("------------------------------------")

if lives == 0:
    print("------------------------------------")
    print("YOU FAILED 😭😭")
    print("------------------------------------")
    print(f"The Answer is **{a}**")
    print("------------------------------------")
    print(f"{name}, You Have {lives}❤️ Lives Left...")
    print("------------------------------------")
