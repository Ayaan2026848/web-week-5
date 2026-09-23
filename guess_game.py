secret_number = 7
attempts = 0

print("Guess the secret number!")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")
    elif guess > secret_number:
        print("Too high!")
    else:
        print(f"You got it in {attempts} tries!")
        break
