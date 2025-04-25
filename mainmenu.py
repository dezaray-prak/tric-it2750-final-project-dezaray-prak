import random
import string
import re

# Password Generation Function
def password_generation():
    print("\n--- Password Generator ---")

    while True:
        # Minimum password criteria
        min_length = 8
        print(f"Password must have at least {min_length} characters.")
        print("You must include at least one of each: uppercase letters, lowercase letters, numbers, and special characters.")
        
        length = input("Enter the desired password length: ")
        try:
            length = int(length)
            if length < min_length:
                print(f"Password must be at least {min_length} characters long. Please try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Asking for required characters
        use_uppercase = input("Include uppercase letters? (yes/no): ").lower() == 'yes'
        use_lowercase = input("Include lowercase letters? (yes/no): ").lower() == 'yes'
        use_numbers = input("Include numbers? (yes/no): ").lower() == 'yes'
        use_symbols = input("Include symbols? (yes/no): ").lower() == 'yes'

        # Ensure at least one character type is selected
        if not (use_uppercase or use_lowercase or use_numbers or use_symbols):
            print("You must select at least one character type. Please try again.")
            continue

        # Generate password
        all_characters = ""
        if use_uppercase:
            all_characters += string.ascii_uppercase
        if use_lowercase:
            all_characters += string.ascii_lowercase
        if use_numbers:
            all_characters += string.digits
        if use_symbols:
            all_characters += string.punctuation

        password = ''.join(random.choice(all_characters) for _ in range(length))
        print(f"Generated password: {password}")

        # Go back to the main menu
        input("\nPress Enter to return to the main menu...")

# OSINT Feature (Phone numbers and emails extraction)
def osint_feature():
    print("\n--- OSINT: Extract Phone Numbers and Emails ---")

    while True:
        filename = input("Enter the filename (with extension): ")

        try:
            with open(filename, 'r') as file:
                text = file.read()
                break  # Successfully opened the file, so break out of the loop
        except FileNotFoundError:
            print(f"The file {filename} does not exist. Please try again.")

    # Regular expression patterns for phone numbers and emails
    phone_pattern = re.compile(r'(\+?(\d{1,3}))?(\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4})')
    email_pattern = re.compile(r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}')

    # Find phone numbers and emails using the patterns
    phone_numbers = set(re.findall(phone_pattern, text))
    emails = set(re.findall(email_pattern, text))

    # Display results
    print("\n--- Results ---")
    print(f"Total phone numbers found: {len(phone_numbers)}")
    for num in phone_numbers:
        print("Phone Number:", num[0])
    
    print(f"\nTotal emails found: {len(emails)}")
    for email in emails:
        print("Email:", email)

    # Go back to the main menu
    input("\nPress Enter to return to the main menu...")

# Main Menu Function
def main_menu():
    while True:
        print("\n--- Main Menu ---")
        print("1. Password Generation")
        print("2. Find Phone Numbers and Emails (OSINT)")
        print("3. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            password_generation()  # Password generation feature
        elif choice == '2':
            osint_feature()  # OSINT feature for phone and email extraction
        elif choice == '3':
            print("Exiting...")
            break  # Exit the program
        else:
            print("Invalid choice, please try again.")

# Run the main menu
if __name__ == "__main__":
    main_menu()