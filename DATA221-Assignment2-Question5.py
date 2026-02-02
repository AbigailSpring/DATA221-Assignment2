import pandas as pd

students = pd.read_csv("student.csv")
def get_grade_band(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:  # grade >= 15
        return "High"
students["grade_band"] = students["grade"].apply(get_grade_band)
grouped = students.groupby("grade_band").agg(
    num_students=("grade", "count"),
    avg_absences=("absences", "mean"),
    pct_internet=("internet", lambda x: x.mean() * 100)  # percentage
).reset_index()
grouped.to_csv("student_bands.csv", index=False)
print(grouped)