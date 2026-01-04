def check_password(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%^&*()" for c in password):
        score += 1

    return score

def login():
    pass

while True:
    print("\n--- Python Password Security Tool ---")
    print("1. Check Password")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        score = check_password(pwd)

        if score <= 2:
            print(f"Password Strength: WEAK ({score}/5)")
        elif score <= 4:
            print(f"Password Strength: MEDIUM ({score}/5)")
        else:
            print(f"Password Strength: STRONG ({score}/5)")

    elif choice == "2":
        print("Login feature will be implemented later.")

    elif choice == "3":
        print("Program exited.")
        break

    else:
        print("Invalid choice! Try again.")