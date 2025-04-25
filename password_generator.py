import random
import string

def password_generation():
    """
    Function to generate a secure password based on user specifications.
    """
    print("\n--- Password Generation ---")
    
    # Get user input for password criteria
    while True:
        try:
            min_length = int(input("Enter the minimum length of the password: "))
            if min_length < 8:
                print("Password length should be at least 8 characters. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    min_upper = int(input("Enter the minimum number of uppercase letters: "))
    min_lower = int(input("Enter the minimum number of lowercase letters: "))
    min_numbers = int(input("Enter the minimum number of numbers: "))
    min_special = int(input("Enter the minimum number of special characters: "))

    while True:
        # Generate password
        password = generate_password(min_length, min_upper, min_lower, min_numbers, min_special)
        
        # Check if password meets all criteria
        if is_valid_password(password, min_upper, min_lower, min_numbers, min_special):
            print(f"Generated password: {password}")
            break
        else:
            print("Generated password doesn't meet the requirements. Trying again...")

    input("Press Enter to return to the main menu...")

def generate_password(length, upper, lower, numbers, special):
    """
    Generates a password based on the given criteria.
    """
    # Create pools of characters to choose from
    upper_chars = string.ascii_uppercase
    lower_chars = string.ascii_lowercase
    num_chars = string.digits
    special_chars = string.punctuation

    # Ensure we meet the minimum criteria first
    password = [
        random.choice(upper_chars) for _ in range(upper)
    ] + [
        random.choice(lower_chars) for _ in range(lower)
    ] + [
        random.choice(num_chars) for _ in range(numbers)
    ] + [
        random.choice(special_chars) for _ in range(special)
    ]
    
    # Fill the rest of the password length with random characters
    remaining_length = length - len(password)
    if remaining_length > 0:
        all_chars = upper_chars + lower_chars + num_chars + special_chars
        password += random.choices(all_chars, k=remaining_length)

    # Shuffle the list to randomize the characters' order
    random.shuffle(password)
    
    # Return the password as a string
    return ''.join(password)

def is_valid_password(password, min_upper, min_lower, min_numbers, min_special):
    """
    Validates the password against the user requirements.
    """
    upper_count = sum(1 for char in password if char.isupper())
    lower_count = sum(1 for char in password if char.islower())
    num_count = sum(1 for char in password if char.isdigit())
    special_count = sum(1 for char in password if char in string.punctuation)
    
    return (upper_count >= min_upper and lower_count >= min_lower and
            num_count >= min_numbers and special_count >= min_special)
