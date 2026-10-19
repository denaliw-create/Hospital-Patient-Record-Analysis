# Hospital-Patient-Records Project 
<img width="554" height="554" alt="images" src="https://github.com/user-attachments/assets/cf7039a2-6060-4124-81b7-5433a2feff6d" />

## Overview
The [Hospital Patient Records dataset](https://www.kaggle.com/datasets/blueblushed/hospital-dataset-for-practice/data) contains synthetic records of 1000 patients treated at a hospital, including demographic information, medical conditions, treatments administered, medical expenses incurred, and current health status. You can explore several patterns, trends, and insights in patient care, recovery rates, and treatment efficacy using this dataset. 


# Installation and Setup
To run this project on your machine, install a SQL-supported database management system (DBMS) or integrated development environment (IDE). For this project, I used DataGrip, an IDE created by JetBrains.

After installing a DBMS or IDE, the next step is to create databases using the following entity relationship diagram (ERD):

<img width="1011" height="565" alt="Screenshot 2026-10-15 at 8 08 25 PM" src="https://github.com/user-attachments/assets/58a05472-4e2d-4657-bc72-87187f8d46a8" />

For additional guidance, you can view the [steps](https://github.com/denaliw-create/Hospital-Patient-Record-Analysis/blob/f1d7a8a0daeae6ffd4da99e7882dfb2482b37e71/Hospital_Patient_Records_Queries) I took to create the three databases.

Next, you can use the [provided](https://github.com/denaliw-create/Hospital-Patient-Record-Analysis/blob/ecbb78a9cc11cbee80403ffc7ed57ad7264b6abe/dataset/diag_and_procedure_type.csv) [datasets](https://github.com/denaliw-create/Hospital-Patient-Record-Analysis/blob/ecbb78a9cc11cbee80403ffc7ed57ad7264b6abe/dataset/Patient_Encounter_Analysis_Raw.csv) and export the data using the .csv files that can be found there. To export the data in DataGrip, you can click the database symbol at the top of the screen to open the database explorer. From there, you can right-click on the tables you created for this project and click: **Import/Export** > **Export Data to File**

## Tools/Applications Used: 
  * Microsoft Excel - Version 16.114
  * DataGrip - Version 2026.1.4
  * Visual Studio Code 5 - Version: 1.136.1 (Universal)
  * Tableau Desktop - Version 2026.2.1

## Programming Languages & Libraries Used:
  * SQL, Python, Pandas

## Key Findings

### Correlation Analysis
- **Age and satisfaction** had the strongest correlation in the dataset 
  (r = -0.75), meaning older patients reported significantly lower 
  satisfaction scores
- **Cost and satisfaction** showed a moderate negative correlation 
  (r = -0.47), suggesting higher-cost encounters are associated with 
  lower patient satisfaction
- **Age and cost** showed a moderate positive correlation (r = 0.30), 
  indicating older patients tend to incur higher medical costs
- Correlations between length of stay and other variables were weak 
  across the board, suggesting LOS is not a strong predictor of cost, 
  satisfaction, or age in this dataset

### Readmission
- Heart Attack (100%) and Heart Disease (98.46%) had the highest 
  readmission rates by far
- 8 diagnoses had 0% readmission rates, including Hypertension, 
  Allergic Reaction, and Osteoarthritis
- Readmitted patients reported lower average satisfaction (3.1) 
  compared to non-readmitted patients (3.8)

### Cost and Length of Stay
- Cancer ($25,000) and Prostate Cancer ($20,000) were associated 
  with the highest average costs
- Allergic Reaction ($100) and Fractured Arm ($500) had the lowest 
  average costs
- Length of stay followed a similar pattern to cost by diagnosis

### Dataset Limitations
- Each procedure maps exclusively to one outcome (100% Recovered or 
  100% Stable), which is characteristic of synthetic data and limits 
  outcome analysis
