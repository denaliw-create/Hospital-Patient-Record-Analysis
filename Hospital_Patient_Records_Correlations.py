import pandas as pd

# Allows for the us to use and view the Hospital Patient Records dataset
df = pd.read_csv('Patient_Encounter_Analysis_Raw.csv')
print(df)

# Correlation between cost and length of stay
print(df[['cost', 'length_of_stay']].corr())

# Corelation between age and cost
print(df[['cost', 'age']].corr())

# Correlation between cost and satisfaction
print(df[['cost', 'satisfaction']].corr())

# Correlation between age and satisfaction
print(df[['age', 'satisfaction']].corr())

# Correlation between age and length of stay
print(df[['age', 'length_of_stay']].corr())

# Correlation between length of stay and satisfaction
print(df[['length_of_stay', 'satisfaction']].corr())


# Correlation between age and length of stay
df['readmission_encoded'] = df['readmission'].map({'Yes': 1, 'No': 0})
print(df[['age', 'readmission_encoded']].corr())

# Correlation between cost and procedure outcomes
df['outcome_encoded'] = df['outcome'].map({'Recovered': 1, "Stable": 0})
print(df[['cost', 'outcome_encoded']].corr())

