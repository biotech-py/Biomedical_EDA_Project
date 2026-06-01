![Python](https://img.shields.io/badge/Python-3.11-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-orange)
![PowerBI](https://img.shields.io/badge/PowerBI-Dashboard-yellow)

# Biomedical EDA: Diabetes Analysis

## Project Objective

This project performs Exploratory Data Analysis (EDA) on the Pima Indians Diabetes Dataset to identify patterns, risk factors, and relationships associated with diabetes.

## Dataset Information

* Dataset: Pima Indians Diabetes Dataset
* Records: 768 patients
* Features: 8 clinical variables and 1 target variable
* Target Variable: Diabetes Outcome (0 = Non-Diabetic, 1 = Diabetic)

## Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

## Key Findings

* Glucose exhibited the strongest correlation with diabetes outcome.
* Diabetic patients had significantly higher average glucose levels.
* Higher BMI was associated with increased diabetes prevalence.
* Older individuals were more likely to be diabetic.
* The Insulin variable contained a large number of missing values represented as zeros.

## Sample Visualizations

### Glucose Distribution

![Glucose Distribution](OUTPUTS/glucose_distribution.png)

### BMI Distribution

![BMI Distribution](OUTPUTS/bmi_distribution.png)

### Outcome Distribution

![Outcome Distribution](OUTPUTS/outcome_distribution.png)

### Correlation Matrix

![Correlation Matrix](OUTPUTS/correlation_matrix.png)

## Repository Structure

```text
Biomedical_EDA_Project/
│
├── DATA/
├── NOTEBOOKS/
│   ├── Diabetes_EDA.ipynb
│   └── Diabetes_EDA.py
├── OUTPUTS/
├── REPORTS/
└── README.md
```

## Future Improvements

* Develop a machine learning model for diabetes prediction.
* Build an interactive Power BI dashboard.
* Perform statistical hypothesis testing.
* Conduct feature engineering and model evaluation.

## Author

Nirupam Joarder

Biotechnology | Data Analytics | Python
