import pandas as pd
import matplotlib.pyplot as plt 
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
print(df.columns)
df_model = df2[['Location', 'Price', 'Style', 'Bedrooms', 'Bathrooms', 'Size(sqft)', 'Den']]

#Get dummy data
df_dum = pd.get_dummies(df_model, dtype = int)

#Train test split
from sklearn.model_selection import train_test_split

X = df_dum.drop('Price', axis =1)
y = df_dum.Price.values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Multiple linear regression
import statsmodels.api as sm

X_sm = X 

X = sm.add_constant(X)
model = sm.OLS(y,X_sm)
model.fit().summary()

from sklearn.linear_model import LinearRegression, Lasso
from sklearn.model_selection import cross_val_score

lm = LinearRegression()
lm.fit(X_train, y_train)

np.mean(cross_val_score(lm, X_train, y_train, scoring = 'neg_mean_absolute_error'))

#Lasso regression
lm_l = Lasso()
np.mean(cross_val_score(lm_l, X_train, y_train, scoring = "neg_mean_absolute_error", cv = 3))

alpha = []
error = []

for i in range(1, 100):
    alpha.append(i/10)
    lml = Lasso(alpha=(i/100))
    error.append(np.mean(cross_val_score(lml, X_train, y_train, scoring = "neg_mean_asbolute_error", cv = 3)))

plt.plot(alpha,error)
#Random Forest
#Tune models
#Test Ensembles

