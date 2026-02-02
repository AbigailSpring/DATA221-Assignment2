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
word_counts = Counter(clean_tokens)
top_10 = word_counts.most_common(10)
for word, count in top_10:
    print(f"{word} -> {count}")
