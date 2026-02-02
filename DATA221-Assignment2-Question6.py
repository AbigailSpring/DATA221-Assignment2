import pandas as pd

crime = pd.read_csv("crime.csv")
crime["risk"] = crime["ViolentCrimesPerPop"].apply(
    lambda x: "HighCrime" if x >= 0.50 else "LowCrime")
grouped = crime.groupby("risk")["PctUnemployed"].mean()
for risk_level in ["HighCrime", "LowCrime"]:
    avg_unemp = grouped[risk_level]
    print(f"Average unemployment rate for {risk_level}: {avg_unemp:.2f}%")