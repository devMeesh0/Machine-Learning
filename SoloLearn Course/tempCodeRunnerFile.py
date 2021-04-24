import numpy as np
import pandas as pd

df = pd.read_csv('https://sololearn.com/uploads/files/titanic.csv')

df['male'] = df['Sex'] == 'male'

small_df = df[['Age',  'Sex', 'Survived', 'male']]
print(small_df.head())