import joblib
import numpy as np

from config import MODEL_PATH


# Load model only once
model = joblib.load(MODEL_PATH)


def predict_loan(features):

    features = np.array(features).reshape(1, -1)

    prediction = model.predict(features)[0]

    probability = model.predict_proba(features)[0]

    confidence = round(
        max(probability) * 100,
        2
    )

    return prediction, confidence