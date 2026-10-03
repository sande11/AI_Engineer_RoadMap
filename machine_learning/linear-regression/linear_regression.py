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

plt.scatter(cdf.FUELCONSUMPTION_COMB, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("FUELCONSUMPTION_COMB")
plt.ylabel("Emission")
plt.show()


plt.scatter(cdf.ENGINESIZE, cdf.CO2EMISSIONS, color='blue')
plt.xlabel("Engine size")
plt.ylabel("Emission")
plt.xlim(0, 27)
plt.show()

# Create train and test datasets
