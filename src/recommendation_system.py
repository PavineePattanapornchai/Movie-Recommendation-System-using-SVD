import pandas as pd
from surprise import Dataset, Reader, SVD
from sklearn.metrics import mean_squared_error
import joblib

def train_model(ratings_train):
    reader = Reader(rating_scale=(0.5, 5.0))
    data = Dataset.load_from_df(ratings_train[['userId', 'movieId', 'rating']], reader)
    trainset = data.build_full_trainset()

    algo = SVD()
    algo.fit(trainset)
    return algo

def predict_rating(model, input_df):
    predictions = []
    for _, row in input_df.iterrows():
        pred = model.predict(row['userId'], row['movieId']).est
        predictions.append(pred)
    input_df['rating'] = predictions
    return input_df

def evaluate_model(actual_df, predicted_ratings):
    actual_ratings = actual_df['rating'].values
    predicted_ratings = predicted_ratings['rating'].values
    rmse = mean_squared_error(actual_ratings, predicted_ratings, squared=False)
    print(f'Validation RMSE: {rmse:.4f}')
    return rmse

def main():
    ratings_train = pd.read_csv('data/ratings_train.csv')
    ratings_valid = pd.read_csv('data/ratings_valid.csv')
    
    print("Training model...")
    model = train_model(ratings_train)

    joblib.dump(model, 'svd_model.pkl')
    print("Model saved as svd_model.pkl")

    print("Predicting ratings for validation set...")
    predictions_valid = predict_rating(model, ratings_valid.copy())
    
    evaluate_model(ratings_valid, predictions_valid)

if __name__ == "__main__":
    main()