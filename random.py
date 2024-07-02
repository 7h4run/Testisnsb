import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 characters to include all character sets.")

    # Define the character sets to include in the password
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure the password contains at least one character from each set
    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining length of the password with random characters from all sets
    all_characters = lower + upper + digits + symbols
    password += random.choices(all_characters, k=length-4)

    # Shuffle the password list to avoid predictable patterns
    random.shuffle(password)

    # Convert the list to a string and return it
    return ''.join(password)

# Specify the desired length of the password
password_length = 12
password = generate_password(password_length)
print(f"Generated password: {password}")
