import random

# Read in all the words in one go
#with open(r"C:\Users\joelc\desktop\lambda-cs\cs-module-project-hash-tables\applications\markov\input.txt") as f:
#    words = f.read()
#words = words.lower()

words = open(r"C:\Users\joelc\desktop\lambda-cs\cs-module-project-hash-tables\applications\markov\input.txt").read().lower().split()



# TODO: analyze which words can follow other words
# Your code here
cache = {}

for i in range(0, len(words) - 1):
    if words[i] not in cache:
        cache[words[i]] = []
        cache[words[i]].append(words[i+1])
    else:
        cache[words[i]].append(words[i+1])

def giberish(word, length, sentance = "", count = 1):
    if count >= length:
        sentance = f'{sentance} {word}'
    else:
        rand = random.randrange(0, len(cache[word]))
        next_word = cache[word][rand]
        sentance = f'{sentance} {word} {giberish(next_word, length, sentance,  count + 1)}'
    return sentance

# TODO: construct 5 random sentences
# Your code here
print(giberish('and', 5))
print(giberish('because', 25))