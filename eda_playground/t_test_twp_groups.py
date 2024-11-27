import clean_data_import
from data_preparation import clean_data


from scipy.stats import ttest_ind

# Separate the data by drug exposure
acetaminophen_los = clean_data.cohort_data[clean_data.cohort_data['drug'] == 'Acetaminophen']['length_of_stay']
lorazepam_los = clean_data.cohort_data[clean_data.cohort_data['drug'] == 'Lorazepam']['length_of_stay']

# Perform t-test
t_stat, p_value = ttest_ind(acetaminophen_los, lorazepam_los)
print(f'T-statistic: {t_stat}, P-value: {p_value}')


# Interpretation: If p_value < 0.05, the difference in length of stay between the two drug groups is statistically significant.