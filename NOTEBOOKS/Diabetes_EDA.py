# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %%
df = pd.read_csv("../DATA/diabetes.csv")

# %%
df.head()

# %%
df.shape

# %%
df.info()

# %%
df.describe()

# %%
(df == 0).sum()

# %% [markdown]
# ### Data Quality Observation
# 
# Although no null values are present, several medical variables contain impossible zero values.
# 
# These zeros likely represent missing or unrecorded measurements.
# 
# The Insulin column contains 374 zero values, suggesting substantial missing data.

# %%
plt.figure(figsize=(6,4))

plt.hist(df["Glucose"])

plt.title("Glucose Distribution")
plt.xlabel("Glucose")
plt.ylabel("Frequency")

plt.savefig("../OUTPUTS/glucose_distribution.png")

plt.show()

# %% [markdown]
# ### Glucose Distribution
# 
# Most patients have glucose levels between 80 and 140.
# 
# The distribution is approximately normal with a slight right skew.
# 
# A small number of zero values are present and may represent missing measurements.

# %%
plt.figure(figsize=(6,4))

plt.boxplot(df["Glucose"])

plt.title("Glucose Boxplot")
plt.ylabel("Glucose")

plt.savefig("../OUTPUTS/glucose_boxplot.png")

plt.show()

# %% [markdown]
# ### Glucose Outliers
# 
# A few extremely low glucose values are present.
# 
# These likely represent missing or incorrectly recorded data rather than true measurements.

# %%
plt.figure(figsize=(6,4))

plt.hist(df["BMI"])

plt.title("BMI Distribution")
plt.xlabel("BMI")
plt.ylabel("Frequency")

plt.savefig("../OUTPUTS/bmi_distribution.png")

plt.show()

# %% [markdown]
# ### BMI Distribution
# 
# Most patients have BMI values between 25 and 40.
# 
# The distribution shows a slight right skew.
# 
# Several patients exhibit very high BMI values, while a few zero values likely indicate missing data.

# %%
plt.figure(figsize=(6,4))

plt.boxplot(df["BMI"])

plt.title("BMI Boxplot")
plt.ylabel("BMI")

plt.savefig("../OUTPUTS/bmi_boxplot.png")

plt.show()

# %% [markdown]
# ### BMI Outliers
# 
# One BMI value near zero appears invalid.
# 
# Several high BMI observations (>50) are present and likely represent genuine extreme cases rather than errors.

# %%
plt.figure(figsize=(6,4))

plt.hist(df["Insulin"])

plt.title("Insulin Distribution")
plt.xlabel("Insulin")
plt.ylabel("Frequency")

plt.savefig("../OUTPUTS/insulin_distribution.png")

plt.show()

# %% [markdown]
# ### Insulin Distribution Analysis
# 
# The insulin distribution is highly right-skewed.
# 
# Most patients have relatively low insulin values, while a small number of observations exhibit extremely high insulin levels.
# 
# A large concentration of values near zero is also present, suggesting possible missing or unrecorded measurements.
# 
# The distribution is not symmetric and contains substantial variability.

# %%
plt.figure(figsize=(6,4))

plt.boxplot(df["Insulin"])

plt.title("Insulin Boxplot")
plt.ylabel("Insulin")

plt.savefig("../OUTPUTS/insulin_boxplot.png")

plt.show()

# %% [markdown]
# ### Insulin Outlier Analysis
# 
# The insulin variable contains a large number of extreme outliers.
# 
# Most observations are concentrated below 150, while several values extend beyond 800.
# 
# Additionally, a significant number of observations contain an insulin value of zero, which is likely indicative of missing or unrecorded measurements.
# 
# The presence of numerous outliers and zero values suggests that this variable may require additional cleaning before further statistical analysis.

# %%
plt.figure(figsize=(6,4))

plt.hist(df["Age"])

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Frequency")

plt.savefig("../OUTPUTS/age_distribution.png")

plt.show()

# %% [markdown]
# ### Age Distribution Analysis
# 
# The age distribution is strongly right-skewed.
# 
# Most patients in the dataset are between 20 and 35 years old, with the frequency of observations decreasing as age increases.
# 
# The dataset contains relatively few older individuals, indicating that younger patients make up the majority of the study population.
# 
# The distribution suggests that age is not evenly represented across all age groups.

# %%
plt.figure(figsize=(6,4))

plt.boxplot(df["Age"])

plt.title("Age Boxplot")
plt.ylabel("Age")

plt.savefig("../OUTPUTS/age_boxplot.png")

plt.show()

# %% [markdown]
# ### Age Outlier Analysis
# 
# The age variable contains a small number of high-value observations.
# 
# These observations correspond to older individuals and appear to be realistic rather than data-entry errors.
# 
# Unlike the BMI and Insulin variables, no suspicious zero values or extreme anomalies are observed.
# 
# The age data appears to be relatively clean and suitable for further analysis.

# %%
df["Outcome"].value_counts()

# %%

plt.figure(figsize=(6,4))

df["Outcome"].value_counts().plot(kind="bar")

plt.title("Outcome Distribution")
plt.xlabel("Outcome")
plt.ylabel("Count")

plt.savefig("../OUTPUTS/outcome_distribution.png")

plt.show()

