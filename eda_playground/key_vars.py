import clean_data_import
from data_preparation import clean_data
import seaborn as sns
import matplotlib.pyplot as plt

# Plot the distribution of length of stay
sns.histplot(clean_data.cohort_data['length_of_stay'], kde=True)
plt.title('Distribution of Length of Stay')
plt.show()

# Boxplot to compare length of stay between different drug groups
sns.boxplot(x='drug', y='length_of_stay', data=clean_data.cohort_data)
plt.title('Length of Stay by Drug Exposure')
plt.show()

# Check balance of discharge location across drug groups
sns.countplot(x='discharge_location', hue='drug', data=clean_data.cohort_data)
plt.title('Discharge Location by Drug Exposure')
plt.show()
