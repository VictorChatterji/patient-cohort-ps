import matplotlib.pyplot as plt
import pandas as pd

icustays = pd.read_csv('data/icustays.csv')
procedures = pd.read_csv('data/procedureevents.csv')


print(icustays.head())
print(procedures.tail())

merged = pd.merge(icustays, procedures, on="stay_id")
iac_procedures = merged[merged["itemid"] == 224275]


iac_procedures["time_to_iac"] = (
    pd.to_datetime(iac_procedures["starttime"]) - pd.to_datetime(iac_procedures["intime"])
).dt.total_seconds() / 3600 #convert to hours

# print(iac_procedures.head())

# Plot distribution
plt.hist(iac_procedures['time_to_iac'], bins=20, alpha=0.7)
plt.title('Time to IAC Placement (Hours)')
plt.xlabel('Hours')
plt.ylabel('Frequency')
plt.show()