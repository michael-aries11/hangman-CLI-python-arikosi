import random
from hangman_art import logo, stages, loser, winner
from hangman_words import word_list
# import only system from os
from os import system, name

# import sleep to show output for some time period
from time import sleep

# define our clear function


def clear():

    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


word_list = ["advark", "sphinx", "mouse"]
display = []

chosen_word = random.choice(word_list)

word_length = len(chosen_word)


for _ in range(word_length):
    display += "#"

lives = 6

# end_of_game = False

# while not end_of_game:
#     guess = (input("Guess a letter in the word.. ")).lower()

#     for position in range(word_length):
#         if chosen_word[position] == guess:
#             display[position] = guess
#     print(f"The evaluated string is  {display}")

#     if "_" not in display:
#         end_of_game = True
#         print("You win :)")

# while lives > 0:
#     guess = (input("Guess a letter in the word.. ")).lower()

#     if guess in chosen_word:
#         print('You guessed correctly')
#         for position in range(word_length):
#             if chosen_word[position] == guess:
#                 display[position] = guess

#     else:
#         print('You made an incorrect guess, so you lose a life')
#         print(stages[lives-1])
#         lives -= 1
#         print(f'Lives left => {lives}')
#         if lives == 0:
#             print('GAME OVER. You LOSE!!')

#     print(" ".join(display))

#     if "#" not in display:
#         print(f"You win  with {lives} lives left:)")
#         lives = -1

end_of_game = False
print(logo)
print(chosen_word)
while not end_of_game:
    guess = (input("Guess a letter in the word.. ")).lower()
    clear()
    if guess in chosen_word:
        print('You guessed correctly')
        for position in range(word_length):
            if chosen_word[position] == guess:
                display[position] = guess

    elif guess in display:
        print(f'You already guessed the letter {guess}. Try again')

    else:
        print('You made an incorrect guess, so you lose a life')
        print(stages[lives])
        lives -= 1

        print(f'Lives left => {lives}')
        if lives == 0:
            # print('GAME OVER. You LOSE!!')
            print(loser)

            end_of_game = True

    print(" ".join(display))

    if "#" not in display:
        print(f"You win  with {lives} lives left:)")
        print(winner)
        end_of_game = True
