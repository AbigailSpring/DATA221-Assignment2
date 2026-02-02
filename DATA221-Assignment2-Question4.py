import pandas as pd

students = pd.read_csv("student.csv")
filtered_students = students[
    (students["studytime"] >= 3) &
    (students["internet"] == 1) &
    (students["absences"] <= 5)]
filtered_students.to_csv("high_engagement.csv", index=False)
num_students = len(filtered_students)
average_grade = filtered_students["grade"].mean()
print(f"Number of students saved: {num_students}")
print(f"Average grade: {average_grade:.2f}")