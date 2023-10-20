import random

words = []

with open('txt/constitution.txt', 'r') as f:
    for line in f:
        # Remove whitespace from the ends
        stripped_line = line.strip()
        # Split the line into a list of words
        line_words = stripped_line.split()
        # Add each word to our master list
        words.extend(line_words)

next_options = {}

for i in range(len(words)-2):
    bigram = (words[i], words[i+1])
    next_word = words[i+2]
    if bigram not in next_options:
        next_options[bigram] = [next_word]
    else:
        next_options[bigram].append(next_word)

# Uncomment the next two lines to see a full
# print of the entire probabilistic model
# for key in sorted(next_options):
#     print('{}: {}'.format(key, next_options[key]))

def generate_sentence(n):
    print()
    # Declare current bigram
    bigram = random.choice(list(next_options.keys()))
    # Print words in current bigram
    print(bigram[0] + ' ' + bigram[1], end=' ')
    # Loop n times:
    for i in range(n):
        # Use current bigram to look up list of possible next words, and pick random next word from that list, store in variable called `next`
        next = random.choice(next_options[bigram])
        # Print `next`
        print(next, end=' ')
        # Use `next` to create new current bigram
        bigram = (bigram[1], next)
    print('\n')

generate_sentence(100)
