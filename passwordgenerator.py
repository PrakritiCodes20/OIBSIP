# Random password generator
import random
import string
def generate_password(length,use_letters,use_numbers,use_symbols):
   # Create the pool of characters based on user preferences 
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    # Generate the password using random choices from the pool
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password
    # user input for password generation 
length = int(input("Enter the password length:"))
use_letters = input("Include letters? (yes/no):").lower() == "yes"
use_numbers = input("Include numbers? (yes/no):").lower() == "yes"
use_symbols = input("Include special characters? (yes/no):").lower() == "yes"
    # Generate and print the password
password = generate_password(length,use_letters,use_numbers,use_symbols)
print("Generated password", password)
