import random

word_list = ["aardvark", "baboon", "camel"]

#TODO-1 

chosen_word = random.choice(word_list)
display = []
word_length = len(chosen_word)
for _ in range(len(chosen_word)):
    display += "_"

#TODO-2 

print(display)

guess = input("Select a letter: ").lower()

#TODO-3 

for position in range(word_length):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)