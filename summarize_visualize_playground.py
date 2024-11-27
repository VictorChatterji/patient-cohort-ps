import matplotlib.pyplot as plt
import pandas as pd
import os

x = pd.read_csv('data/cohort_final.csv')
# y = pd.read_csv('data/patients.csv')
# procedureevents = pd.read_csv('data/procedureevents.csv')

# print(procedureevents.info())
# print(procedureevents["value"])
# print(icd_procedures[icd_procedures["long_title"].str.contains('arterial catheter', case=False, na=False)])
# print(x[x["label"].str.contains("arterial", case=False, na=True)])

# print(x.info())
print(x.shape)
# print(y.info())

