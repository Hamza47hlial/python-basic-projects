import art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    # Return None so the calculator can tell "this failed" apart from a real number
    if n2 == 0:
        return None
    return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def get_number(prompt):
    """Keeps asking until the user types a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            # float() raises ValueError when the text isn't a number
            print("That's not a valid number, try again.")


def get_operation():
    """Keeps asking until the user picks a symbol that exists."""
    while True:
        for symbol in operation:
            print(symbol)
        op = input("Pick an operation : ")
        if op in operation:  # checking first avoids the KeyError
            return op
        print("That's not a valid operation, try again.")


def calculator():
    print(art.logo)
    n1 = get_number("What's the first number? : ")
    should_accumulate = True

    while should_accumulate:
        op = get_operation()
        n2 = get_number("What's the second number? : ")
        result = operation[op](n1, n2)

        # Failed division: show the error and ask again, keeping n1 so the user doesn't lose their progress
        if result is None:
            print("You can't divide by 0! Try again.")
            continue

        print(f"{n1} {op} {n2} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ").lower()

        if choice == "y":
            n1 = result
        else:
            should_accumulate = False


# A loop replaces the old recursion: each new calculation starts fresh without stacking function calls on top of each other
while True:
    calculator()
    print("\n" * 50)  # clear the screen before the next calculation