# %% [markdown]
# ### Outcome Distribution Analysis
# 
# The outcome variable represents whether a patient has diabetes (1) or does not have diabetes (0).
# 
# The dataset contains a larger number of non-diabetic patients compared to diabetic patients.
# 
# Although both classes are represented, the distribution is not perfectly balanced.
# 
# This imbalance should be considered when interpreting results and performing further analysis.

# %%
(df["Outcome"].value_counts(normalize=True) * 100).round(2)

# %% [markdown]
# ### Outcome Percentage Analysis
# 
# Approximately one-third of the patients in the dataset are diabetic, while the remaining patients are non-diabetic.
# 
# The prevalence of diabetes within this dataset is therefore substantial and provides sufficient observations for comparative analysis.

# %%
df["Outcome"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Diabetes Outcome Percentage")

plt.ylabel("")

plt.show()



# %% [markdown]
# ##  Comparative Analysis: Diabetic  VS  Non-Diabetic Patients

# %%
df.groupby("Outcome")["Glucose"].mean()

# %%
df.groupby("Outcome")["Glucose"].mean().plot(kind="bar")

plt.title("Average Glucose by Outcome")
plt.xlabel("Outcome")
plt.ylabel("Average Glucose")

plt.show()

# %% [markdown]
# #### Glucose Comparison
# 
# Diabetic patients have a significantly higher average glucose level (141.26) compared to non-diabetic patients (109.98).
# 
# This substantial difference suggests that elevated glucose levels are strongly associated with diabetes.

# %%
df.groupby("Outcome")["BMI"].mean()

# %%
df.groupby("Outcome")["BMI"].mean().plot(kind="bar")

plt.title("Average BMI by Outcome")
plt.xlabel("Outcome")
plt.ylabel("Average BMI")

plt.show()

# %% [markdown]
# #### BMI Comparison
# 
# The average BMI of diabetic patients (35.14) is higher than that of non-diabetic patients (30.30).
# 
# This finding indicates that higher body mass index may be associated with an increased likelihood of diabetes.

# %%
df.groupby("Outcome")["Insulin"].mean()

# %%
df.groupby("Outcome")["Insulin"].mean().plot(kind="bar")

plt.title("Average Insulin by Outcome")
plt.xlabel("Outcome")
plt.ylabel("Average Insulin")

plt.show()

# %% [markdown]
# #### Insulin Comparison
# 
# Diabetic patients exhibit higher average insulin levels (100.34) compared to non-diabetic patients (68.79).
# 
# However, the insulin variable contains many missing or zero values and several extreme outliers, which may influence the average.

# %%
df.groupby("Outcome")["Age"].mean()

# %%
df.groupby("Outcome")["Age"].mean().plot(kind="bar")

plt.title("Average Age by Outcome")
plt.xlabel("Outcome")
plt.ylabel("Average Age")

plt.show()

# %% [markdown]
# #### Age Comparison
# 
# The average age of diabetic patients (37.07 years) is higher than that of non-diabetic patients (31.19 years).
# 
# This suggests that diabetes is more common among older individuals in this dataset.

# %% [markdown]
# ## Comparative Analysis Conclusion
# 
# The comparative analysis reveals clear differences between diabetic and non-diabetic patients.
# 
# Diabetic patients tend to have:
# 
# - Higher glucose levels
# - Higher BMI values
# - Higher insulin levels
# - Greater average age
# 
# Among all variables examined, glucose shows the largest difference between the two groups, indicating that it may be one of the strongest factors associated with diabetes.
# 
# These findings are consistent with established medical knowledge regarding diabetes risk factors and characteristics.

# %% [markdown]
# ## Correlation Analysis

# %%
df.corr()

# %%
plt.figure(figsize=(8,6))

plt.imshow(df.corr(), cmap="coolwarm")

plt.colorbar()

plt.xticks(range(len(df.columns)), df.columns, rotation=90)
plt.yticks(range(len(df.columns)), df.columns)

plt.title("Correlation Matrix")

plt.savefig("../OUTPUTS/correlation_matrix.png")

plt.show()

# %% [markdown]
# ## Correlation Analysis Conclusion
# 
# The correlation matrix reveals that glucose has the strongest relationship with diabetes outcome, followed by BMI, age, and number of pregnancies.
# 
# Key observations include:
# 
# - Glucose exhibits the strongest positive correlation with diabetes (0.467).
# - BMI shows a moderate positive correlation with diabetes (0.293).
# - Age and pregnancies also demonstrate positive relationships with diabetes occurrence.
# - Blood pressure and skin thickness exhibit relatively weak correlations with diabetes.
# 
# These findings suggest that glucose level, BMI, and age are among the most important variables associated with diabetes in this dataset.

# %% [markdown]
# # Final Conclusion
# 
# This exploratory data analysis was conducted on the Pima Indians Diabetes Dataset to identify factors associated with diabetes.
# 
# Key findings include:
# 
# - The dataset contains 768 patient records and 9 variables.
# - Several variables, particularly Glucose, BMI, and Insulin, contain zero values that likely represent missing measurements.
# - Diabetic patients exhibit higher average glucose levels, BMI values, insulin levels, and age compared to non-diabetic patients.
# - Glucose demonstrated the strongest correlation with diabetes outcome, making it the most influential variable in the dataset.
# - BMI and age also showed meaningful associations with diabetes.
# 
# Overall, the analysis indicates that elevated glucose levels, higher BMI, and increasing age are important characteristics associated with diabetes within this dataset.


