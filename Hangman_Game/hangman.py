import random
from hangman_words import word_list
from hangman_art import stages, logo

lives = 6

print(logo)

chosen_word = random.choice(word_list)

# Build a string of underscores, one for each letter in the word
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess : " + placeholder)

game_over = False
correct_letters = []  # every letter the player has guessed correctly so far

while not game_over:

    print(
        f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter : ").lower()

    if guess in correct_letters:
        print(f"You've already guessed {guess}")

    # Rebuild the display from scratch every round
    display = ""

    for letter in chosen_word:
        if letter == guess:
            # The guess matches this position: reveal it and remember it
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            # Guessed in an earlier round, so keep it revealed
            display += letter
        else:
            display += "_"

    print("Word to guess : " + display)

    # Wrong guess: lose a life, and end the game if none are left
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True

            print(
                f"***********************IT WAS {chosen_word}! YOU LOSE**********************")

    # No underscores left means every letter has been found
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    # Show the hangman drawing that matches the lives left
    print(stages[lives])