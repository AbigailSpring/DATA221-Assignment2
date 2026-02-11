import pandas as pd
student_data = pd.read_csv("student.csv")
def determine_grade_band(grade):
    if grade <= 9:
        return "Low"
    elif 10 <= grade <= 14:
        return "Medium"
    else:  # grade >= 15
        return "High"
student_data["grade_band"] = (student_data["grade"].apply(determine_grade_band))
grade_band_summary = student_data.groupby("grade_band").agg(
    num_students_in_band=("grade", "count"),
    avg_absences_in_band=("absences", "mean"),
    pct_with_internet=("internet", lambda x: x.mean() * 100)).reset_index()
grade_band_summary.to_csv("student_bands.csv", index=False)
print(grade_band_summary)
