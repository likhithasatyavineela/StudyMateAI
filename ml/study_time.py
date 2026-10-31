import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib

# Load dataset
df = pd.read_csv("data/study_time_dataset.csv")

# Features (Input)
X = df[["pages", "words", "topics", "difficulty"]]

# Target (Output)
y = df["study_time_hours"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "ml/study_time_model.pkl")

print("✅ Model trained successfully!")
print("✅ Model saved as study_time_model.pkl")