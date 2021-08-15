import tabula
import pandas as pd

# pdf_path = "http://ars.els-cdn.com/content/image/1-s2.0-S1470160X17308592-mmc1.pdf"
# pdf_path = "./Water-Indexed Benefits and Impacts of California Almond.pdf"
pdf_path = "./truncated-Water-Indexed Benefits and Impacts of California Almond.pdf"

# Table 1
print('Table 1...')
df = tabula.read_pdf(pdf_path, pages='1,2', multiple_tables=False, pandas_options={'header': None}, user_agent='Mozilla/5.0')[0]
headers = list(df.loc[0:2].fillna('').apply(' '.join).str.strip())
df.loc[43][0] = 'Sweet Potatoes'
df.drop([42,44], inplace=True) 

df.drop(df.head(3).index, inplace=True)
df.to_csv("data/table1_raw.csv", header=headers, index=False)

# Table 2
print('Table 2...')
df = tabula.read_pdf(pdf_path, pages='3,4', multiple_tables=False, pandas_options={'header': None}, user_agent='Mozilla/5.0')[0]
headers = list(df.loc[0:1].fillna('').apply(' '.join).str.strip())
headers = ['Crop', '2004-2015 Average Price ($USD/tonne)', '2004-2015 Average Price (rank)', '2014 Total Value ($USD)', '2014 Production (tonnes)', '2014 Water Footprint (cubic meters)', '2014 Value: Water Footprint Ratio', '1996-2005 Average Water Footprint (cubic meters/tonne)', 'Water Footprint Rank']
df.drop(df.head(2).index, inplace=True)
df.to_csv("data/table2_raw.csv", header=headers, index=False)

print('Extraction done!')