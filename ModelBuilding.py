import pandas as pandas
import matplotlib.pylot as plt
import numpy as np 

df = pd.read_csv('housing_cleaned.csv')
df2 = pd.read_csv('housing_cleaned.csv')

df2 = df2[df2["Size(sqft)"].str.contains("N/A") == False]
df2 = df2[df2["Size(sqft)"].str.contains("Limited") == False]
df2= df2[df2["Bedrooms"].str.contains("5+") == False]
df = df[df["Bedrooms"].str.contains("5+") == False]
df2['Bedrooms'] = df2["Bedrooms"].astype(float)
df2['Bathrooms'] = df2["Bathrooms"].astype(float)
df['Bedrooms'] = df["Bedrooms"].astype(float)
df['Bathrooms'] = df["Bathrooms"].astype(float)

#Choose relevant columns
df.columns
df_model = df[['Location']]
#Get dummy data
#Train test split
#Multiple linear regression
#Lasso regression
#Random Forest
#Tune models
#Test Ensembles

