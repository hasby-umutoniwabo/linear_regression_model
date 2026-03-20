import joblib
import numpy as np

# Load model and scaler
model  = joblib.load("best_model.pkl")
scaler = joblib.load("scaler.pkl")

# One sample: [Hours Studied, Previous Scores, Extracurricular, Sleep Hours, Papers Practiced]
sample = np.array([[7, 85, 1, 8, 3]])

# Scale and predict
sample_scaled = scaler.transform(sample)
prediction = model.predict(sample_scaled)[0]

print(f"Predicted Performance Index: {prediction:.2f}")