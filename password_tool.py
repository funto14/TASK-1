import re

def check_password_strength(password):
    feedback = []
    strength = 0
    
    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password must be at least 8 characters long.")
    
    if re.search(r'[a-z]', password) and re.search(r'[A-Z]', password):
        strength += 1
    else:
        feedback.append("Password must contain both uppercase and lowercase letters.")
    
    if re.search(r'[0-9]', password):
        strength += 1
    else:
        feedback.append("Password must contain at least one numeric digit.")
    
    if re.search(r'[\W_]', password):
        strength += 1
    else:
        feedback.append("Password must contain at least one special character (e.g., !@#$%^&*()).")

    if strength == 4:
        feedback.append("Password is strong!")
    elif strength == 3:
        feedback.append("Password is medium strength.")
    else:
        feedback.append("Password is weak.")
    
    return feedback

password = input("Enter a password to check its strength: ")


feedback = check_password_strength(password)


for message in feedback:
    print(message)
