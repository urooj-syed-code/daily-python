# password strength checker
def password_strength(password):
    if len(password) < 6:
        return "Weak"
    elif len(password) < 12:
        return "Moderate"
    else:
        return "Strong"
def get_user_password():
    while True:
        password = input("Enter your password: ").strip()
        if password:
            return password
        else:
            print("Please enter a valid password.")
def main():
    password = get_user_password()
    strength = password_strength(password)
    print(f"Your password is: {strength}")
if __name__ == "__main__":    
    main()
