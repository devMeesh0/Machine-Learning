import numpy as np
import pandas as pd

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

df['male'] = df['Sex'] == 'male'

# create a smaller data frame of collumns from the original one
small_df = df[['Age',  'Sex', 'Survived', 'male']]

# return numpy array of the values of certain columns within the dataframe
arr = df[['Pclass', 'Fare', 'Age']].values

mask = arr[:,2] < 18 # makes array "mask" which contains boolean values 
                     # dependant on whether the values of the array are less than 18 or not

print(arr[mask]) # prints the True values, in this case all the ones under 18 (can be done with print(arr[:,2 < 18]))

print(arr.shape) # prints array dimensions (887, 3)

print(arr[0,1]) # prints single element from numpy array
print(arr[0])   # prints single row from numpy array
print(arr[:,2]) # prints single column from numpy array