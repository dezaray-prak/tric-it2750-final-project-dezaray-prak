import re

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
