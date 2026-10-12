import art
print(art.logo)


def find_highest_bidder(bids):
    # max() loops over the dictionary's keys (the names)
    # key=bids.get tells it to compare them by their values (the bid amounts),so it returns the NAME with the highest bid
    winner = max(bids, key=bids.get)
    print(f"The winner is {winner} with a bid of ${bids[winner]}.")


# Dictionary that stores each bidder: {name: bid}
auction = {}

# Keep collecting bids until someone says there are no more bidders
while True:
    name = input("What is your name? ")
    # int() turns the text into a number
    price = int(input("What is your bid? $"))
    auction[name] = price

    choice = input(
        "Are there any other bidders? Type 'yes' or 'no' : ").lower()
    if choice == "no":
        break  # stop asking and go pick the winner
    elif choice == "yes":
        # Print 100 blank lines to hide the previous bid (it's a *secret* auction)
        print("\n" * 100)

find_highest_bidder(auction)
