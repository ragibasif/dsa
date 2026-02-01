def is_lowercase(c):
    return ord(c) >= ord('a') and ord(c) <= ord('z')

def is_uppercase(c):
    return ord(c) >= ord('A') and ord(c) <= ord('Z')

def is_alpha(c):
    return is_lowercase(c) or is_uppercase(c)

def is_digit(c):
    return ord(c) >= ord('0') and ord(c) <= ord('9')

def is_alphanumeric(c):
    return is_alpha(c) or is_digit(c)

def to_uppercase(c):
    if is_lowercase(c):
        return chr(ord('z') - ord(c) + ord('A'))
    return c

def to_lowercase(c):
    if is_uppercase(c):
        return chr(ord('Z') - ord(c) + ord('a'))
    return c

