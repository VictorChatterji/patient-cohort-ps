import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt


admissions = pd.read_csv('data/admissions.csv')
icustays = pd.read_csv('data/icustays.csv')
procedureevents = pd.read_csv('data/procedureevents.csv')

iac_procedures= procedureevents[procedureevents["itemid"] == 224275]
iac_procedures = pd.merge(iac_procedures, icustays, on="stay_id")
# iac_procedures = pd.merge(iac_procedures, admissions[['hadm_id', 'hospital_expire_flag']], on='hadm_id')
print(iac_procedures.info())
print(iac_procedures.head())
iac_procedures["iac_placed"] = True
# print(iac_procedures.info())
# print(outcomes.info())

# correlation_data = iac_procedures[['los', 'hospital_expire_flag', 'iac_placed']]

# corr_matrix = correlation_data.corr()

# sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
# plt.title('Correlation Matrix: LOS, Mortality and IAC Placement')
# plt.show()