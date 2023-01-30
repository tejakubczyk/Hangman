# Step 1
import random
import hangman_words
import hangman_art

letters_list = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]


word_list = hangman_words.word_list
word_picked = random.choice(word_list)

print(hangman_art.logo)

# Testing code
#print(f'Pssst, the solution is {word_picked}.')

# Create blanks
word_display_list = []

for char in word_picked:
    word_display_list.append("_")

basic_word_display = "".join(word_display_list)
print(basic_word_display)

# print(word_display_list)

word_length = len(word_picked)
word_display = ""

lives = len(hangman_art.stages)

chosen_letters = []

while word_picked != word_display:
    word_display = ""
    letter = input("Guess a letter: ").lower()

    if letter not in letters_list:
        print("Please, type a letter.")
        continue

    for char in range(0, word_length):
        if word_picked[char] == letter:
            word_display_list[char] = letter

    if letter not in word_picked:
        if letter in chosen_letters:
            print(f"You've already chosen letter {letter}.")
        else:
            print(f"The word does not contain letter {letter}. You lose a life.")
            lives -= 1
            if lives == 0:
                print(hangman_art.stages[0])
                print("You lost.")
                break

    chosen_letters.append(letter)

    word_display = ''.join(word_display_list)
    print(word_display)

    if word_picked == word_display:
        print("You win.")
    print(hangman_art.stages[lives])
    print("#####################################################################################################")
