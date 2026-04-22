import pandas as pd

# 1. Create DataFrame
data = {
    "Name": ["Pankaj", "Rahul", "Amit"],
    "Age": [21, 22, 23],
    "Marks": [85, 90, 78]
}
df = pd.DataFrame(data)
print("DataFrame:\n", df)

# 2. Read / Write (example)
# df = pd.read_csv("file.csv")
# df.to_csv("output.csv", index=False)

# 3. Basic Info
print("\nInfo:")
print(df.info())
print("\nDescribe:\n", df.describe())

# 4. Selection
print("\nSelect Column:\n", df["Name"])
print("\nSelect Row:\n", df.iloc[0])

# 5. Filtering
print("\nAge > 21:\n", df[df["Age"] > 21])

# 6. Add / Update Column
df["Grade"] = ["A", "A+", "B"]
df["Age"] = df["Age"] + 1

# 7. Missing Values
df.loc[1, "Marks"] = None
print("\nMissing:\n", df.isnull())
df["Marks"].fillna(df["Marks"].mean(), inplace=True)

# 8. Sorting
print("\nSorted by Marks:\n", df.sort_values(by="Marks"))

# 9. GroupBy
print("\nGroupBy Grade:\n", df.groupby("Grade")["Marks"].mean())

# 10. Drop Column
df.drop("Grade", axis=1, inplace=True)

print("\nFinal Data:\n", df)
