import random
import string

def generate_password(length):
    """Generate a random password of given length"""
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))

# Get user inputs for number and length of passwords
num_passwords = int(input("Enter the number of passwords to generate: "))
password_length = int(input("Enter the length of each password: "))

# Generate the passwords and print them out
print("Generated Passwords:")
for i in range(num_passwords):
    password = generate_password(password_length)
    print(password)
