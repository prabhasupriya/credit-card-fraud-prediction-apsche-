# Credit Card Fraud Detection using Machine Learning

## Project Overview

The Credit Card Fraud Detection project predicts whether a credit card transaction is **Genuine** or **Fraudulent** using Machine Learning algorithms. The application provides a simple web interface where users can enter transaction details and receive a prediction.

This project follows the complete Machine Learning workflow, including data preprocessing, exploratory data analysis, model training, evaluation, and deployment using Flask.

---

# Objectives

- Detect fraudulent credit card transactions.
- Compare multiple Machine Learning models.
- Select the best-performing model.
- Deploy the trained model using Flask.
- Build a simple and user-friendly web interface.

---

# Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Flask
- Joblib
- HTML
- CSS

---

# Dataset

Dataset: Credit Card Fraud Detection Dataset

Features:

- Time
- V1 to V28 (PCA-transformed features)
- Amount

Target:

- Class
  - 0 → Genuine Transaction
  - 1 → Fraudulent Transaction

---

# Machine Learning Workflow

## 1. Data Collection

- Downloaded the Credit Card Fraud Detection dataset.
- Loaded the dataset into Pandas.

---

## 2. Data Analysis

Performed:

- Dataset exploration
- Data visualization
- Univariate analysis
- Multivariate analysis
- Statistical analysis

---

## 3. Data Preprocessing

Performed:

- Duplicate removal
- Missing value checking
- Feature selection
- Feature scaling
- Train-Test split

---

## 4. Models Used

The following Machine Learning algorithms were trained and evaluated:

- Logistic Regression
- Decision Tree
- Random Forest

---

# Model Comparison

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|-------|----------|-----------|--------|----------|----------|
| Logistic Regression | 99.896% | 70.00% | 66.31% | 68.11% | 83.13% |
| Decision Tree | 99.898% | 69.07% | 70.53% | 69.79% | 85.24% |
| Random Forest | **99.951%** | **97.18%** | **72.63%** | **83.13%** | **86.31%** |

Random Forest achieved the best performance and was selected for deployment.

---

# Project Structure

```
Project Development Phase
│
├── app.py
├── requirements.txt
├── README.md
│
├── dataset
│      creditcard.csv
│
├── notebook
│      Credit_Card_Fraud_Detection.ipynb
│
├── saved_models
│      best_model.pkl
│      time_scaler.pkl
│      amount_scaler.pkl
│
├── templates
│      index.html
│      resultvalue.html
│
└── static
       style.css
```

---

# Installation

Clone the repository:

```bash
git clone https://github.com/prabhasupriya/credit-card-fraud-prediction-apsche-.git
```

Move to the project directory:

```bash
cd Project Development Phase
```

Install the required packages:

```bash
pip install -r requirements.txt
```

---

# Running the Application

Run the Flask application:

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

# Application Workflow

1. Open the web application.
2. Enter transaction details.
3. Click the **Predict** button.
4. The trained Random Forest model predicts whether the transaction is Genuine or Fraudulent.
5. The prediction result is displayed on the result page.

---

# Future Enhancements

- Deep Learning-based fraud detection.
- Real-time transaction monitoring.
- Cloud deployment.
- User authentication.
- Interactive dashboard.
- API integration.

---

# Conclusion

This project successfully demonstrates the use of Machine Learning for detecting fraudulent credit card transactions. Among the evaluated models, the Random Forest classifier achieved the highest performance and was deployed using Flask to provide real-time predictions through a web interface.

---

## Developed By

**Bandaru Prabha Supriya**

B.Tech - Artificial Intelligence and Machine Learning
