import pandas as pd

df = pd.read_csv("data/patients_dakar.csv")

print("Nombre de patients :", len(df))
print("Colonnes :", df.columns)

print("\n--- 5 premiers ---")
print(df.head())

print("\n--- Statistiques ---")
print(df.describe())

print("\n--- Diagnostics ---")
print(df["diagnostic"].value_counts())


print("\n--- Patients par sexe et diagnostic ---")

group = df.groupby(["sexe", "diagnostic"]).size()

print(group)