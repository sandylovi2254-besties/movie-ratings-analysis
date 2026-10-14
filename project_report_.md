Movie Ratings Analysis Project Report

1. Problem Statement

Movies receive different ratings from viewers based on their preferences and experiences. Identifying highly rated movies, popular movies, and trends in movie ratings can help us better understand viewer preferences.

The objective of this project is to analyze movie ratings data using Python to identify highly rated movies, find the most popular movies, study the distribution of ratings, examine the relationship between movie popularity and average ratings, and compare ratings across different movie genres.

This project uses Pandas and NumPy for data analysis and Matplotlib and Seaborn for data visualization. The aim is to extract meaningful insights from the dataset and present the results using statistical summaries and graphical representations. 

2. Dataset Description

This project uses two CSV datasets: "movies.csv" and "ratings.csv".

2.1 Movies Dataset

The "movies.csv" file contains information about movies.

- "movieId": A unique identifier assigned to each movie.
- "title": The title of the movie.
- "genres": The genres associated with the movie.

2.2 Ratings Dataset

The "ratings.csv" file contains user ratings for movies.

- "userId": The identifier of the user who rated a movie.
- "movieId": The identifier of the movie being rated.
- "rating": The rating given by the user.
- "timestamp": The time when the rating was recorded.

2.3 Purpose of the Datasets

The movies dataset provides movie titles and genres, while the ratings dataset provides user ratings. The two datasets are connected using "movieId", allowing the analysis to calculate average ratings, count ratings, compare genres, and identify popular movies.

2. Dataset Description

This project uses two CSV datasets: "movies.csv" and "ratings.csv".

2.1 Movies Dataset

The "movies.csv" file contains information about movies.

- "movieId": A unique identifier assigned to each movie.
- "title": The title of the movie.
- "genres": The genres associated with the movie.

2.2 Ratings Dataset

The "ratings.csv" file contains user ratings for movies.

- "userId": The identifier of the user who rated a movie.
- "movieId": The identifier of the movie being rated.
- "rating": The rating given by the user.
- "timestamp": The time when the rating was recorded.

2.3 Purpose of the Datasets

The movies dataset provides movie titles and genres, while the ratings dataset provides user ratings. The two datasets are connected using "movieId", allowing the analysis to calculate average ratings, count ratings, compare genres, and identify popular movies.

4. Data Analysis Using Pandas and NumPy

The Pandas and NumPy libraries are used to analyze the movie ratings dataset and extract meaningful information.

The following analyses are performed in this project:

4.1 Average Movie Ratings

The average rating of each movie is calculated by grouping the ratings dataset using "movieId" and finding the mean of the ratings.

4.2 Rating Counts and Movie Popularity

The total number of ratings received by each movie is calculated. Movies with at least 100 ratings are considered when identifying the most popular movies.

4.3 Highest-Rated Movies

Movies with at least 100 ratings are sorted according to their average ratings to identify the top 10 highest-rated movies.

4.4 Rating Statistics

Descriptive statistics are generated to understand the distribution of ratings, including the mean, standard deviation, minimum, maximum, and quartiles.

4.5 Correlation Analysis

The correlation between the number of ratings and the average movie rating is calculated to examine whether a relationship exists between movie popularity and average ratings.

4.6 Genre Analysis

Movies are grouped according to their genres to calculate average genre ratings and movie counts. Genres containing at least 50 movies are considered in the improved genre comparison.

These analyses provide a foundation for understanding movie ratings, popularity, and genre-level trends.

4. Data Analysis Using Pandas and NumPy

The Pandas and NumPy libraries are used to analyze the movie ratings dataset and extract meaningful information.

The following analyses are performed in this project:

4.1 Average Movie Ratings

The average rating of each movie is calculated by grouping the ratings dataset using "movieId" and finding the mean of the ratings.

4.2 Rating Counts and Movie Popularity

The total number of ratings received by each movie is calculated. Movies with at least 100 ratings are considered when identifying the most popular movies.

4.3 Highest-Rated Movies

Movies with at least 100 ratings are sorted according to their average ratings to identify the top 10 highest-rated movies.

4.4 Rating Statistics

Descriptive statistics are generated to understand the distribution of ratings, including the mean, standard deviation, minimum, maximum, and quartiles.

4.5 Correlation Analysis

The correlation between the number of ratings and the average movie rating is calculated to examine whether a relationship exists between movie popularity and average ratings.

4.6 Genre Analysis

Movies are grouped according to their genres to calculate average genre ratings and movie counts. Genres containing at least 50 movies are considered in the improved genre comparison.

These analyses provide a foundation for understanding movie ratings, popularity, and genre-level trends.

6. Key Findings

The analysis of the movie ratings dataset produced the following key findings:

1. Overall Average Rating: The overall average rating across the dataset was 3.5 out of 5, indicating the general rating level given by users.

2. Highest-Rated Movie: Lamerica (1994) achieved an average rating of 5.0 in the final project results.

3. Genre Analysis: The highest average rating among genres containing at least 50 movies was 3.78.

4. Popularity and Ratings Relationship: The correlation between the number of ratings and average movie ratings was 0.127, indicating a weak positive linear relationship.

5. Movie Popularity: The analysis identified the ten most popular movies based on the number of ratings received, considering movies with at least 100 ratings.

6. Rating Distribution: The rating statistics and histogram provided an overview of how users distributed their ratings across the dataset.

7. Genre Comparison: The genre visualizations enabled comparisons of average ratings across different movie genres, with the improved comparison considering genres containing at least 50 movies.

Overall, the findings demonstrate how Python-based data analysis and visualization can help identify patterns in movie ratings, popularity, and genre preferences.