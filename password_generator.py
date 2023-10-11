import random
import string
from cryptography.fernet import Fernet

# Generate a key for encryption
key = Fernet.generate_key()
cipher_suite = Fernet(key)


# Function to generate a secure password
def generate_password(min_length, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special

    pwd = ""
    meets_criteria = False
    has_number = False
    has_special = False

    while not meets_criteria or len(pwd) < min_length:
        new_char = random.choice(characters)
        pwd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meets_criteria = True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria = meets_criteria and has_special

    return pwd


# Function to securely store and encrypt passwords along with website information
def store_password(website, password):
    encrypted_data = cipher_suite.encrypt(f"{website}:{password}".encode())
    with open("vault", "ab") as f:
        f.write(encrypted_data + b'\n')

# Function to delete a password based on the website
def delete_password(website):
    passwords = get_passwords()
    updated_passwords = []
    deleted = False

    for stored_website, stored_password in passwords:
        if stored_website.lower() == website.lower():
            deleted = True
            print(f"Password for '{website}' has been deleted.")
        else:
            updated_passwords.append((stored_website, stored_password))

    if not deleted:
        print(f"No password found for '{website}'.")

    # Rewrite the vault file with updated passwords
    with open("vault", "wb") as f:
        for stored_website, stored_password in updated_passwords:
            encrypted_data = cipher_suite.encrypt(f"{stored_website}:{stored_password}".encode())
            f.write(encrypted_data + b'\n')

# Function to decrypt and retrieve passwords along with website information
def get_passwords():
    with open("vault", "rb") as f:
        encrypted_passwords = f.readlines()

    decrypted_passwords = []
    for encrypted_password in encrypted_passwords:
        decrypted_data = cipher_suite.decrypt(encrypted_password).decode()
        website, password = decrypted_data.strip().split(":")
        decrypted_passwords.append((website, password))
    return decrypted_passwords


while True:
    print("\nMenu:")
    print("1. Generate a new password")
    print("2. Retrieve passwords from the vault")
    print("3. Delete a password")
    print("4. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        min_length = int(input("Enter the minimum length you require for the password: "))
        has_number = input("Do you want to include numbers (Y/N)? ").lower() == "y"
        has_special = input("Do you want to include special characters (Y/N)? ").lower() == "y"
        website = input("Enter the website associated with the password: ")

        # Generate and store a new password along with the associated website
        pwd = generate_password(min_length, has_number, has_special)
        store_password(website, pwd)
        print("Password has been securely stored for the website:", website)

    elif choice == "2":
        # Retrieve and display stored passwords along with associated websites
        stored_passwords = get_passwords()
        print("\nStored Passwords:")
        for stored_website, stored_password in stored_passwords:
            print(f"Website: {stored_website}, Password: {stored_password}")

    elif choice == "3":
        website_to_delete = input("Enter the website for which you want to delete the password: ")
        delete_password(website_to_delete)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice. Please try again.")