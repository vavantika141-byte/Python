num=int(input("Enter the number:"))
guess=0
while guess!=num:
    guess=int(input("Guess the number: "))
    if guess<num:
        print("Too low!")
    elif guess>num:
        print("Too high!")

print("You guessed the number.")