


def email_validator(email):

    lambdas = [
        lambda x: "@" in x,
        lambda x: "." in x,
    ]

    validation = [lam(email) for lam in lambdas]
    if all(validation):
        return True
    return False


def password_validator(password):
    # The length of password should be over 8 digits.
    if len(password) < 8:
        return False

    # Special letters and numbers should be contained.
    lambdas = [
        lambda x: x in "!@#$%^&*()",
        lambda x: x in [str(i) for i in range(0, 9)]
    ]

    is_valid = []
    for lam in lambdas:
        if any([lam(x) for x in password]):
            is_valid.append(1)
        else:
            is_valid.append(0)

    return all(is_valid)


def phone_validator(phone):

    try:    
        if len(phone) == 11 and all([isinstance(int(num), int) for num in phone]):
            return True
    except ValueError:
        return False
    return False