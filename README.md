# Password Manager

Password Manager is a command-line Python script designed to help users securely generate, store, retrieve, and delete passwords for various websites or services. It provides a convenient way to manage complex passwords without remembering them, enhancing overall online security.

## Features

- **Password Generation:** The password generator creates strong and unique passwords based on user-defined criteria, including minimum length, inclusion of numbers, and special characters.

- **Password Storage and Encryption:** Generated passwords are securely stored in an encrypted file (vault) using the Fernet encryption method from the cryptography library. This ensures that sensitive information remains protected.

- **Password Retrieval:** Stored passwords, along with their associated website information, can be retrieved and displayed in the terminal. This feature allows users to access their passwords quickly when needed.

- **Password Deletion:** Users can delete stored passwords based on the associated website. This functionality helps in managing and updating stored credentials as needed.

## Prerequisites

- **Python 3.x:** Ensure you have Python 3.x installed on your system.
- **Required Packages:** Install the required Python packages using the following command:
pip install cryptography

## How to Use

1. **Clone the Repository:**
git clone [REPO_URL]

2. **Run the Script:**
python password.manager.py


3. **Usage Instructions:**
- **Generate a New Password:**
  - Enter the minimum length for the password.
  - Choose whether to include numbers and special characters.
  - Provide the website associated with the password.
- **Retrieve Passwords:**
  - View a list of stored passwords along with their respective websites.
- **Delete a Password:**
  - Enter the website for which you want to delete the password. The script will confirm the deletion.
- **Exit:**
  - Quit the application.

## Example Usage

### Generating a Password
![image](https://github.com/Andresa1897/PasswordManager-Vault/assets/98703359/d14e1075-1f06-47cd-acd7-55f46c5930e8)

### Retrieving Passwords
![image](https://github.com/Andresa1897/PasswordManager-Vault/assets/98703359/e4ddbb38-c965-48fd-82f2-0b7bb7814b03)

### Deleting a Password
![image](https://github.com/Andresa1897/PasswordManager-Vault/assets/98703359/c96fa929-96eb-4557-a77e-137f8c88fe86)

## Disclaimer

The developers of this script are not responsible for any misuse or damage caused by this tool. Use it responsibly and adhere to legal regulations and ethical standards.
