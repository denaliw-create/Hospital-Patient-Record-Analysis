# Hospital-Patient-Records Project 
<img width="554" height="554" alt="images" src="https://github.com/user-attachments/assets/cf7039a2-6060-4124-81b7-5433a2feff6d" />

# Overview
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
  * SQL was used for creating queries and creating the databases.
  * Python was the programming language utilized for its libraries. 
  * Pandas was the Python library used for identifying correlations between different columns.

## Correlation Analysis Steps
1. Place `Patient_Encounter_Analysis_Raw.csv` in an accessible folder in VS Code or any other Python-supported IDE.
2. Run `Hospital_Patient_Records_Correlations.py`

## Key Findings

### Diagnoses & Procedures
- The most common diagnoses were Heart Attack and Fractured Leg, 
  each with 67 cases. The least common was Osteoarthritis with 64 cases.
- Diagnosis counts were relatively evenly distributed across all 
  15 conditions, with a difference of only 3 cases between the most 
  and least common.

### Cost & Utilization
- Cancer had the highest average cost ($25,000) and longest average 
  length of stay (42.7 days). Prostate Cancer was a close second 
  at $20,000 and 41.6 days.
- There is a weak positive correlation (r = 0.11) between length of 
  stay and cost, suggesting that LOS alone is not a strong driver 
  of hospital costs in this dataset.

### Readmission
- Heart Attack (100%) and Heart Disease (98.46%) had the highest 
  readmission rates among all diagnoses.
- Readmitted patients reported lower average satisfaction (3.11) 
  compared to non-readmitted patients (3.78), a difference of 0.67.
- Age is a weak predictor of readmission (r = 0.22).

### Outcomes
- Procedures such as Cast and Physical Therapy, Appendectomy, and 
  X-Ray and Splint had 100% recovery rates.
- Note: Each procedure maps exclusively to one outcome in this 
  dataset, which is characteristic of synthetic data and limits 
  the depth of outcome analysis.
- Cost very weakly correlates with better outcomes (r = .25).

### Patient Satisfaction
- Age was the strongest predictor of satisfaction. Patients under 
  30 reported an average satisfaction of 5.0, while patients aged 
  70 or older reported the lowest average of 2.4 — a difference 
  of over 2.6 points.
- Readmitted patients reported lower satisfaction (3.11) compared 
  to non-readmitted patients (3.78).
- Procedure type was associated with satisfaction scores. Patients 
  who received an X-Ray and Splint or Epinephrine Injection reported 
  the highest average satisfaction (5.0), while those who received 
  a CT Scan and Medication or Cardiac Catheterization reported the 
  lowest (2.0).

### Actionable Insights
- Due to the nature of this dataset, the data and findings may not be realistic. However, if this were a real-world dataset with genuine findings, a hospital's administrative team could investigate satisfaction scores below 5 more deeply; confounding variables not in the dataset could also affect satisfaction scores, such as how medical staff treated patients. 

- Additionally, the most common diagnoses have been identified as heart attacks and leg fractures. Consequently, medical institutions and employees can learn about patients' social determinants of health (SDOH) and empower them to make decisions that may help avoid the aforementioned diagnoses.

### Dataset Limitations
- Each procedure maps exclusively to one outcome (100% Recovered or 
  100% Stable), which is frequently observed in synthetic data and limits 
  outcome analysis.
