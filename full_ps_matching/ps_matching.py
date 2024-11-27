# Importing necessary libraries
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
# Step 2: Importing the dataset and displaying the first 5 rows
df= pd.read_csv("data/cohort_final.csv")
df['drug_binary'] = df['drug'].apply(lambda x: 1 if x == 'Acetaminophen' else 0)

df.head()
# Step 3: Exploring the data~1
print(df.dtypes)  # Displaying the data types of the columns
# Step 3: Exploring the data~2
print(df.describe())  # Displaying the summary statistics of the dataset
# Step 4: Visualizing the distribution of covariates
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
sns.countplot(x='gender', hue='drug_binary', data=df, ax=axes[0])  # Visualizing the distribution of Gender
axes[0].set_title('Distribution of Gender')
sns.countplot(x='length_of_stay', hue='drug_binary', data=df, ax=axes[1])  # Visualizing the distribution of BaselineHealth
axes[1].set_title('Distribution of Length of Stay')
plt.show()
# Step 5: Splitting the data into treatment and control groups
treatment_df = df[df["drug_binary"] == 1]  # Creating a subset for the treatment group
control_df = df[df["drug_binary"] == 0]  # Creating a subset for the control group
df.shape
treatment_df.shape, control_df.shape
# Step 6: Propensity score model using Logistic Regression
log_reg_model = LogisticRegression()  # Initializing the logistic regression model
df['gender_number'] = df['gender'].apply(lambda x: 1 if x == 'M' else 0)
X_log_reg = df[["anchor_age", "gender_number", "length_of_stay"]]  # Independent variables for the model
y_log_reg = df["drug_binary"]  # Dependent variable for the model
log_reg_model.fit(X_log_reg, y_log_reg)  # Fitting the logistic regression model

# Calculating and storing the propensity scores using Logistic Regression
df["PropensityScore_LogReg"] = log_reg_model.predict_proba(X_log_reg)[:, 1]

df["PropensityScore_LogReg"]
# Step 7: Propensity score model using KNN
knn_model = KNeighborsClassifier(n_neighbors=5)  # Initializing the KNN model
X_knn = df[["anchor_age", "gender_number", "length_of_stay"]]  # Independent variables for the KNN model
y_knn = df["drug_binary"]  # Dependent variable for the KNN model
knn_model.fit(X_knn, y_knn)  # Fitting the KNN model

# Calculating and storing the propensity scores using KNN
df["PropensityScore_KNN"] = knn_model.predict_proba(X_knn)[:, 1]
df['PropensityScore_KNN']
# Step 8: Visualizing the propensity scores
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
sns.histplot(df, x='PropensityScore_LogReg', hue='drug_binary', kde=True, ax=axes[0])  # Visualizing the propensity score distribution from Logistic Regression
axes[0].set_title('Propensity Score Distribution (Logistic Regression)')
sns.histplot(df, x='PropensityScore_KNN', hue='drug_binary', kde=True, ax=axes[1])  # Visualizing the propensity score distribution from KNN
axes[1].set_title('Propensity Score Distribution (KNN)')
plt.show()
# Step 9: Propensity Score Matching
# test_size_percentage = 0.5  # Adjusting the test size percentage
# treated_matched, control_matched = train_test_split(control_df, test_size=test_size_percentage, random_state=42)  # Performing the matching

# matched_df = pd.concat([treatment_df, treated_matched])  # Combining the treated and matched control groups
# matched_df.head()
# # Step 10: Evaluating the treatment effect
# # effect = matched_df["Outcome"].mean() - control_df["Outcome"].mean()  # Calculating the average treatment effect
# # print(f"Average Treatment Effect: {effect}")  # Displaying the average treatment effect
# # Step 11: Fitting the logistic regression model using statsmodels
# logit_model = sm.Logit(matched_df['drug_binary'], sm.add_constant(matched_df[['anchor_age', 'gender', 'length_of_stay']]))  # Initializing the logistic regression model using statsmodels
# logit_result = logit_model.fit()  # Fitting the logistic regression model
# print(logit_result.summary())  # Displaying the summary of the logistic regression model
# # Step 12: Assessing balance after matching
# fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(12, 5))
# sns.boxplot(x='drug_binary', y='age', data=matched_df, ax=axes[0])  # Visualizing the age distribution after matching
# axes[0].set_title('Age Distribution - Matched')
# sns.boxplot(x='drug_binary', y='length_of_stay', data=matched_df, ax=axes[1])  # Visualizing the outcome distribution after matching
# axes[1].set_title('Length of Stay Distribution - Matched')
# plt.show()
