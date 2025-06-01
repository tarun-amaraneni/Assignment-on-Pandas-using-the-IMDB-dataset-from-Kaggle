# Exploring - Pandas

# 🎬 IMDB Movie Dataset Analysis using Pandas

This project explores the **IMDB 5000 Movie Dataset** using the **Pandas** library. It demonstrates data loading, exploration, cleaning, filtering, statistical analysis, and visualization of movie data.

---

## 📥 Dataset

- Dataset: [IMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/carolzhangdc/imdb-5000-movie-dataset)
- File: `movie_metadata.csv`
- Rename to: `IMDB-Movie-Data.csv`

---

## 🧰 Requirements

Install required libraries:

```bash
pip install pandas matplotlib
```

---

## 🚀 How to Run

1. Download and rename the dataset to `IMDB-Movie-Data.csv`
2. Place it in the same folder as `main.py`
3. Run the Python script:

```bash
python main.py
```

---

## 📊 Code Breakdown and Functionality

### ✅ Step 1: Import Libraries

```python
import pandas as pd
import matplotlib.pyplot as plt
```
These libraries are essential for data handling (`pandas`) and creating visualizations (`matplotlib`).

---

### ✅ Step 2: Load Dataset

```python
df = pd.read_csv("IMDB-Movie-Data.csv")
```
Loads the dataset from CSV format into a Pandas DataFrame for manipulation and analysis.

---

### ✅ Step 3: Explore Dataset

```python
print(df.head())
print(df.info())
print(df.describe())
```
- `.head()`: Shows the first 5 rows of data.
- `.info()`: Gives data types, non-null counts.
- `.describe()`: Provides statistical summary of numeric columns.

---

### ✅ Step 4: Handle Missing Values

```python
df_cleaned = df.dropna()
```
Removes rows with any missing values. This is critical for clean analysis.

---

### ✅ Step 5: Filter High-Rated Movies

```python
high_rated_movies = df_cleaned[df_cleaned['imdb_score'] > 7.0]
```
Filters out only movies with an IMDB rating above 7.0.

---

### ✅ Step 6: Summary Statistics

```python
df_cleaned['imdb_score'].mean()
df_cleaned['imdb_score'].median()
df_cleaned['imdb_score'].std()
```
Calculates:
- Mean (average)
- Median (middle value)
- Standard deviation (spread of ratings)

---

### ✅ Step 7: Top 10 Movies by Rating

```python
top_10 = df_cleaned.nlargest(10, 'imdb_score')
```
Finds the 10 highest-rated movies in the cleaned dataset.

---

### ✅ Step 8: Histogram of Ratings

```python
df_cleaned['imdb_score'].plot.hist()
```
Creates a histogram to visualize the frequency distribution of IMDB ratings.

---

### ✅ Step 9: Bar Chart of Top 10 Movies

```python
top_10.set_index('movie_title')['imdb_score'].plot.bar()
```
Visualizes the top 10 highest-rated movies using a bar chart.

---

## 📂 Project Structure

```
imdb-pandas-analysis/
│
├── IMDB-Movie-Data.csv         # Dataset file (from Kaggle)
├── main.py                     # Python script with analysis
├── README.md                   # This readme file

