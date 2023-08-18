import pandas as pd
import numpy as np
import csv


df = pd.read_csv('finalfile.csv', encoding="ISO-8859-1")


#Remove "Wanteds"
df = df[df["Title"].str.contains("Wanted:") == False]

#Bedroom number only
df["Bedrooms"] = df["Bedrooms"].str.replace('Bedrooms: ', '')
df = df[df["Bedrooms"].str.contains("N/A") == False]

#Bathroom number only
df["Bathrooms"] = df["Bathrooms"].str.replace('Bathrooms: ', '')
df = df[df["Bathrooms"].str.contains("N/A") == False]

#Turn "Not Available" to "N/A"
df["Size(sqft)"] = df["Size(sqft)"].str.replace('Not Available', 'N/A')


#Parse bedrooms (den, studio)
df['Den'] = np.where(df["Bedrooms"].str.find("Den") > 0, "Yes", "No")
df["Bedrooms"] = df["Bedrooms"].str.replace('+ Den', '')

df['Bachelor/Studio'] = np.where(df["Bedrooms"].str.find("Bachelor/Studio") > 0, "Yes", "No")
df["Bedrooms"] = df["Bedrooms"].str.replace('Bachelor/Studio', '0')

#Remove extra headers
df = df[df["Title"].str.contains("Title") == False]

#Remove incorrectly scraped data
df = df[df["Style"].str.contains("No") == False]

#Remove dollar sign
df["Price"] = df["Price"].str.replace('$', '')
df["Price"] = df["Price"].str.replace('.00', '')

#Remove "Please Contact" prices
df = df[df["Price"].str.contains("Please Contact") == False]
df = df = df[df["Title"].str.contains("Please Contact") == False]

#Ensure price is numeric value only
df = df[df["Price"].str.contains("House") == False]

#Turn df into csv
df.to_csv("housing_cleaned.csv")