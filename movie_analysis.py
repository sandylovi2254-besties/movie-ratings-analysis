import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# ==========================================
# STEP 1: LOAD DATA
# ==========================================

movies = pd.read_csv("movies.csv")
ratings = pd.read_csv("ratings.csv")

print("MOVIE RATINGS DATA ANALYSIS")
print("-" * 40)
print("Total movies:", len(movies))
print("Total ratings:", len(ratings))

print("\nFirst five movies:")
print(movies.head())

print("\nFirst five ratings:")
print(ratings.head())

# ==========================================
# STEP 2: HIGHEST-RATED MOVIES
# ==========================================

average_ratings = ratings.groupby("movieId")["rating"].mean()
rating_counts = ratings.groupby("movieId")["rating"].count()

movie_stats = (
    average_ratings.rename("average_rating")
    .to_frame()
    .join(rating_counts.rename("rating_count"))
    .reset_index()
    .merge(movies[["movieId", "title"]], on="movieId", how="left")
)

top_10 = (
    movie_stats[movie_stats["rating_count"] >= 100]
    .sort_values("average_rating", ascending=False)
    .head(10)
)

print("\nTop 10 Highest-Rated Movies (minimum 100 ratings):")
print(top_10[["title", "average_rating", "rating_count"]])

plt.figure(figsize=(10, 6))
sns.barplot(data=top_10, x="average_rating", y="title",
            color="#6C5CE7")
plt.title("Top 10 Highest-Rated Movies")
plt.xlabel("Average Rating")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()

# ==========================================
# STEP 3: MOST POPULAR MOVIES
# ==========================================

popular_movies = (
    movie_stats[movie_stats["rating_count"] >= 100]
    .sort_values("rating_count", ascending=False)
    .head(10)
)

print("\nTop 10 Most Popular Movies:")
print(popular_movies[["title", "rating_count"]])

plt.figure(figsize=(10, 6))
sns.barplot(data=popular_movies, x="rating_count", y="title",
            color="#00B894")
plt.title("Top 10 Most Popular Movies")
plt.xlabel("Number of Ratings")
plt.ylabel("Movie Title")
plt.tight_layout()
plt.show()

# ==========================================
# STEP 4: DISTRIBUTION OF RATINGS
# ==========================================

print("\nRating Statistics:")
print(ratings["rating"].describe())

plt.figure(figsize=(10, 6))
sns.histplot(data=ratings, x="rating", bins=10,
             kde=True, color="#E17055")
plt.title("Distribution of Movie Ratings")
plt.xlabel("Movie Rating")
plt.ylabel("Number of Ratings")
plt.tight_layout()
plt.show()

# ==========================================
# STEP 5: POPULARITY VS AVERAGE RATING
# ==========================================

plt.figure(figsize=(10, 6))
sns.scatterplot(
    data=movie_stats,
    x="rating_count",
    y="average_rating",
    color="red",
    alpha=0.6,
    s=40
)
plt.title("Movie Popularity vs Average Rating")
plt.xlabel("Number of Ratings (Popularity)")
plt.ylabel("Average Rating")
plt.tight_layout()
plt.show()

# Correlation calculation
correlation = movie_stats["rating_count"].corr(
    movie_stats["average_rating"]
)

print("\nCorrelation between Popularity and Average Rating:",
      round(correlation, 3))

if correlation > 0:
    print("The relationship is positive.")
elif correlation < 0:
    print("The relationship is negative.")
else:
    print("There is no linear correlation.")

# Correlation heatmap
plt.figure(figsize=(7, 5))
sns.heatmap(
    movie_stats[["rating_count", "average_rating"]].corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    vmin=-1,
    vmax=1
)
plt.title("Correlation: Popularity vs Average Rating")
plt.tight_layout()
plt.show()

# ==========================================
# STEP 6: GENRE ANALYSIS
# ==========================================

genre_data = movie_stats[["movieId", "average_rating"]].merge(
    movies[["movieId", "genres"]],
    on="movieId",
    how="left"
)

