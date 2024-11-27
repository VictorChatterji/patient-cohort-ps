import clean_data_import
from data_preparation import clean_data
from scipy.stats import chi2_contingency
import pandas as pd

# Create contingency table for discharge location by drug group
contingency_table = pd.crosstab(clean_data.cohort_data['drug'], clean_data.cohort_data['long_title'])

# Perform chi-square test
chi2, p_value, _, _ = chi2_contingency(contingency_table)
print(f'Chi-square statistic: {chi2}, P-value: {p_value}')
