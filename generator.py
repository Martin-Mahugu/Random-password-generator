import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_passwords():
    password_length = int(input("How many characters would you like your password to have? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)

    print(password)


generate_passwords()