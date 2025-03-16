# 🏥 Heart Disease Prediction using Machine Learning

## 📌 Overview  
This repository contains a machine learning model to predict heart disease based on clinical data. The dataset includes patient symptoms and risk factors.  

## 📊 Dataset  
The dataset is stored in `dataset/heart_disease_extended_large.csv` and contains the following features:  

- **RestingBP** (Blood Pressure)  
- **Cholesterol** (Cholesterol Level)  
- **MaxHR** (Maximum Heart Rate)  
- **Age** (Age of the patient)  
- **Sex** (0 = Female, 1 = Male)  
- **ChestPainType** (0-3, indicating severity)  
- **ShortnessOfBreath**, **PainLocation**, **NumbnessWeakness**, **Dizziness**, **Fainting**, etc.  

## 🚀 How to Use  

### 1️⃣ **Clone the Repository**  
```sh
git clone https://github.com/Venkata-sai-koushik-M/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction
```

### 2️⃣ **Install Dependencies**  
```sh
pip install -r requirements.txt
```

### 3️⃣ **Run Jupyter Notebook**  
```sh
jupyter notebook
```
Open `notebook/heart_disease_prediction.ipynb` and run the cells.  

### 4️⃣ **Train the Model (Optional)**  
```sh
python src/train_model.py
```

### 5️⃣ **Make Predictions**  
```sh
python src/predict.py
```
---
How to Run:

### 1️⃣Ensure you have Python installed and required libraries. Install them using:
```sh
pip install -r requirements.txt
```
### 2️⃣Place the heart_disease_model.pkl and scaler.pkl files in the same directory.

### 3️⃣Run the script in the terminal or command prompt:
```sh
python heart_disease_prediction.py
```
### 4️⃣Enter the required inputs when prompted.

### 5️⃣aThe model will predict whether the person has heart disease or not.

---

## ⚙️ Machine Learning Models Used  
- **Logistic Regression**  
- **Decision Tree**  

### 📈 Model Performance  
The model is evaluated using:  
✅ Accuracy Score  
✅ Confusion Matrix  
✅ Classification Report  

---

## 📌 Contribution  
Feel free to contribute by submitting a pull request.  

## 📜 License  
MIT License  

## Authors
1-[M.Venkata sai koushik][https://github.com/Venkata-sai-koushik-M?tab=repositories]

2-[R.L.Sriyutha][https://github.com/Sriyutha-R-L]
