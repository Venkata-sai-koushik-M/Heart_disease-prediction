import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler

# Load the trained model and scaler
model_filename = "heart_disease_model.pkl"
scaler_filename = "scaler.pkl"

with open(model_filename, "rb") as file:
    model = pickle.load(file)

with open(scaler_filename, "rb") as file:
    scaler = pickle.load(file)

# Function to predict heart disease
def predict_heart_disease(bp, cholesterol, maxhr, age, sex, chest_pain, breath, pain, numbness, dizziness, fainting, flutter, swelling, fatigue):
    input_data = np.array([[bp, cholesterol, maxhr, age, sex, chest_pain, breath, pain, numbness, dizziness, fainting, flutter, swelling, fatigue]])
    input_scaled = scaler.transform(input_data)
    prediction = model.predict(input_scaled)
    return "Heart Disease Detected" if prediction[0] == 1 else "No Heart Disease"

# Run prediction if executed as a script
if __name__ == "__main__":
    bp = float(input("Enter Blood Pressure: "))
    cholesterol = float(input("Enter Cholesterol Level: "))
    maxhr = float(input("Enter Maximum Heart Rate: "))
    age = int(input("Enter Age: "))
    sex = int(input("Enter Sex (0 = Female, 1 = Male): "))
    chest_pain = int(input("Enter Chest Pain Type (0-3): "))
    breath = int(input("Shortness of Breath (0/1): "))
    pain = int(input("Pain Location (0-4): "))
    numbness = int(input("Numbness/Weakness (0/1): "))
    dizziness = int(input("Dizziness (0/1): "))
    fainting = int(input("Fainting (0/1): "))
    flutter = int(input("Fluttering Heart (0/1): "))
    swelling = int(input("Swelling (0/1): "))
    fatigue = int(input("Fatigue (0/1): "))

    result = predict_heart_disease(bp, cholesterol, maxhr, age, sex, chest_pain, breath, pain, numbness, dizziness, fainting, flutter, swelling, fatigue)
    print(result)
