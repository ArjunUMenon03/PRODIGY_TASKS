import re

def password_strength_checker(password):
    # Initialize variables to check password criteria
    length = len(password)
    has_upper = bool(re.search(r'[A-Z]', password))
    has_lower = bool(re.search(r'[a-z]', password))
    has_digit = bool(re.search(r'\d', password))
    has_special = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Criteria for password strength
    criteria = {
        'Length >= 8': length >= 8,
        'Contains uppercase letter': has_upper,
        'Contains lowercase letter': has_lower,
        'Contains digit': has_digit,
        'Contains special character': has_special
    }

    # Count the number of criteria met
    criteria_met = sum(criteria.values())

    # Determine the password strength
    if criteria_met == 5:
        strength = 'Very Strong'
    elif criteria_met == 4:
        strength = 'Strong'
    elif criteria_met == 3:
        strength = 'Medium'
    elif criteria_met == 2:
        strength = 'Weak'
    else:
        strength = 'Very Weak'

    # Provide feedback to the user
    feedback = f'Password Strength: {strength}\n'
    feedback += 'Criteria met:\n'
    for criterion, met in criteria.items():
        feedback += f'{criterion}: {"✔" if met else "✘"}\n'

    return feedback

# Test the password strength checker
password = input("Enter a password to check its strength: ")
print(password_strength_checker(password))
