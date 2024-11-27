import matplotlib.pyplot as plt
import pandas as pd

patients = pd.read_csv('data/patients_final.csv')

gender_counts = patients['gender'].value_counts()
gender_counts.plot(kind='bar', color=['blue', 'pink'], alpha=0.7)
plt.title('Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()