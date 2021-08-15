import matplotlib.pyplot as plt
import pandas as pd
from numpy import arange, nan
import numpy as np

df = pd.read_csv('data/total_nutrient.csv')
nutrient_total_keys = ['2014 Total Protein (g)','2014 Total Fiber (g)','2014 Total Vitamin A (mg)','2014 Total Vitamin C (g)','2014 Total Vitamin E (g)','2014 Total Calcium (g)','2014 Total Iron (mg)','2014 Total Magnesium (g)','2014 Total Potassium (g)','2014 Total Saturated Fat (g)','2014 Total Sodium (g)']

normalized = {}

true = {}
true_names = []

for nutrient in nutrient_total_keys:
    name = nutrient.replace('2014 Total', '') + ' per 1kL'
    normalized[name] = df[nutrient+'/m3_of_water'] / df[nutrient+'/m3_of_water'].max()
    true[name] = df[nutrient+'/m3_of_water']
    true_names.append(name)


dfn = pd.DataFrame.from_dict(normalized)
dft = pd.DataFrame.from_dict(true)

# dft['Sum of Normalized'] = dfn.sum(axis=1)
# dfn['Sum of Normalized'] = dft['Sum of Normalized'] / dft['Sum of Normalized'].max()
# true_names.append('Sum of Normalized')


# the inner array is the x axis
raw_2d = dfn.to_numpy(dtype=np.float64)
raw_2d_true = dft.to_numpy(dtype=np.float64)

fig, ax = plt.subplots(figsize=[10,10])
im = ax.imshow(raw_2d, aspect='auto', cmap='Blues') #YlGnBu

# We want to show all ticks...
ax.set_xticks(np.arange(len(true_names)))
ax.set_yticks(np.arange(len(df['Crop'])))
# ... and label them with the respective list entries
ax.set_xticklabels(true_names)
ax.set_yticklabels(df['Crop'])

# Rotate the tick labels and set their alignment.
plt.setp(ax.get_xticklabels(), rotation=30, ha="right",
         rotation_mode="anchor")

# Loop over data dimensions and create text annotations.
for i in range(len(df['Crop'])):
    for j in range(len(true_names)):
        true_val = raw_2d_true[i, j]
        norm_val = raw_2d[i,j]
        text = ax.text(j, i, round(true_val, 3),
                       ha="center", va="center", color="grey" if norm_val < 0.5 else "w")



plt.title("Total Nutrient Mass per 1kL of Water Used\nFrom 2014 California Data")
plt.xlabel("Nutrient per 1kL / max(Nutrient per 1kL)\n(Color-scale normalized for each, text shows real)", size=10)

fig.tight_layout()
plt.savefig('figures/wi_heatmap_compare_water_efficiency.png', bbox_inches='tight', dpi=200, transparent=False)
# plt.show()