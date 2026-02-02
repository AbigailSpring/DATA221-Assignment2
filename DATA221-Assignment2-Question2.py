import string
from collections import Counter

with open("sample-file.txt", "r", encoding="utf-8") as file:
    text = file.read()
tokens = text.split()
clean_tokens = []
for token in tokens:
    token = token.lower()
    token = token.strip(string.punctuation)
    if sum(char.isalpha() for char in token) >= 2:
        clean_tokens.append(token)
bigrams = []
for i in range(len(clean_tokens) - 1):
    bigram = clean_tokens[i] + " " + clean_tokens[i + 1]
    bigrams.append(bigram)
bigram_counts = Counter(bigrams)
top_5 = bigram_counts.most_common(5)
for bigram, count in top_5:
    print(f"{bigram} -> {count}")