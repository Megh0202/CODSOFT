import random  # Import the random module for generating random choices
import string # Import the string module to access letters, digits, and special char

def generate_password(length):
    # Define the character set
    characters = string.ascii_letters + string.digits + string.punctuation
     # Use random.choices() to generate a password of the given length
    return ''.join(random.choices(characters, k=length))

def main():
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            print("Please enter a positive number.")
        else:
            print("Generated Password:", generate_password(length))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
# Run the main function
if __name__ == "__main__":
    main()
