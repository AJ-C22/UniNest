import pandas as pd
import numpy as np
import csv


df = pd.read_csv('finalfile.csv', encoding="ISO-8859-1")


#Remove "Wanteds"
df = df[df["Title"].str.contains("Wanted:") == False]

#Bedroom number only
df["Bedrooms"] = df["Bedrooms"].str.replace('Bedrooms: ', '')

#Bathroom number only
df["Bathrooms"] = df["Bathrooms"].str.replace('Bathrooms: ', '')

#Turn "Not Available" to "N/A"
df["Size(sqft)"] = df["Size(sqft)"].str.replace('Not Available', 'N/A')

#Parse bedrooms (den, studio)
df['Den'] = np.where(df["Bedrooms"].str.find("Den") > 0, "Yes", "No")
df["Bedrooms"] = df["Bedrooms"].str.replace('+ Den', '')

#Remove extra headers
df = df[df["Title"].str.contains("Title") == False]
print(df)

#Remove incorrectly scraped data
df = df[df["Style"].str.contains("No") == False]

#Remove dollar sign
df["Price($)"] = df["Price($)"].str.replace('$', '')
df["Price($)"] = df["Price($)"].str.replace('.00', '')


#Turn df into csv
#df.to_csv("housing_cleaned.csv")