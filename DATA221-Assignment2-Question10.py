def find_lines_containing(filename, keyword):
    results = []
    keyword_lower = keyword.lower()

    with open(filename, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, start=1):
            if keyword_lower in line.lower():
                results.append((i, line.strip()))
    return results
matches = find_lines_containing("sample-file.txt", "lorem")
print(f"Number of matching lines: {len(matches)}")
print("\nFirst 3 matching lines:")
for line_number, line_text in matches[:3]:
    print(f"{line_number}: {line_text}")