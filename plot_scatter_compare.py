import matplotlib.pyplot as plt
import pandas as pd
from numpy import arange, nan

df = pd.read_csv('data/total_nutrient.csv')
nutrient_total_keys = ['2014 Total Protein (Kg)','2014 Total Fiber (Kg)','2014 Total Vitamin A (mg)','2014 Total Vitamin C (g)','2014 Total Vitamin E (g)','2014 Total Calcium (g)','2014 Total Iron (g)','2014 Total Magnesium (g)','2014 Total Potassium (g)','2014 Total Saturated Fat (Kg)','2014 Total Sodium (g)']

normalized = { 'Crop': df['Crop']}
normalized_names = []

for nutrient in nutrient_total_keys:
    name = nutrient.replace('2014 Total', '').replace('(Kg)', '').replace('(g)', '').replace('(mg)', '')
    normalized_names.append(name)
    normalized[name] = df[nutrient+'/m3_of_water'] / df[nutrient+'/m3_of_water'].max()

dfn = pd.DataFrame.from_dict(normalized)

fig, ax = plt.subplots(figsize=(10, 8))

for i, nut in enumerate(normalized_names):
    data = dfn[nut].to_numpy()
    data[data == 0] = nan

    ax.scatter(data, df['Crop'], 
                    # alpha=0.5,
                    # s = 1,
                    label=nut)

ax.invert_yaxis() 

fig.subplots_adjust(right=0.75)   


plt.title("Normalized 2014 Nutrient per Cubic Meter of Water")
plt.xlabel("Nutrient per 1kL / max(Nutrient per 1kL)", size=14)

plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')

# fig.tight_layout() 
plt.savefig('figures/scatter_compare_water_efficiency.png', bbox_inches='tight', dpi=200, transparent=False)
# plt.show()