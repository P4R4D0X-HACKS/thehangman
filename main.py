import random
from hangman_word import word_list
from hangman_art import stages, logo

print(logo)
life = 6
# randomly choose a word form the list
chosen_word = random.choice(word_list)
# creating an empty list for each letter in chosen word adding "_"
display = []
word_len = len(chosen_word)
for letter in range(word_len):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:
    # ask the user to guess a letter and assign their answer to a variable called guess. Make the guess lowercase
    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You've already guessed {guess}")
    # replacing the underscore with the letter that the user choose if it is right
    for position in range(word_len):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        life -= 1
        if life == 0:
            end_of_game = True
            print("You Lose!")
            print(f"The correct word was {chosen_word}")
    print(display)
    if "_" not in display:
        end_of_game = True
        print("You Win!")
    print(stages[life])
