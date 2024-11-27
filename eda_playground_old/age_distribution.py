import matplotlib.pyplot as plt
import pandas as pd

patients = pd.read_csv('data/patients_final.csv')
# admissions = pd.read_csv('data/admissions.csv')

print(patients.head())


# plot age distribution
# Plot age distribution
plt.hist(patients['anchor_age'], bins=20, alpha=0.7)
plt.title('Patient Age Distribution')
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.show()