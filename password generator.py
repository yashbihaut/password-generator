import random
import string

def generate_password(length, use_uppercase, use_digits, use_special):
    characters = string.ascii_lowercase  
    
    if use_uppercase:
        characters += string.ascii_uppercase 
    if use_digits:
        characters += string.digits  
    if use_special:
        characters += string.punctuation  

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# User Input
length = int(input("Enter the desired length of the password: "))
use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
use_digits = input("Include digits? (y/n): ").lower() == 'y'
use_special = input("Include special characters? (y/n): ").lower() == 'y'

# Generate and display the password
generated_password = generate_password(length, use_uppercase, use_digits, use_special)
print("Generated Password:", generated_password)