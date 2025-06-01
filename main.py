
# IMDB Dataset Analysis using Pandas

import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
df = pd.read_csv("IMDB-Movie-Data.csv")

# Explore Dataset
print("First 5 rows:")
print(df.head())

print("\nDataset Info:")
print(df.info())

print("\nDescriptive Statistics:")
print(df.describe())

# Handle Missing Values
df_cleaned = df.dropna()

# Filter High-Rated Movies
high_rated_movies = df_cleaned[df_cleaned['imdb_score'] > 7.0]
print("\nHigh Rated Movies (>7.0):")
print(high_rated_movies.head())

# Summary Statistics
mean_rating = df_cleaned['imdb_score'].mean()
median_rating = df_cleaned['imdb_score'].median()
std_rating = df_cleaned['imdb_score'].std()

print("\nSummary Statistics:")
print("Mean Rating:", mean_rating)
print("Median Rating:", median_rating)
print("Standard Deviation:", std_rating)

# Top 10 Movies by Rating
top_10 = df_cleaned.nlargest(10, 'imdb_score')
print("\nTop 10 Movies by IMDB Rating:")
print(top_10[['movie_title', 'imdb_score']])

# Histogram of Ratings
plt.figure(figsize=(8,5))
df_cleaned['imdb_score'].plot.hist(bins=20, color='skyblue', edgecolor='black')
plt.title('Distribution of IMDB Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of Movies')
plt.grid(True)
plt.tight_layout()
plt.savefig("assets/histogram.png")
plt.show()

# Bar Chart of Top 10 Movies
plt.figure(figsize=(10,6))
top_10.set_index('movie_title')['imdb_score'].plot.bar(color='orange')
plt.title('Top 10 Highest Rated Movies')
plt.ylabel('IMDB Score')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig("assets/top10.png")
plt.show()
