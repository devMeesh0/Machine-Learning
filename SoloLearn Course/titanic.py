import numpy as np
import pandas as pd

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

small_df = df[['Age',  'Sex', 'Survived']]
print(small_df.head())