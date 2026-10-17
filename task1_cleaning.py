
import pandas as pd

# 1. Load the original dataset
df = pd.read_csv("Dataset.csv")

print("NETFLIX DATA CLEANING AND PREPARATION")
print("=" * 40)

# 2. Inspect the dataset
print("\nOriginal dataset shape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())

print("\nColumn information:")
df.info()

# 3. Check data quality before cleaning
print("\nMissing values before cleaning:")
print(df.isnull().sum())

print("\nDuplicate rows before cleaning:", df.duplicated().sum())

# Check blank or whitespace-only values
print("\nBlank or whitespace-only values:")
for col in df.columns:
    blank_count = (
        df[col].astype("string").str.strip().eq("").sum()
    )
    print(f"{col}: {blank_count}")

# 4. Create a separate copy for cleaning
cleaned_df = df.copy()

# 5. Standardize whitespace in text columns
text_columns = [
    "type", "title", "director", "country",
    "date_added", "rating", "duration", "listed_in"
]

for col in text_columns:
    cleaned_df[col] = cleaned_df[col].str.strip()

# Standardize content type capitalization
cleaned_df["type"] = (
    cleaned_df["type"]
    .str.lower()
    .replace({
        "movie": "Movie",
        "tv show": "TV Show"
    })
)

# Preserve "Not Given" country values because they
# represent unavailable information in this dataset.

# 6. Remove duplicate records
cleaned_df = cleaned_df.drop_duplicates()

# 7. Validate the cleaned dataset
print("\nMissing values after cleaning:")
print(cleaned_df.isnull().sum())

print("\nDuplicate rows after cleaning:",
      cleaned_df.duplicated().sum())

print("\nContent type counts:")
print(cleaned_df["type"].value_counts())

print("\nCountry values marked as Not Given:",
      cleaned_df["country"].eq("Not Given").sum())

print("\nFinal dataset shape:", cleaned_df.shape)

# 8. Export the cleaned dataset
cleaned_df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaned dataset exported successfully!")
print("Output file: netflix_cleaned.csv")
