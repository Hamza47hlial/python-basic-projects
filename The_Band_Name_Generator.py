print("Welcome to the Band Name Generator.")


def ask(prompt):
    """Keeps asking until the user types something that isn't empty."""
    while True:
        # strip() removes accidental spaces at the start and end
        answer = input(prompt).strip()
        if answer:
            return answer
        print("Please type something, try again.")


while True:
    mood = ask("What vibe should your band have? (dark, happy, wild, chill...) \n")
    # "thing" instead of "object", so we don't hide Python's built-in name
    thing = ask("Name an object or thing you think sounds cool : \n")

    # title() capitalizes each word, so "dark moon" becomes "Dark Moon"
    band_name = f"{mood} {thing}".title()
    print(f"Your band name could be : {band_name}")

    again = input("\nWant another name? Type 'y' or 'n' : ").lower()
    if again != "y":
        # Prints a fun goodbye message when the user decides to stop generating band names
        print("Rock on! 🤘")
        break
