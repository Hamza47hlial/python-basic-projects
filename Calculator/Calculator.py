import Art


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    if n2 == 0:
        return "You can't divide by 0!"
    else:
        return n1 / n2


operation = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculator():
    print(Art.logo)
    should_accumulate = True
    n1 = float(input("What's the first number? : "))

    while should_accumulate:
        for symbol in operation:
            print(symbol)
        op = input("Pick an operation : ")
        n2 = float(input("What's the second number? : "))
        result = operation[op](n1, n2)
        print(f"{n1} {op} {n2} = {result}")

        choice = input(
            f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation : ").lower()

        if choice == "y":
            n1 = result
        else:
            should_accumulate = False
            print("\n" * 50)
            calculator()


calculator()
