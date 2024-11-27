import matplotlib.pyplot as plt
import pandas as pd

lab_events = pd.read_csv('data/labevents.csv')

# Select a specific lab test (e.g., Glucose levels)
glucose_test = lab_events[lab_events['itemid'] == 50809]  # Glucose test item ID in MIMIC-IV
glucose_test = glucose_test.dropna(subset=['valuenum'])  # Drop rows with missing values

# Boxplot to detect outliers
plt.boxplot(glucose_test['valuenum'], vert=False)
plt.title('Glucose Levels Boxplot')
plt.xlabel('Glucose Level')
plt.show()

# Summary statistics
print("Glucose Test Statistics:")
print(glucose_test['valuenum'].describe())