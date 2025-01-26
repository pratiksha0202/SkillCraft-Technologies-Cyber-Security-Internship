import re

def assess_password_strength(password):
    criteria = {
        "length": len(password) >= 8,
        "uppercase": bool(re.search(r"[A-Z]", password)),
        "lowercase": bool(re.search(r"[a-z]", password)),
        "numbers": bool(re.search(r"[0-9]", password)),
        "special_characters": bool(re.search(r"[!@#$%^&*(),.?\":{}|<>]", password))
    }

    strength_score = sum(criteria.values())

    if strength_score == 5:
        strength = "Strong"
    elif 3 <= strength_score < 5:
        strength = "Moderate"
    else:
        strength = "Weak"

    return strength, criteria

def main():
    print("Password Strength Assessment Tool")
    while True:
        password = input("\nEnter a password to assess its strength (or type 'exit' to quit): ")
        if password.lower() == 'exit':
            print("Exiting the tool. Goodbye!")
            break

        strength, criteria = assess_password_strength(password)
        print(f"\nPassword Strength: {strength}")
        print("Criteria Assessment:")
        for criterion, met in criteria.items():
            print(f"  {criterion.capitalize()}: {'✔' if met else '✘'}")

if __name__ == "__main__":
    main()
