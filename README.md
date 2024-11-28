# Patient Cohort PS - Local Setup

This project is focused on patient cohorting using medical data for clinical trials. It uses various technologies and libraries to process and analyze patient data for cohorting. Follow the steps below to run the project locally.

## Prerequisites

Before running the project locally, make sure you have the following installed:

- **Python** (>= 3.8)
- **pip** (Python package installer)
- **git** (for cloning the repository)

Additionally, the project may rely on other services or APIs. Make sure you have access to them, as they might be required to fully run the application.

## Cloning the Repository

1. Clone the repository using Git:

   ```bash
   git clone https://github.com/VictorChatterji/patient-cohort-ps.git
   cd patient-cohort-ps
   ```

## Setting Up the Environment

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**:
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Install required dependencies**:

   Inside the project folder, run the following:

   ```bash
   pip install -r requirements.txt
   ```

   This will install all necessary Python packages and dependencies.


## Running the Project

1. **Run the application**:

   After the environment is set up and all dependencies are installed, you can run the application using:

   ```bash
   python <file>.py
   ```



# Project Thought Process

This document outlines the step-by-step thought process for creating patient cohorts and performing further analysis using the provided codebase.

## Step 1: Sample Patient Data

The sample patient data is located in the `data/patients_final.csv` file. This CSV file contains the necessary patient data that will be used throughout the cohort creation and subsequent analysis.

## Step 2: Database Related Code

The code that interacts with the database is found in `cohort_creation/database.py`. This file contains the logic for accessing and querying the database to support cohort creation.

## Step 3: Creating Cohorts

We will create cohorts based on specific objectives outlined in `cohort_creation/cohort.py`. This file contains the logic for defining the cohort creation rules based on the desired objectives. 

## Step 4: Exporting Data

Once the cohorts are created, we export the data by running the script located in `cohort_creation/cohort_export.py`. This script handles the export process, and all exported data will be saved as CSV files.

## Step 5: CSV Exports Folder

All exported files, including the cohort data, will be found in the `csv_exports` folder. The key file to look for here is `cohort_filtered.csv`, which contains the filtered cohort data that will be used for further analysis.

## Step 6: Data Preparation for Propensity Analysis

After obtaining the filtered cohort data (`cohort_filtered.csv`), the next step is data preparation for propensity analysis. The script that performs this task is located in `clean_data.py`. This file processes the data and prepares it for the next steps in the analysis pipeline.

## Step 7: Exploratory Data Analysis (EDA)

Once the data is clean, we proceed with exploratory data analysis (EDA). This step is critical for understanding the data and identifying key trends or patterns. The code for EDA can be found in the `eda_playground` directory. This will help us explore the data and gain insights into the cohorts.

## Step 8: Propensity Score Matching

Finally, once we have completed the exploratory data analysis, we move on to propensity score matching (PSM) for further analysis. The relevant code for propensity score matching is located in the `full_ps_matching` folder. This step will help in matching cohorts based on their propensity scores, which is essential for performing causal inference analysis.

---

### Codebase Overview

Here is a summary of the files involved:

- **`data/patients_final.csv`**: Contains the sample patient data.
- **`cohort_creation/database.py`**: Code for interacting with the database.
- **`cohort_creation/cohort.py`**: Logic for creating cohorts based on objectives.
- **`cohort_creation/cohort_export.py`**: Code for exporting cohort data.
- **`csv_exports/`**: Folder where CSV exports are saved, including `cohort_filtered.csv`.
- **`clean_data.py`**: Data preparation code for propensity analysis.
- **`eda_playground/`**: Directory for exploratory data analysis code.
- **`full_ps_matching/`**: Directory for propensity score matching code.

This workflow provides a structured approach to cohort creation, data analysis, and further statistical modeling.



## Contributing

If you wish to contribute to the project, feel free to fork the repository and submit a pull request. Please follow the contribution guidelines provided in the project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


## TODO

1. SQL implementation where table already exists issue resolution

## Author
Chatterji N

