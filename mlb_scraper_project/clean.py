import pandas as pd

# Load original data
original_df = pd.read_csv("mlb_scraper_project/my_mlb_data.csv")

# Validate each column
valid_year = original_df["Year"].notna() & (original_df["Year"].str.lower() != "year")
valid_league = original_df["League"].isin(["AL", "NL"])
valid_avg = original_df["AVG"].str.contains(r"\d", na=False)

# Combine validation rules
is_valid = valid_year & valid_league & valid_avg

# Split valid and removed rows
removed_rows = original_df[~is_valid]
cleaned_rows = original_df[is_valid]

# Save removed rows
removed_rows.to_csv("removed.txt", index=False, sep="\t")

# Clean the valid data
df = cleaned_rows.copy()
df["Year"] = df["Year"].astype(int)
df["AVG"] = df["AVG"].astype(str).str.extract(r"([\d.]+)")[0].astype(float)
df["Player"] = df["Player"].astype(str).str.strip()
df["Team"] = df["Team"].astype(str).str.strip()
df = df[df["AVG"] > 0]

# Save cleaned data
df.to_csv("my_mlb_data_cleaned.csv", index=False)

# Print summary
print("\nRemoved rows:")
print(removed_rows.to_string(index=False))
print("\nSaved: my_mlb_data_cleaned.csv and removed.txt")