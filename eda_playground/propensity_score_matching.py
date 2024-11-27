from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import clean_data_import
from data_preparation import clean_data
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import seaborn as sns
import matplotlib.pyplot as plt


cohort_data = clean_data.cohort_data


print(cohort_data[['anchor_age', 'drug', 'long_title']].isnull().sum())

# Create binary target variable for Acetaminophen vs Other drugs
cohort_data['drug_binary'] = cohort_data['drug'].apply(lambda x: 1 if x == 'Acetaminophen' else 0)

# Define the features (age + long_title features)
X = cohort_data[['anchor_age', 'length_of_stay']]
y = cohort_data['drug_binary']  # Target: Acetaminophen (1) or Other (0)

# Split the data into training and testing sets (optional, for model validation)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the logistic regression model
model = LogisticRegression(max_iter=5000)
model.fit(X_train, y_train)

# Get the predicted propensity scores (probabilities of receiving Acetaminophen)
cohort_data['propensity_score'] = model.predict_proba(X)[:, 1]

# print(cohort_data.head())


# Plot the distribution of propensity scores
sns.histplot(cohort_data['propensity_score'], kde=True)
plt.title('Distribution of Propensity Scores')
plt.show()

# from sklearn.neighbors import NearestNeighbors

# # Separate treated and control groups
# treated = cohort_data[cohort_data['drug'] == 'Acetaminophen']
# control = cohort_data[cohort_data['drug'] != 'Acetaminophen']

# # Nearest neighbor matching based on propensity score
# nbrs = NearestNeighbors(n_neighbors=1).fit(control[['propensity_score']])
# distances, indices = nbrs.kneighbors(treated[['propensity_score']])

# # Get the matched control group based on nearest propensity score
# matched_control = control.iloc[indices.flatten()]
# matched_data = pd.concat([treated, matched_control])

# # Check matched data
# print(matched_data[['subject_id', 'drug', 'propensity_score']].head())

