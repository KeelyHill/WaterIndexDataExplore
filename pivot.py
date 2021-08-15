import pandas as pd

df1 = pd.read_csv('data/table1_clean.csv')
df2 = pd.read_csv('data/table2_clean.csv')


p1 = df1.pivot_table(columns='Crop')
p1.to_csv('data/table1_pivot.csv')

p2 = df2.pivot_table(columns='Crop')
p2.to_csv('data/table2_pivot.csv')

