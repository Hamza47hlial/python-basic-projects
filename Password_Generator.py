import secrets
import random

letters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
numbers = list("0123456789")
symbols = list("!#$%&()*+")


def get_count(prompt):
    """Keeps asking until the user types a whole number that is 0 or more."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")
            continue
        if value < 0:
            print("The number can't be negative, try again.")
            continue
        return value


def generate_password(nr_letters, nr_symbols, nr_numbers):
    password_list = []

    # secrets.choice is the secure version of random.choice, so the password is safe to actually use
    for _ in range(nr_letters):
        password_list.append(secrets.choice(letters))
    for _ in range(nr_symbols):
        password_list.append(secrets.choice(symbols))
    for _ in range(nr_numbers):
        password_list.append(secrets.choice(numbers))

    # SystemRandom().shuffle is the secure version of random.shuffle
    random.SystemRandom().shuffle(password_list)

    # join() glues all the characters into one string
    return "".join(password_list)


print("Welcome to the Password Generator!")

while True:
    nr_letters = get_count("How many letters would you like in your password?\n")
    nr_symbols = get_count("How many symbols would you like?\n")
    nr_numbers = get_count("How many numbers would you like?\n")

    # An empty password is useless, so ask again if everything is 0
    if nr_letters + nr_symbols + nr_numbers == 0:
        print("Your password needs at least one character. Let's try again.\n")
        continue
    break

password = generate_password(nr_letters, nr_symbols, nr_numbers)
print(f"Your password is : {password}")