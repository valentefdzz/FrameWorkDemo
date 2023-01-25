import random
import string
from typing import Final

def get_random_digit():
    random_source = string.digits
    # select 1 digit
    digit = random.choice(string.digits)

    for i in range(0):
        digit += random.choice(random_source)

    digit_list = list(digit)
    # shuffle all characters
    random.SystemRandom().shuffle(digit_list)
    password = ''.join(digit_list)
    return digit

constant_digit: Final = str(get_random_digit())

def get_random_password():
    random_source = string.ascii_letters
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)

    # generate other characters
    for i in range(7):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

constant_password: Final = str(get_random_password())+str(constant_digit)


def letter_for_email():
    # input string
    randomItem = random.choice(get_random_password())
    return randomItem

constant_letter: Final = random.choice(constant_password)

def get_random_invalid_password():
    random_source = string.ascii_letters
    # select 1 lowercase
    password = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    password += random.choice(string.ascii_uppercase)

    # generate other characters
    for i in range(8):
        password += random.choice(random_source)

    password_list = list(password)
    # shuffle all characters
    random.SystemRandom().shuffle(password_list)
    password = ''.join(password_list)
    return password

constant_invalid_password: Final = get_random_invalid_password()

def get_random_email():
    random_source = string.ascii_letters
    # select 1 lowercase
    email = random.choice(string.ascii_lowercase)
    # select 1 uppercase
    email += random.choice(string.ascii_uppercase)

    # generate other characters
    for i in range(6):
        email += random.choice(random_source)

    email_list = list(email)
    # shuffle all characters
    random.SystemRandom().shuffle(email_list)
    password = ''.join(email_list)
    return password+(constant_letter)+str("@")

constant_email: Final = get_random_email()

valid_domain = "gmail"