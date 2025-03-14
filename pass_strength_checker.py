import re

def check_password_strength(password):
    """
    Check the strength of a password based on the following rules:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one digit
    - Contains at least one special character
    """
    # Check length
    if len(password) < 8:
        return "Weak: Password should be at least 8 characters long."

    # Check for uppercase letters
    if not re.search(r'[A-Z]', password):
        return "Weak: Password should contain at least one uppercase letter."

    # Check for lowercase letters
    if not re.search(r'[a-z]', password):
        return "Weak: Password should contain at least one lowercase letter."

    # Check for digits
    if not re.search(r'[0-9]', password):
        return "Weak: Password should contain at least one digit."

    # Check for special characters
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        return "Weak: Password should contain at least one special character."

    return "Strong: Password meets all strength requirements."

def main():
    print("Welcome to the Password Strength Checker!")
    password = input("Enter your password: ")
    result = check_password_strength(password)
    print(result)

if __name__ == "__main__":
    main()
