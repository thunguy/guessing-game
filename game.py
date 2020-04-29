import random

name = input("What's your name? ").capitalize()
greeting = f"Hello {name}! I'm thinking of a number between 1 and 100. Can you guess what it is?"

print(greeting)

random_num = random.randint(1, 100)
attempts = 0

while True:
    guess = input("Your guess? ") 

    try:
        guess = int(guess) 
    except ValueError:  # if ValueError is thrown, then guess != valid integer
        print(f"Oops, {guess} is not a valid number. Please try again.")
        continue

    if guess < 1 or guess > 100:
        print(f"{guess} is out of range. Please choose a number between 1 and 100.")
        continue

    attempts += 1

    if random_num > guess:
        print("Your guess is too low, try again.")
        
    elif random_num < guess:
        print("Your guess is too high, try again.")

    else:
        print(f"Congratulations, {name}! You guessed it in {attempts} tries.")
        break  # game over -- stop prompting for guesses


