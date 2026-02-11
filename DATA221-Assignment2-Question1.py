import string
from collections import Counter

with open("sample-file.txt", "r", encoding="utf-8") as file:
    text_in_file = file.read()
tokens_in_chosen_file = text_in_file.split()
clean_tokens_in_file = []
for token in tokens_in_chosen_file:
    token = token.lower()
    token = token.strip(string.punctuation)
    if sum(char.isalpha() for char in token) >= 2:
        clean_tokens_in_file.append(token)
word_counts = Counter(clean_tokens_in_file)
top_10 = word_counts.most_common(10)
for word, count in top_10:
    print(f"{word} -> {count}")