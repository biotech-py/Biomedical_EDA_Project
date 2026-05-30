# Diabetes Exploratory Data Analysis (EDA)

## Project Overview

This project explores the Pima Indians Diabetes Dataset to identify patterns and factors associated with diabetes.

The objective was to perform a complete Exploratory Data Analysis (EDA) workflow including:

* Data inspection
* Data quality assessment
* Distribution analysis
* Outlier detection
* Outcome analysis
* Comparative analysis
* Correlation analysis

The project was developed using Python, Pandas, NumPy, and Matplotlib.

---

## Dataset Summary

| Metric                | Value   |
| --------------------- | ------- |
| Records               | 768     |
| Features              | 9       |
| Target Variable       | Outcome |
| Diabetic Patients     | 34.9%   |
| Non-Diabetic Patients | 65.1%   |

### Variables

* Pregnancies
* Glucose
* BloodPressure
* SkinThickness
* Insulin
* BMI
* DiabetesPedigreeFunction
* Age
* Outcome

---

# Data Quality Assessment

Although the dataset contains no null values, several medical variables contain physiologically impossible zero values.

### Zero Value Counts

| Variable      | Zero Values |
| ------------- | ----------- |
| Glucose       | 5           |
| BloodPressure | 35          |
| SkinThickness | 227         |
| Insulin       | 374         |
| BMI           | 11          |

### Key Observation

The Insulin variable contains the highest number of zero values, indicating substantial missing or unrecorded measurements.

These values should ideally be handled during future data preprocessing before predictive modeling.

---

# Distribution Analysis

## Glucose

* Most patients have glucose levels between 80 and 140.
* Distribution is approximately normal with a slight right skew.
* Few observations contain zero values, likely representing missing measurements.

## BMI

* Majority of patients have BMI values between 25 and 40.
* Distribution shows a moderate right skew.
* Several individuals exhibit high BMI values.

## Insulin

* Highly right-skewed distribution.
* Large concentration of values near zero.
* Presence of extreme high-value observations.

## Age

* Majority of patients fall between 20 and 35 years of age.
* Frequency decreases with increasing age.
* Distribution is strongly right-skewed.

---

# Outlier Analysis

## Glucose

A small number of extremely low glucose values were identified and likely represent recording errors or missing measurements.

## BMI

Several high BMI observations (>50) were observed and appear to represent genuine extreme cases rather than errors.

## Insulin

The insulin variable contains numerous extreme outliers extending beyond 800.

This variable also contains a large number of zero values, making it one of the most challenging variables in the dataset.

## Age

A few older patients appear as outliers, but these values remain realistic and do not indicate data quality issues.

---

# Outcome Analysis

## Class Distribution

| Outcome          | Percentage |
| ---------------- | ---------- |
| Non-Diabetic (0) | 65.1%      |
| Diabetic (1)     | 34.9%      |

### Observation

The dataset is moderately imbalanced, with non-diabetic patients representing roughly two-thirds of the population.

Both classes remain sufficiently represented for comparative analysis.

---

# Comparative Analysis

Average values were compared between diabetic and non-diabetic patients.

| Variable | Non-Diabetic | Diabetic |
| -------- | ------------ | -------- |
| Glucose  | 109.98       | 141.26   |
| BMI      | 30.30        | 35.14    |
| Insulin  | 68.79        | 100.34   |
| Age      | 31.19        | 37.07    |

## Findings

### Glucose

Diabetic patients exhibit significantly higher average glucose levels.

### BMI

Diabetic patients show higher average BMI values.

### Insulin

Average insulin levels are higher among diabetic patients, although this variable contains substantial missing and extreme values.

### Age

Diabetic patients tend to be older than non-diabetic patients.

---

# Correlation Analysis

The correlation matrix was used to evaluate relationships between variables.

### Strongest Correlations with Diabetes Outcome

| Variable    | Correlation |
| ----------- | ----------- |
| Glucose     | 0.467       |
| BMI         | 0.293       |
| Age         | 0.238       |
| Pregnancies | 0.222       |

### Insights

* Glucose has the strongest relationship with diabetes.
* BMI demonstrates a moderate positive association.
* Age and number of pregnancies also show meaningful positive relationships.
* Blood pressure and skin thickness show relatively weak relationships with diabetes.

---

# Key Insights

1. Glucose is the strongest indicator associated with diabetes.
2. Higher BMI is linked with increased diabetes prevalence.
3. Older individuals are more likely to be diabetic.
4. Insulin levels tend to be higher among diabetic patients.
5. The dataset contains several variables with significant missing-value issues represented as zeros.

---

# Conclusion

This exploratory data analysis identified several important factors associated with diabetes.

The analysis demonstrates that diabetic patients generally exhibit:

* Higher glucose levels
* Higher BMI values
* Higher insulin levels
* Greater average age

Among all variables examined, glucose emerged as the most influential factor associated with diabetes.

The findings align with established medical understanding of diabetes risk factors and provide a strong foundation for future predictive modeling projects.

---

# Tools Used

* Python
* Pandas
* NumPy
* Matplotlib
* Jupyter Notebook

---

# Author

**Nirupam Joarder**

Biotechnology Student | Aspiring Data Analyst

GitHub Portfolio Project – Biomedical Data Analytics
