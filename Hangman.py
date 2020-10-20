print("Welcome to the virtual hangman game!")
# finding a word
import random
with open('hangman_words', 'r') as word_list:
    lines = word_list.readlines()
    # Chose a random word from the file
    number = random.randint(1, 850)
    original_word = lines[number]
    word_to_guess = lines[number]

# the word is in list format so every letter is a new item in the list
word_to_guess = list(word_to_guess)
word_to_guess.remove('\n')

# create an empty list
hidden = []
# add an underscore for every letter in the word
for letter in word_to_guess:
    hidden.append('_')

# print for reference DELETE AFTER
# print(word_to_guess)
# print(hidden)

incorrect_attempts = 0
max_attempts = int(input("How many guesses would you like: "))

# loop until either the player has won or lost
game_over = False
# keep looping while the game isn't over
while not game_over:
    # print out the number of attempts remaining
    print('You have', max_attempts - incorrect_attempts, 'incorrect attempts remaining')
    hidden_string = ' '.join(hidden)
    # print how much of the word they already know
    print(hidden_string)

    # ask the player to guess a letter
    letter_guessed = input("Guess a letter: ")
    # if the letter is in the word change the hidden and word list
    if letter_guessed in word_to_guess:
        print(letter_guessed, 'was in the word!')
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == letter_guessed:
                hidden[i] = letter_guessed
                word_to_guess[i] = '_'
    # otherwise increase the incorrect attempt counter and print a message
    else:
        print(letter_guessed, "was not in the word")
        incorrect_attempts += 1

    # if the player runs out of attempts game over
    if incorrect_attempts == max_attempts:
        print("You ran out of attempts! The word was", original_word)
        print("Game Over")
        game_over = True
    # if the player has guessed the whole word print a victory message and end the game
    if (all('_' == letter for letter in word_to_guess)):
        print("Victory! You guessed the word!")
        game_over = True
