import pandas as pd

crime_data = pd.read_csv("crime.csv")
crime_data["crime_risk"] = crime_data["ViolentCrimesPerPop"].apply(
    lambda crime_rate: "HighCrime" if crime_rate >= 0.50 else "LowCrime")
avg_unemployment_by_risk = crime_data.groupby("crime_risk")["PctUnemployed"].mean()
for risk_category in ["HighCrime", "LowCrime"]:
    avg_unemployment = avg_unemployment_by_risk[risk_category]
    print(f"Average unemployment rate for {risk_category}: {avg_unemployment:.2f}%")