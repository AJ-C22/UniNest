import pandas as pd

df = pd.read_csv('products.csv', encoding="ISO-8859-1")


#Remove "Wanteds"
df = df[df["Title"].str.contains("Wanted:") == False]

#Bedroom number only

#Bathroom number only
df[" Bathrooms"] = df[" Bathrooms"].str.replace('Bathrooms: ', '')

#Turn "Not Available" to "N/A"
df[" Size"] = df[" Size"].str.replace('Not Available', 'N/A')

#Parse bedrooms (den, studio)
den_val = df[" Bedrooms"].str.find("Den")

