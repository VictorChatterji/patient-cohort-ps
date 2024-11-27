import clean_data_import
from data_preparation import clean_data
import seaborn as sns
import matplotlib.pyplot as plt

corr_matrix = clean_data.cohort_data[['length_of_stay', 'anchor_age']].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix')
plt.show()