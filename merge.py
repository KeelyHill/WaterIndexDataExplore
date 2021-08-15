import pandas as pd

df1 = pd.read_csv('data/table1_clean.csv')
df2 = pd.read_csv('data/table2_clean.csv')

mdf = df1.merge(df2, left_on='Crop', right_on='Crop')

# output merge
mdf.to_csv('data/merged.csv', index=False)
mdf.to_json('data/merged.json', orient='split')

# output pivoted merge
p1 = mdf.pivot_table(columns='Crop')
p1.to_json('data/merged_pivot.json', orient='split')



############
# Calculate nutrient/metric per water footprint

per_cubic_meter_keys = ['Protein (g)','Fiber (g)','Vitamin A (μg)','Vitamin C (mg)','Vitamin E (mg)','Calcium (mg)','Iron (mg)','Magnesium (mg)','Potassium (mg)','Saturated Fat (g)','Sodium (mg)','2004-2015 Average Price ($USD/tonne)','2014 Total Value ($USD)','2014 Production (tonnes)']
per_cubic_meter = {}

per_cubic_meter['Crop'] = mdf['Crop']

for key in per_cubic_meter_keys:
    per_cubic_meter[key + "/H2O-print"] = mdf[key] / mdf['1996-2005 Average Water Footprint (cubic meters/tonne)']


per_m3_water = pd.DataFrame.from_dict(per_cubic_meter)
per_m3_water = per_m3_water.pivot_table(columns='Crop')
per_m3_water.to_json('data/merged_water_cubic_meter.json', orient='split')

####################

total_nutrient = {}

total_nutrient['Crop'] = mdf['Crop']
total_nutrient['2014 Water Footprint (cubic meters)'] = mdf['2014 Water Footprint (cubic meters)']
total_nutrient['2014 Total Value ($USD)'] = mdf['2014 Total Value ($USD)']

# for key in per_cubic_meter_keys:
#     total_nutrient[key + '%'] = mdf[key] / sum(mdf[key]) * 100
#     break

# 2014 Production (tonnes)

tonnes_series = mdf['2014 Production (tonnes)']

# Amount of the nutrient per 100g of food.
#   From page 10 of USDA's "Download Field Descriptions"
#   https://fdc.nal.usda.gov/portal-data/external/dataDictionary
# This means (nutrient_g/100g) = ratio of nutrient mass.
# This ratio mutliplied by total mass gives total nutrient mass.

#                                          total tones of crop  | nutrient                 | to g  | to ratio | tonnes to ?g
total_nutrient['2014 Total Protein (g)']       = ( tonnes_series * ( mdf['Protein (g)']       / 1      / 100 ) * 1e6  )
total_nutrient['2014 Total Fiber (g)']         = ( tonnes_series * ( mdf['Fiber (g)']         / 1      / 100 ) * 1e6  )
total_nutrient['2014 Total Vitamin A (mg)']     = ( tonnes_series * ( mdf['Vitamin A (μg)']    / 1e6    / 100 ) * 1e9  )
total_nutrient['2014 Total Vitamin C (g)']     = ( tonnes_series * ( mdf['Vitamin C (mg)']    / 1e3    / 100 ) * 1e6  )
total_nutrient['2014 Total Vitamin E (g)']     = ( tonnes_series * ( mdf['Vitamin E (mg)']    / 1e3    / 100 ) * 1e6  )
total_nutrient['2014 Total Calcium (g)']       = ( tonnes_series * ( mdf['Calcium (mg)']      / 1e3    / 100 ) * 1e6  )
total_nutrient['2014 Total Iron (mg)']          = ( tonnes_series * ( mdf['Iron (mg)']         / 1e3    / 100 ) * 1e9  )
total_nutrient['2014 Total Magnesium (g)']     = ( tonnes_series * ( mdf['Magnesium (mg)']    / 1e3    / 100 ) * 1e6  )
total_nutrient['2014 Total Potassium (g)']     = ( tonnes_series * ( mdf['Potassium (mg)']    / 1e3    / 100 ) * 1e6  )
total_nutrient['2014 Total Saturated Fat (g)'] = ( tonnes_series * ( mdf['Saturated Fat (g)'] / 1      / 100 ) * 1e6  )
total_nutrient['2014 Total Sodium (g)']        = ( tonnes_series * ( mdf['Sodium (mg)']       / 1e3    / 100 ) * 1e6  )


nutrient_total_keys = ['2014 Total Protein (g)','2014 Total Fiber (g)','2014 Total Vitamin A (mg)','2014 Total Vitamin C (g)','2014 Total Vitamin E (g)','2014 Total Calcium (g)','2014 Total Iron (mg)','2014 Total Magnesium (g)','2014 Total Potassium (g)','2014 Total Saturated Fat (g)','2014 Total Sodium (g)']

for metric in nutrient_total_keys:
    total_nutrient[metric + '/m3_of_water'] = total_nutrient[metric] / mdf['2014 Water Footprint (cubic meters)']


total_nutrient = pd.DataFrame.from_dict(total_nutrient)
total_nutrient.to_csv('data/total_nutrient.csv', index=False)
