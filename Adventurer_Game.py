LOGO = r'''
                     ,@@@@@@@,
             ,,,.   ,@@@@@@/@@,  .oo8888o.
          ,&%%&%&&%,@@@@@/@@@@@@,8888\88/8o
         ,%&\%&&%&&%,@@@\@@@/@@@88\88888/88'
         %&&%&%&/%&&%@@\@@/ /@@@88888\88888'
         %&&%/ %&%%&&@@\ V /@@' `88\8 `/88'
         `&%\ ` /%&'    |.|        \ '|8'
             |o|        | |         | |
             |.|        | |         | |
      \\/ ._\//_/__/  ,\_//__\\/.  \_//__/_
'''
# Every scene is either:
#   a question: {"text": ..., "options": {answer: next_scene}}
#   an ending:  {"ending": "win" / "escape" / "dead", "text": [lines]}
story = {
    "start": {
        "text": "You're at the edge of the forest. Two paths: a dark trail "
                "and a path with a river.",
        "options": {"trail": "cabin", "river": "river"},
    },

    # --- The trail branch ---
    "cabin": {
        "text": "You walk along the trail and find an old cabin. "
                "Smoke is coming from the chimney.",
        "options": {"knock": "hermit", "sneak": "trap"},
    },
    "hermit": {
        "text": "An old hermit opens the door. He offers you a map "
                "but warns that the cave has a guardian. Do you take the map?",
        "options": {"yes": "cave", "no": "lost"},
    },
    "cave": {
        "text": "You reach the cave. The guardian, a huge bear, "
                "sleeps at the entrance.",
        "options": {"sneak": "gold", "fight": "bear", "run": "run_away"},
    },

    # --- The river branch ---
    "river": {
        "text": "You reach a wide river. There is a rickety bridge and "
                "a shallow crossing with rocks.",
        "options": {"bridge": "bridge_snaps", "rocks": "mushrooms"},
    },
    "mushrooms": {
        "text": "You cross safely and find a glowing mushroom path.",
        "options": {"follow": "chest", "ignore": "go_home"},
    },

    # --- Endings ---
    "gold": {
        "ending": "win",
        "text": ["You slip past the bear and find a chest full of gold.",
                 "YOU WIN! You are rich!"],
    },
    "chest": {
        "ending": "win",
        "text": ["The mushrooms lead you to a hidden chest under a tree.",
                 "YOU WIN! The treasure is yours!"],
    },
    "run_away": {
        "ending": "escape",
        "text": ["You run back to the forest edge, safe but empty-handed.",
                 "YOU ESCAPED! At least you're alive."],
    },
    "lost": {
        "ending": "escape",
        "text": ["Without the map, you get lost as night falls.",
                 "You find your way out at dawn, exhausted but alive.",
                 "YOU ESCAPED! No treasure, but you live."],
    },
    "go_home": {
        "ending": "escape",
        "text": ["You go back to the forest edge and head home safely.",
                 "YOU ESCAPED! No treasure, but you live."],
    },
    "trap": {
        "ending": "dead",
        "text": ["The hermit's trap catches your foot and you fall into a pit.",
                 "GAME OVER. You died."],
    },
    "bear": {
        "ending": "dead",
        "text": ["The bear wakes up and crushes you.",
                 "GAME OVER. You died."],
    },
    "bridge_snaps": {
        "ending": "dead",
        "text": ["The bridge snaps and you fall into the rushing water.",
                 "GAME OVER. You died."],
    },
}


def ask_choice(text, options):
    """Shows the scene and keeps asking until the answer is a valid option."""
    # Build the "Type ..." hint from the options, so we never write it by hand
    hint = ' or '.join(f'"{option}"' for option in options)
    while True:
        # strip() ignores accidental spaces, lower() ignores capital letters
        answer = input(f"{text}\nType {hint}.\n").strip().lower()
        if answer in options:
            return answer
        print("That's not one of the options, try again.\n")


def play():
    """Walks through the story until an ending is reached."""
    print(LOGO)
    print("Welcome to the Whispering Forest.")
    print("Legend says a treasure is hidden deep inside.")
    print("Your mission: find the treasure... and stay alive.\n")

    scene = "start"
    while True:
        node = story[scene]

        # An ending has no options: print it and stop
        if "ending" in node:
            print()
            for line in node["text"]:
                print(line)
            return node["ending"]

        answer = ask_choice(node["text"], node["options"])
        print()
        scene = node["options"][answer]  # move to the next scene


# Keep track of how the player's adventures turned out
results = {"win": 0, "escape": 0, "dead": 0}

while True:
    outcome = play()
    results[outcome] += 1
    print(f"\nWins: {results['win']} | Escapes: {results['escape']} | "
          f"Deaths: {results['dead']}")

    again = input("\nPlay again? Type 'y' or 'n' : ").strip().lower()
    if again != "y":
        print("Thanks for playing!")
        break
    print("\n" * 25)
