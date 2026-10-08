import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import truststore
truststore.inject_into_ssl()


url= "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(url)

# verify successful load with some randomly selected records
# to show all columns use the command below before any print statement
# pd.set_option("display.max_columns", None) 
# print(df.sample(5))
print(df.describe())

cdf = df[['ENGINESIZE', 'CYLINDERS', 'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
print(cdf.sample(9))

viz = cdf[['CYLINDERS', 'ENGINESIZE',  'FUELCONSUMPTION_COMB', 'CO2EMISSIONS']]
# viz.hist()
# plt.show()

# As you can see, most engines have 4, 6, or 8 cylinders, and engine sizes between 2 and 4 liters.
# As you might expect, combined fuel consumption and CO2 emission have very similar distributions.
# Go ahead and display some scatter plots of these features against the CO2 emissions, to see how linear their relationships are.

# plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("FUELCONSUMPTION_COMB")
# plt.ylabel("Emission")
# plt.show()


# plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
# plt.xlabel("Engine size")
# plt.ylabel("Emission")
# plt.xlim(0, 27)
# plt.show()

# Create train and test datasets
# extracting input feature and labels of the dataset

x = cdf.ENGINESIZE.to_numpy()
y = cdf.CO2EMISSIONS.to_numpy()

# Next, you will split the dataset into mutually exclusive training and testing sets. You will train a simple linear regression model 
# on the training set and estimate its ability to generalize to unseen data by using it to make predictions on the unseen testing data.
#  testing sizes range from 20% to 30%. The smaller your data, the larger your training set needs to be because it's easier to find 
# spurious patterns in smaller data. The downside is that your evaluation of generalizability will have less reliability. Bigger is better when it comes to data.

from sklearn.model_selection import train_test_split
from sklearn import linear_model

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
type(x_train), np.shape(x_train), np.shape(x_train)

# create a model object
regressor = linear_model.LinearRegression()

# train the model on the training data
# X_train is a 1-D array but sklearn models expect a 2D array as input for the training data, with shape (n_observations, n_features).
# So we need to reshape it. We can let it infer the number of observations using '-1'.
regressor.fit(x_train.reshape(-1, 1), y_train)
print('Coefficient: ', regressor.coef_[0])
print('Intercept', regressor.intercept_)

plt.scatter(x_train, y_train, color='blue')
plt.plot(x_train, regressor.coef_ * x_train + regressor.intercept_, '-r')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.show()