genre_data["genres"] = genre_data["genres"].str.split(
    "|", regex=False
)
genre_data = genre_data.explode("genres")

genre_stats = genre_data.groupby("genres").agg(
    average_rating=("average_rating", "mean"),
    movie_count=("movieId", "nunique")
)

top_genres_all = genre_stats.sort_values(
    "average_rating", ascending=False
).head(10)

plt.figure(figsize=(10, 6))
sns.barplot(
    x=top_genres_all["average_rating"],
    y=top_genres_all.index,
    color="steelblue",
    order=top_genres_all.index
)
plt.title("Top 10 Genres by Average Movie Rating")
plt.xlabel("Average Rating")
plt.ylabel("Genre")
plt.tight_layout()
plt.show()

# ==========================================
# STEP 7: IMPROVED GENRE ANALYSIS
# Minimum 50 movies per genre
# ==========================================

popular_genres = genre_stats[
    genre_stats["movie_count"] >= 50
].sort_values("average_rating", ascending=False)

top_genres = popular_genres.head(10)

print("\nTop Genres (minimum 50 movies):")
print(top_genres)

if not top_genres.empty:
    plt.figure(figsize=(10, 6))

    sns.barplot(
        data=top_genres.reset_index(),
        x="average_rating",
        y="genres",
        color="steelblue",
        order=top_genres.index.tolist()
    )

    plt.title(
        "Top Movie Genres by Average Rating "
        "(Minimum 50 Movies)"
    )
    plt.xlabel("Average Rating")
    plt.ylabel("Genre")
    plt.tight_layout()
    plt.show()
else:
    print("No genres meet the minimum 50-movie threshold.")

# ==========================================
# STEP 8: FINAL INSIGHTS VISUALIZATION
# ==========================================

best_movie = movie_stats.loc[
    movie_stats["average_rating"].idxmax()
]

overall_average = ratings["rating"].mean()

if not popular_genres.empty:
    highest_genre_average = popular_genres[
        "average_rating"
    ].max()
else:
    highest_genre_average = np.nan

insight_labels = [
    "Overall Average Rating",
    "Highest Movie Average",
    "Highest Genre Average"
]

insight_values = [
    overall_average,
    best_movie["average_rating"],
    highest_genre_average
]

colors = ["#8E44AD", "#00B894", "#F1C40F"]

print("\nFINAL PROJECT INSIGHTS")
print("-" * 40)
print("Overall average rating:", round(overall_average, 2))
print("Highest-rated movie:", best_movie["title"])
print("Its average rating:", round(best_movie["average_rating"], 2))

if not np.isnan(highest_genre_average):
    print("Highest-rated qualifying genre average:",
          round(highest_genre_average, 2))
else:
    print("No qualifying genre available.")

print("Popularity-rating correlation:", round(correlation, 3))

# Plot only metrics with valid values
valid_insights = [
    (label, value, color)
    for label, value, color in zip(
        insight_labels, insight_values, colors
    )
    if pd.notna(value)
]

labels = [item[0] for item in valid_insights]
values = [item[1] for item in valid_insights]
bar_colors = [item[2] for item in valid_insights]

fig, ax = plt.subplots(figsize=(10, 5))

bars = ax.barh(
    labels,
    values,
    color=bar_colors,
    edgecolor="black",
    height=0.6
)

for bar in bars:
    value = bar.get_width()
    ax.text(
        value + 0.03,
        bar.get_y() + bar.get_height() / 2,
        f"{value:.2f}",
        va="center",
        fontsize=11,
        fontweight="bold"
    )

ax.set_title(
    "Movie Ratings Analysis - Key Insights",
    fontsize=15,
    fontweight="bold"
)
ax.set_xlabel("Average Rating (out of 5)")
ax.set_xlim(0, 5.5)
ax.grid(axis="x", linestyle="--", alpha=0.3)
ax.set_axisbelow(True)

plt.tight_layout()
plt.show()

print("\nANALYSIS COMPLETE")