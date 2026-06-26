# Smart Lender v1.0

An AI-powered Loan Approval Prediction System built using Machine Learning and Flask.

---

## Overview

Smart Lender is a web application that predicts whether a loan application is likely to be approved or rejected based on applicant financial information, credit score, and asset details.

The system uses a trained Machine Learning model to analyze user input and provide instant loan approval predictions along with a confidence score.

---

## Features

### Machine Learning

* Loan approval prediction using Machine Learning
* Confidence score generation
* Multiple model evaluation and selection
* Trained model persistence using Pickle

### Web Application

* Professional responsive user interface
* Home page
* Loan prediction page
* Result page
* Error handling page
* About page

### User Experience

* Real-time CIBIL score feedback
* Automatic asset calculation
* Indian currency formatting
* Mobile, tablet, and desktop support

---

## Technology Stack

### Frontend

* HTML5
* CSS3
* JavaScript
* Font Awesome

### Backend

* Python
* Flask

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy
* XGBoost
* Imbalanced-Learn

### Development Tools

* Jupyter Notebook
* VS Code
* Git
* GitHub

---

## Project Structure

```text
Smart-Lender/
│
├── dataset/
│   └── loan_approval_dataset.csv
│
├── notebooks/
│   ├── 01_data_understanding.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_data_preprocessing.ipynb
│   └── 04_model_building_and_evaluation.ipynb
│
├── models/
│   ├── best_model.pkl
│   └── scaler.pkl
│
├── flask_app/
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   │
│   ├── templates/
│   │   ├── base.html
│   │   ├── index.html
│   │   ├── predict.html
│   │   ├── result.html
│   │   ├── error.html
│   │   └── about.html
│   │
│   ├── app.py
│   ├── predictor.py
│   ├── config.py
│   └── requirements.txt
│
├── README.md
├── .gitignore
└── .hintrc
---

## Machine Learning Workflow

1. Data Collection
2. Data Understanding
3. Exploratory Data Analysis
4. Data Preprocessing
5. Feature Engineering
6. Model Training
7. Model Evaluation
8. Model Selection
9. Model Deployment

---

## Installation

### Clone the repository

```bash
git clone https://github.com/your-username/Smart-Lender.git
cd Smart-Lender
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / macOS

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000
```

---

## Input Features

The model uses the following features:

* Number of Dependents
* Education Level
* Self Employment Status
* Annual Income
* Loan Amount
* Loan Term
* CIBIL Score
* Residential Asset Value
* Commercial Asset Value
* Luxury Asset Value
* Bank Asset Value

---

## Screenshots

Add screenshots of:

* Home Page
* Prediction Form
* Prediction Result
* About Page
* Error Page

inside a `screenshots/` folder and reference them here.

---

## Functional Features

### Smart Lender

* Loading animation
* Prediction history
* PDF report generation

---

## Disclaimer

Smart Lender provides predictions based on historical data and Machine Learning models. Final loan approval decisions should always be made by authorized financial institutions.

---

## Version Information

| Item         | Value        |
| ------------ | ------------ |
| Project Name | Smart Lender |
| Version      | v1.0         |
| Status       | Released     |
| Release Year | 2026         |

---

## Author

Developed as an academic Machine Learning project using Python, Flask, and Scikit-Learn.
