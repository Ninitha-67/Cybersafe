import re

def check_password_strength(password):
    length = len(password)
    lower = re.search("[a-z]", password)
    upper = re.search ("[A-Z]", password)
    digit = re.search("[0-9]", password)
    symbol = re.search("[@#$%^&*+=]",password)

    score = sum([bool(lower), bool(upper), bool(digit), bool(symbol)])

    if length >= 8 and score >= 3:
        return "Strong password"
    elif length >= 6 and score >= 2:
        return "Moderate passworde"
    else:
        return "Weak passsword"
    
if __name__ == "__main__":
    pwd = input("Enter password to check: ")
    print(check_password_strength(pwd))