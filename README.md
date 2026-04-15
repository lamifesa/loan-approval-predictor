# 🏦 Loan Eligibility Predictor

A machine learning web application that predicts whether a loan applicant 
is likely to be approved, based on financial and personal profile data.

Built as a hands-on learning project to develop practical ML engineering 
skills. Development included guidance and code review from AI tools (Claude).

## 🔗 Live Demo
https://loan-approval-predictor-b87qkkkevn4evru4tbymsz.streamlit.app/

## 📌 Project Overview
Users enter their financial details into a web form and receive an instant 
prediction on their loan eligibility. The app demonstrates a full ML 
pipeline from raw data to deployed web application.

## 🛠️ Tech Stack
- **Python** — core language
- **Pandas** — data preprocessing
- **Scikit-learn** — model training (Random Forest Classifier)
- **Streamlit** — web interface and deployment
- **Joblib** — model serialisation

## 📊 Dataset
[Loan Prediction Dataset 2025](https://www.kaggle.com/datasets/nabihazahid/loan-prediction-dataset-2025)
— 20,000 records with financial and demographic features.

## ⚙️ How It Works
1. Data is preprocessed and categorical features are label-encoded
2. A Random Forest Classifier is trained and tuned using RandomizedSearchCV
3. The best model is saved and loaded into a Streamlit web app
4. Users input their details and receive a prediction in real time

## 📈 Model Performance
- **Accuracy:** 90.2%
- **Precision:** 89.5%
- **Recall:** 99.3%

## 🚀 Run Locally
```bash
git clone https://github.com/lamifesa/loan-approval-predictor
cd loan-approval-predictor
pip install -r requirements.txt
streamlit run app.py
```

## 📁 Project Structure
```
├── data_process.ipynb     # Data exploration, preprocessing and model training
├── app.py                 # Streamlit web application
├── randomforestclassifier.pkl  # Saved trained model
└── README.md
```
