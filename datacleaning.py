import pandas as pd
import numpy as np
import csv

filename = 'finalfile.csv'
f = open(filename, 'w')
f.write('Location,Title,Price,Style,Bedrooms,Bathrooms,Size,Air Conditioned  \n')
f.close()


'''
df = pd.read_csv('products.csv', encoding="ISO-8859-1")


#Remove "Wanteds"
df = df[df["Title"].str.contains("Wanted:") == False]

#Bedroom number only
df["Bedrooms"] = df["Bedrooms"].str.replace('Bedrooms: ', '')

#Bathroom number only
df["Bathrooms"] = df["Bathrooms"].str.replace('Bathrooms: ', '')

#Turn "Not Available" to "N/A"
df["Size"] = df["Size"].str.replace('Not Available', 'N/A')

#Parse bedrooms (den, studio)
df['Den'] = np.where(df["Bedrooms"].str.find("Den") > 0, "Yes", "No")
df["Bedrooms"] = df["Bedrooms"].str.replace('+ Den ', '')
'''