def get_number(prompt, minimum=0, allow_zero=True, as_int=False):
    """Keeps asking until the user types a valid number that is allowed."""
    while True:
        try:
            # Get input from the user and convert it to an integer if as_int is True, otherwise convert it to a decimal number (float). 'A if condition else B'
            value = int(input(prompt)) if as_int else float(input(prompt))
        except ValueError:
            print("That's not a valid number, try again.")
            continue
        if value < minimum or (value == minimum and not allow_zero):
            print("That number isn't allowed here, try again.")
            continue
        return value


def calculate_share(bill, tip, people):
    """Returns how much each person pays, tip included."""
    # 1 + tip / 100 turns a percentage into a multiplier (10% -> 1.10)
    return (bill / people) * (1 + tip / 100)


print("Welcome to the Tip Calculator!")

while True:
    # The bill must be more than 0, the tip can be 0, and at least 1 person is needed
    bill = get_number("What was the total bill? $", allow_zero=False)
    # float() allows decimal tips like 12.5
    tip = get_number(
        "What percentage (5,10,12,15..) tip would you like to give? ")
    # as_int=True because you can't split a bill between 2.5 people
    people = get_number("How many people to split the bill? ",
                        allow_zero=False, as_int=True)

    pay = calculate_share(bill, tip, people)

    # :.2f always shows two decimals, so you get $33.60 instead of $33.6
    print(f"Each person should pay : ${pay:.2f}")

    again = input("\nCalculate another bill? Type 'y' or 'n' : ").lower()
    if again != "y":
        print("Thanks for using the Tip Calculator!")
        break
