Question 1
Read a text file, split it into words, clean each word by lowercasing and removing punctuation, keep only words with at least two letters, and count the frequency of each word. Prints the 10 most frequent words.

Question 2
Similar to Question 1, but constructs bigrams (pairs of consecutive words) from the cleaned text and counts their frequency. Prints the 5 most frequent bigrams.

Question 3
Detects near-duplicate lines in a text file by normalizing them (lowercase, removing whitespace and punctuation). Identifies sets of lines that are identical after normalization and prints the first two sets with line numbers and original text.

Question 4
Filters a student dataset (student.csv) for high engagement: students with studytime ≥ 3, internet access, and ≤ 5 absences. Saves the filtered data to high_engagement.csv and prints the number of students and their average grade.

Question 5
Adds a grade_band column to student.csv (Low: ≤9, Medium: 10–14, High: ≥15), generates a summary table showing the number of students, average absences, and percentage with internet for each band, and saves the table to student_bands.csv.

Question 6
Creates a risk category in crime.csv based on ViolentCrimesPerPop (≥0.50 → HighCrime, otherwise LowCrime). Groups data by risk and calculates the average unemployment rate for each group, printing the results clearly.

Question 7
Scrapes the Wikipedia Data Science page, extracts the page title from the <title> tag, and retrieves the first paragraph of the main content (≥50 characters) for display.

Question 8
Extracts all h2 section headings from the Wikipedia Data Science page (main content area), removes [edit] text, excludes headings like References or External links, and saves the headings to headings.txt, preserving their order.

Question 9
Scrapes the Wikipedia Machine Learning page, locates the first table with at least three data rows, extracts headers (or generates default ones if missing), pads rows with missing values, and saves the table to wiki_table.csv.

Question 10
Defines a reusable function find_lines_containing(filename, keyword) that searches a text file for lines containing a given keyword (case-insensitive). Returns line numbers and text. Prints the total matches and the first three results when tested with sample-file.txt and the keyword lorem.
