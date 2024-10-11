# Movie Recommendation System using SVD

## Overview
This project implements a movie recommendation system using the Surprise library, specifically utilizing the SVD (Singular Value Decomposition) algorithm. SVD helps decompose the user-item rating matrix to uncover underlying patterns in the data, allowing for accurate prediction of movie ratings and improved personalization.

## Key Features
- **SVD Algorithm**: Uses matrix factorization to predict user ratings based on historical data.
- **Surprise Library**: The project leverages the Surprise library, a Python tool for building recommendation systems.
- **RMSE Calculation**: The model's performance is evaluated using Root Mean Square Error (RMSE) to measure the accuracy of predicted ratings.

## Data
The dataset consists of user ratings for movies, and the project uses two datasets:
1. **Training Set (ratings_train.csv)**: Used to train the recommendation model.
2. **Validation Set (ratings_valid.csv)**: Used to evaluate the model's performance.

## How It Works
1. **Data Loading**: The data is loaded using Pandas and preprocessed by removing unnecessary columns.
2. **Model Training**: The SVD algorithm is trained on the user-item-rating data.
3. **Prediction**: After training, the model predicts movie ratings for the validation dataset.
4. **Evaluation**: The Root Mean Square Error (RMSE) is calculated to compare the predicted ratings with the actual ratings.
