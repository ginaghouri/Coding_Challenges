# A code to generate a positive affirmation
import random

# A list of positive affirmations
affirmations = [
    "You are strong and resilient.",
    "You are worthy and deserving of respect.",
    "You are handsome and unique.",
    "You are capable and competent.",
    "You are brave and courageous.",
    "You are smart and creative.",
    "You are kind and compassionate.",
    "You are optimistic and hopeful.",
    "You are fun and adventurous.",
    "You are loyal and trustworthy."
]

# A function to randomly select an affirmation
def choose_affirmation():
    return random.choice(affirmations)

# A function to print the affirmation
def print_affirmation():
    print("Your affirmation for today is:")
    print(choose_affirmation())

# Call the function
print_affirmation()