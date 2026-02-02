import string
from collections import defaultdict

with open("sample-file.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
normalized_map = defaultdict(list)
for index, line in enumerate(lines, start=1):
    normalized = line.lower()
    normalized = "".join(normalized.split())
    normalized = normalized.translate(str.maketrans("", "", string.punctuation))
    normalized_map[normalized].append((index, line.strip()))
near_duplicate_sets = [
    group for group in normalized_map.values() if len(group) > 1]
print(f"Number of near-duplicate sets: {len(near_duplicate_sets)}")
for i, group in enumerate(near_duplicate_sets[:2], start=1):
    print(f"\nSet {i}:")
    for line_num, text in group:
        print(f"{line_num}: {text}")