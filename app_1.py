import random

# Generate a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)


def startgame():
    # Ask the user to guess a number
    guess=input("Guess a number between 1 and 100: ")
    try:
        guess = int(guess)
    except ValueError:
        print('Please enter a valid number.')
        startgame()

    # Compare the user's guess to the generated number
    if guess==random_number:
        print('Congratulations, you guessed the number!')
    elif guess>1 or guess<100:
        print('Please enter a number between 1 and 100.')
        startgame()
    elif guess < random_number:
        print('Too low!')
        startgame()
    else:
        print('Too high!')
        startgame()
startgame()