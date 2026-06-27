number = int(input("Enter the secret number: "))
guess = 0

while guess != number:
    guess = int(input("Guess the number: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print("Congratulations! You guessed the number.")