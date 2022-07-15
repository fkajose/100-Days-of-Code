import random
from replit import clear
from hangman_words import word_list
from hangman_art import logo, stages

chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = len(stages) - 1
print(logo)

#Create blanks
display = []
for _ in range(word_length):
    display += "_"
print(' '.join(display))

guessed_letters=[]
while lives>0:
    guess = input("Guess a letter: ").lower()
    clear()
    
    if guess in guessed_letters:
            print(f"You already guessed {guess}.")
    guessed_letters+=guess

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.

    if guess not in chosen_word:
        lives -= 1
        print(f"{guess} is not in word.")
        if lives == 1:
            print(f"You have {lives} life left.")
        elif lives == 0:
            print("You have run out of lives.")
        else:
            print(f"You have {lives} lives left.")

    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")
    print(stages[lives])

#Check if user has got all letters.
    if "_" not in display:
        lives = 0
        print("Ccongrats, you win!")
    elif lives == 0:
        print("You lose.")
        print(f'The word was {chosen_word}.')