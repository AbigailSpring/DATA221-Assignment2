import string
from collections import defaultdict
import string

with open("sample-file.txt", "r", encoding="utf-8") as input_file:
    all_lines = input_file.readlines()
normalized_line_map = defaultdict(list)
for line_number, original_line in enumerate(all_lines, start=1):
    normalized_line = original_line.lower()
    normalized_line = "".join(normalized_line.split())
    normalized_line = normalized_line.translate(
        str.maketrans("", "", string.punctuation))
    normalized_line_map[normalized_line].append(
        (line_number, original_line.strip()))
near_duplicate_groups = [
    line_group
    for line_group in normalized_line_map.values()
    if len(line_group) > 1]
print(f"Number of near-duplicate sets: {len(near_duplicate_groups)}")

for group_index, duplicate_group in enumerate(near_duplicate_groups[:2], start=1):
    print(f"\nSet {group_index}:")
    for line_number, line_text in duplicate_group:
        print(f"{line_number}: {line_text}")