import clean_data_import
from data_preparation import clean_data

print(clean_data.cohort_data.info())
print(clean_data.cohort_data.describe())
drug_value_count = clean_data.cohort_data['drug'].value_counts()
print(drug_value_count)