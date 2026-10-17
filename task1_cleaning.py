
import pandas as pd

# Load the dataset
df = pd.read_csv("Dataset.csv")

# Display basic information
print("Dataset loaded successfully!")
print("\nFirst 5 rows:")
print(df.head())

print("\nDataset shape:")
print(df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate rows:")
print(df.duplicated().sum())

print("\nColumn information:")
df.info()

print("\nUnique values in Type:")
print(df["type"].unique())

print("\nUnique values in Rating:")
print(df["rating"].unique())

print("\nSample Country values:")
print(df["country"].drop_duplicates().head(20).to_list())

print("\nBlank or whitespace-only values:")
for col in df.columns:
    blank_count = df[col].astype(str).str.strip().eq("").sum()
    print(f"{col}: {blank_count}")

print("\nCountry values marked as Not Given:")
print((df["country"].str.strip() == "Not Given").sum())

print("\nCountry values with extra spaces:")
print((df["country"] != df["country"].str.strip()).sum())

print("\nType values with extra spaces:")
print((df["type"] != df["type"].str.strip()).sum())

print("\nRating values with extra spaces:")
print((df["rating"] != df["rating"].str.strip()).sum())

# Create a cleaned copy of the dataset
cleaned_df = df.copy()

# Standardize text columns
text_columns = ["type", "title", "director", "country",
                "rating", "duration", "listed_in"]

for col in text_columns:
    cleaned_df[col] = cleaned_df[col].str.strip()

# Standardize content type capitalization
cleaned_df["type"] = cleaned_df["type"].replace({
    "movie": "Movie",
    "tv show": "TV Show"
})

# Check the cleaning results
print("\nType values after standardization:")
print(cleaned_df["type"].value_counts())

print("\nCountry values marked as Not Given:")
print((cleaned_df["country"] == "Not Given").sum())

print("\nDataset shape after cleaning:")
print(cleaned_df.shape)
# Remove duplicate records if any exist
cleaned_df = cleaned_df.drop_duplicates()

# Check for missing values after cleaning
print("\nMissing values after cleaning:")
print(cleaned_df.isnull().sum())

# Save the cleaned dataset
cleaned_df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaned dataset exported successfully!")
print("Final dataset shape:", cleaned_df.shape)
print("Output file: netflix_cleaned.csv")