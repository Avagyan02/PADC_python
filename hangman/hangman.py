import random
import time
from hangman_ui import hangman_ui

class ThemeAndWords:
    def __init__(self):
        self.word = None
        self.theme = None
        self.themes = {
            "pets": ["dog", "cat", "cow", "horse", "chicken"],
            "wild": ["lion", "tiger", "crocodile", "wolf"],
            "countries": ["russia", "denmark", "croatia", "argentina"]
        }

    # get random theme and word
    def get_theme_and_word(self):
        self.theme, value = random.choice(list(self.themes.items()))
        self.word = random.choice(value)


class StartTheGame:
    def __init__(self):
        theme_and_words = ThemeAndWords()
        theme_and_words.get_theme_and_word()
        self.theme = theme_and_words.theme
        self.word = theme_and_words.word

        self.start_the_game()
        self.write_word_letters()

    def start_the_game(self):
        print('Starting the game...')
        time.sleep(2)
        self.replace_word = len(self.word) * "_ "
        print('The theme is ', self.theme)
        print('Word is ', self.replace_word)

    def write_word_letters(self):
        misstakes_count = 0

        while True:
            # validation users inserted data
            if misstakes_count == len(hangman_ui):
                print('The word was ' + self.word)
                print('Game over')
                break

            letter = input("Write the letter ").lower()

            if len(letter) != 1 or letter.isdigit():
                print('Enter a valid letter')
                continue

            if letter.lower() not in self.word:
                print("Not correct letter, try again")
                print(hangman_ui[misstakes_count])
                misstakes_count += 1
                continue

            if (
                    letter.lower() in self.replace_word and
                    self.word.count(letter.lower()) == self.replace_word.count(letter.lower())
                ):
                print('Letter already added')
                continue

            r_index = self.word.rfind(letter)
            l_index = self.word.find(letter)

            # replace for show user his inserted letters
            if r_index != l_index:
                self.replace_word = (
                    self.replace_word[0:l_index * 2] + letter + self.replace_word[l_index * 2 + 1::]
                )
                self.replace_word = (
                    self.replace_word[0:r_index * 2] + letter + self.replace_word[r_index * 2 + 1::]
                )
            else:
                self.replace_word = (
                    self.replace_word[0:l_index * 2] + letter + self.replace_word[l_index * 2 + 1::]
                )

            if self.replace_word.count('_') > 0:
                print(self.replace_word)
                continue

            if self.replace_word.count('_') == 0:
                print("Congratulations you won")
                print("The word was " + self.word[0].upper() + self.word[1::])
                break