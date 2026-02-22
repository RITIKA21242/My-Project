import re


COMMON_PASSWORDS = [
    "password", "123456", "12345678", "qwerty",
    "abc123", "password123", "admin", "letmein"
]

def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        feedback.append("Add at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        feedback.append("Add at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        score = 0
        feedback.append("This password is too common.")

    return score, feedback


def get_strength_label(score):
    if score <= 2:
        return "Weak"
    elif score <= 4:
        return "Medium"
    else:
        return "Strong"

if __name__ == "__main__":
    print("🔐 Password Strength Checker 🔐")
    password = input("Enter a password: ")

    score, feedback = check_password_strength(password)
    strength = get_strength_label(score)

    print("\nPassword Strength:", strength)
    print("Score:", score, "/ 5")

    if feedback:
        print("\nSuggestions to improve your password:")
        for item in feedback:
            print("-", item)
    else:
        print("Your password is strong!")
