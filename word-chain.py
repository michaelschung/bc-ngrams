import random

words = []

with open('txt/small2.txt', 'r') as f:
    for line in f:
        # Remove whitespace from the ends
        stripped_line = line.strip()
        # Split the line into a list of words
        line_words = stripped_line.split()
        # Add each word to our master list
        words.extend(line_words)

# Create dictionary where the keys are letters
# and the values are lists of words beginning
# with each letter
alpha_words = {}
for word in words:
    first = word[0]
    if first not in alpha_words:
        alpha_words[first] = [word]
    else:
        alpha_words[first].append(word)

# Print dictionary
# for letter in alpha_words:
#     print('{}: {}'.format(letter, alpha_words[letter]))

###### PROBLEM ######

# Given the dictionary above, generate a sentence
# of n words where each word begins with the
# last letter of the previous word

def word_chain(n):
    # Declare your current word
    word = random.choice(words)
    # Loop n times:
    for i in range(n):
        # Print current word
        print(word, end=' ')
        # Grab last letter of current word
        last = word[-1]
        # Use last letter to find next current word
        word = random.choice(alpha_words[last])
    print()

word_chain(40)
