import random

# Generate a random number between 1 and 100 (inclusive)
random_number = random.randint(1, 100)

# Print the random number
#print(random_number)

# Ask the user to guess a number
guess=int(input("Guess a number between 1 and 100: "))

# Repeat until the user guesses the correct number
while guess!=random_number:
    # Compare the user's guess to the generated number
    
    if guess < random_number:
        print("Too low!")
    else:
        print("Too high!")
        
    # Allow the user to guess again
    guess = int(input("Guess again: "))
# If the user guesses the correct number, print a message indicating that they won    
print("Congratulations, you guessed the number!")