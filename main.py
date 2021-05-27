import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

print(logo)
#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
a = []
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    clear()

    if guess in a:
        print(f"You've already guessed {guess}")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]

        if letter == guess:
            display[position] = letter
            a.append(guess)

    #Check if user is wrong.
    if guess not in chosen_word:

        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
        else:
            print(
                f"You guessed {guess}, that is not in the word. You lose a life"
            )

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[lives])
print(f"The word is {chosen_word}")
