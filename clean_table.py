import pandas as pd
import re

df1 = pd.read_csv('data/table1_raw.csv')
df2 = pd.read_csv('data/table2_raw.csv')

def extract_rank(df, key='[rank]'):
    new_dict = {}
    for col in df:
        if key in col:
            header_sans_rank = col.replace(key, '').strip()
            no_unit = re.sub(r'\(.\)',  '', header_sans_rank).strip()

            actual = df[col].str.extract('((\d|\.)(.*?)(?=\[))')[0].str.strip()
            rank = df[col].str.extract('((?<=\[)((\d|\.)*)(?=\]))')[0].str.strip()
        
            new_dict[header_sans_rank] = actual.str.replace(',', '')
            new_dict[no_unit + ' Rank'] = rank.str.replace(',', '')
        else:
            new_dict[col] = df[col]

    return pd.DataFrame.from_dict(new_dict)

t1 = extract_rank(df1)
t1.to_csv('data/table1_clean.csv', index=False)

for col in df2:
    df2[col] = df2[col].astype(str).str.replace('$', '', regex=False).str.replace(',', '', regex=False) #extract_rank(df2)

t2 = df2
t2.to_csv('data/table2_clean.csv', index=False)
