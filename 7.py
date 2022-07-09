from operator import index
import numpy as np
import pandas as pd
from datetime import datetime, date
import seaborn as sns
import matplotlib.pyplot as plt
# pd.options.display.max_rows = 999
data = pd.read_excel('Employee_Data.xls')
# print(data)
# print(data.head(10))
# print(data.tail(10))
# print(data.shape)
# print(data.info())
# print(data.describe())
# print(data.corr())
# print(data.isnull().sum())
# data.fillna(method='bfill',inplace=True)
# print(data.isnull().sum())
avg_sal=data['salary'].mean()
# print("Average salary = ",avg_sal)

# salary of male employees below the average salary
# msd = data.loc[(data['gender']=='m')&(data['salary']<avg_sal)].value_counts()
# print(msd)

# salary of female employees below the average salary
# fsd = data.loc[(data['gender']=='f')&(data['salary']<avg_sal)].value_counts()
# print(fsd)

# how many male employees earn equal of more than average salary
# msd = data.loc[(data['gender']=='m')&(data['salary']>=avg_sal)].value_counts()
# print(msd)
# print("Total {} Male candidate have equal or more than {} of average salary".format(len(msd),avg_sal))

# how many female employees earn equal of more than average salary
# fsd = data.loc[(data['gender']=='f')&(data['salary']>=avg_sal)].value_counts()
# print(fsd)
# print("Total {} Female candidate have equal or more than {} of average salary".format(len(fsd),avg_sal))

# Gender distribution
# print(data['gender'].value_counts())

# Average salary by gender
# g_s = data.groupby(['gender'],as_index = False).salary.mean()
# print(g_s)

# Create a new column of age 
# To find unique birth year
# year = pd.DatetimeIndex(data['bdate']).year
# print(year.unique())

# current_date = date.today()
# print(current_date)

# current_year = current_date.year
# print(current_year)

# data["age"] = current_year - year
# print(data.head(10))

# Salary analysis by job category
print(data['jobcat'].value_counts())

# Average Salary By Job Category
JD = data.groupby(['jobcat'],as_index = False).salary.mean()
print(JD)

# Data Visualization
dv =sns.barplot(x='jobcat',y='salary',data=JD)
plt.show()


# sns.countplot(x='gender',data=data,palette="Set3")
# plt.show()