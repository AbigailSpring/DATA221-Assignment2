import pandas as pd
student_data = pd.read_csv("student.csv")
high_engagement_students = student_data[
    (student_data["studytime"] >= 3) &
    (student_data["internet"] == 1) &
    (student_data["absences"] <= 5)]
high_engagement_students.to_csv("high_engagement.csv", index=False)
num_high_engagement_students = len(high_engagement_students)
average_high_engagement_grade = high_engagement_students["grade"].mean()
print(f"Number of high-engagement students saved: {num_high_engagement_students}")
print(f"Average grade of high-engagement students: {average_high_engagement_grade:.2f}")

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