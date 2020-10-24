import re

def validatePasswordContent(inputPassword, allowedChars):
    return validateContent(inputPassword, allowedChars)

def validateLoginContent(inputLogin, allowedChars):
    return validateContent(inputLogin, allowedChars)


def validateContent(input, allowedChars):
    match = re.match(allowedChars, input)
    return not (match is None)