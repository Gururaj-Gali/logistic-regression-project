import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle

# Sample dataset
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "attendance": [40, 50, 55, 65, 70, 75, 85, 90],
    "result": [0, 0, 0, 0, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance"]]
y = df["result"]

# Train model
model = LogisticRegression()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)

print("Model trained and saved as model.pkl")
