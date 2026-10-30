import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import truststore
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression 
from sklearn.metrics import(
    mean_absolute_error,
    mean_squared_error,
    r2_score
) #for evaluating mode

truststore.inject_into_ssl

url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-ML0101EN-SkillsNetwork/labs/Module%202/data/FuelConsumptionCo2.csv"
df = pd.read_csv(url)

# print(df.describe())

# select the features
x = df[
    [
        'ENGINESIZE',
        'CYLINDERS',
        'FUELCONSUMPTION_COMB',
    ]
]

y= df['CO2EMISSIONS']

# print(x.head())
# print(y.head())

# x.shape returns a tuple describing the dimensions of the feature matrix.
# For x with n samples and 3 features, it returns (n, 3):
#
#                 features
#              ┌──────────────────────────────┐
# samples      │ x₁₁  x₁₂  x₁₃                │
#              │ x₂₁  x₂₂  x₂₃                │
#              │  ⋮    ⋮    ⋮                  │
#              │ xₙ₁  xₙ₂  xₙ₃                 │
#              └──────────────────────────────┘
#
# Checking the shape is necessary in ML to confirm that the data has the
# expected number of samples and features before training a model, preventing
# dimension mismatches and helping ensure that X and y align correctly.
# print(x.shape)

# the output
# #                Features
#              ↓        ↓        ↓
#              Engine Cylinders Fuel
# Car 1         2.0      4      8.5
# Car 2         2.4      4      9.6
# Car 3         3.5      6     11.0
# Car 4         5.0      8     14.0


x_train, x_test, y_train, y_test = train_test_split(
    x,
    y,
    test_size=0.2,
    random_state=42
)

# create the model
model = LinearRegression()
# train the model
model.fit(x_train, y_train)

# to see what the model learned:
# -intercept
# print(model.intercept_)
# -coefficients
# print(model.coef_)

# the result is model.intercept_ = 67.348...
# the model.coef_ = [11.2094395   7.15561381  9.5208118 ]
# model.coef_[0] corresponds to ENGINESIZE, model.coef_[1] corresponds to CYLINDERS and model.coef_[2] corresponds to FUELCONSUMPTION_COMB
# the order matters, to make that explicit use: 

# for feature, coefficient in zip(X.columns, model.coef_):
    # print(feature, coefficient)

# generate a prediction on the test data we kept aside (20%)

y_pred = model.predict(x_test)
# print("prediction:", y_pred)

# evaluate the model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("MAE", mae)
print("RMSE", rmse)
print("R", r2)

# if MAE is 16 for example it means the models prediction are off by about 10g/km on average in absolute terms
# RMSE penalizes large errors more strongly
# suppose its 0.87, this means the models explains about 85% of the variation in the target relative to a mean-prediction baseline
# on the evaluated data. dont intepret it as 85% accurate