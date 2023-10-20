import random

words = []

with open('txt/tswift.txt', 'r') as f:
    for line in f:
        # Remove whitespace from the ends
        stripped_line = line.strip()
        # Split the line into a list of words
        line_words = stripped_line.split()
        # Add each word to our master list
        words.extend(line_words)

###### PROBLEM ######

# Given the above list of words, which has been read in from a file, generate a “sentence” of 20 words by repeatedly choosing a random word from the list.

# words = ['one', 'two', 'three', 'four', 'five']

def random_sentence(n):
    for i in range(n):
        # 1) Grab a random word
        random_word = random.choice(words)
        # 2) Remove word from the list
        words.remove(random_word)
        # 3) Print the chosen word
        print(random_word, end=' ')
    print()

random_sentence(100)
