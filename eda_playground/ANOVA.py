import clean_data_import
from data_preparation import clean_data
from scipy.stats import f_oneway

# Perform ANOVA
acetaminophen_los = clean_data.cohort_data[clean_data.cohort_data['drug'] == 'Acetaminophen']['length_of_stay']
lorazepam_los = clean_data.cohort_data[clean_data.cohort_data['drug'] == 'Lorazepam']['length_of_stay']
atorvastatin_los = clean_data.cohort_data[clean_data.cohort_data['drug'] == 'Atorvastatin']['length_of_stay']

f_stat, p_value = f_oneway(acetaminophen_los, lorazepam_los, atorvastatin_los)
print(f'F-statistic: {f_stat}, P-value: {p_value}')
