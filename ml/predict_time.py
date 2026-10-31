import joblib

# Load trained model
model = joblib.load("ml/study_time_model.pkl")


def predict_study_time(pages, words, topics, difficulty):

    prediction = model.predict([[pages, words, topics, difficulty]])

    return round(prediction[0], 2)