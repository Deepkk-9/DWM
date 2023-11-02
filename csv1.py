import pandas as pd

data = pd.read_csv('missingValues.csv')
print(data)

null_age = data['Age'].isnull().sum()
null_salary = data['Salary'].isnull().sum()
print('\nNumber of Missing Values in Age Column: ', null_age)
print('Number of Missing Values in Salary Column: ', null_salary)
print('\n\t\t\t==========Handling Missing Values==========\n')



print('1. Dropping Rows:')
data.dropna(axis=0, inplace=True)
print(data.head())

print('\n2. Filling with Specific Value:')
data = pd.read_csv('missingValues.csv')
data.fillna(0, inplace=True)
print(data.head())

print('\n3. Imputing with Mean:')
data = pd.read_csv('missingValues.csv')
mean = data['Age'].mean()
data['Age'].fillna(mean, inplace=True)
mean = data['Salary'].mean()
data['Salary'].fillna(mean, inplace=True)
print(data.head())
