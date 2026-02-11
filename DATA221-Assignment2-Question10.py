def find_lines_with_keyword(file_path, search_keyword):
    matching_lines = []
    search_keyword_lower = search_keyword.lower()
    with open(file_path, "r", encoding="utf-8") as input_file:
        for line_number, line_text in enumerate(input_file, start=1):
            if search_keyword_lower in line_text.lower():
                matching_lines.append((line_number, line_text.strip()))
    return matching_lines
keyword_matches = find_lines_with_keyword("sample-file.txt", "lorem")
print(f"Number of matching lines: {len(keyword_matches)}")
print("\nFirst 3 matching lines:")
for line_number, line_text in keyword_matches[:3]:
    print(f"{line_number}: {line_text}")