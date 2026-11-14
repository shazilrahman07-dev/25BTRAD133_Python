import random

# Lab Exercise 5: Number Guessing Game

# Generate a secret random number between 1 and 100
secret_number = random.randint(1, 100)
attempts = 0

print("=" * 40)
print(" WELCOME TO THE NUMBER GUESSING GAME ")
print("=" * 40)
print("I'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("\nEnter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"\nCongratulations! You guessed the number in {attempts} attempts.")
        break