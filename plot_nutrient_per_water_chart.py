import matplotlib.pyplot as plt
import pandas as pd
from numpy import arange

WIDTH = 0.9       # the width of the bars: can also be len(x) sequence

df = pd.read_csv('data/total_nutrient.csv')
nutrient_total_keys = ['2014 Total Protein (g)','2014 Total Fiber (g)','2014 Total Vitamin A (mg)','2014 Total Vitamin C (g)','2014 Total Vitamin E (g)','2014 Total Calcium (g)','2014 Total Iron (mg)','2014 Total Magnesium (g)','2014 Total Potassium (g)','2014 Total Saturated Fat (g)','2014 Total Sodium (g)']


fig, axs = plt.subplots(3, 4, figsize=(20, 31)) # facecolor='w', edgecolor='k'
# fig.subplots_adjust(hspace = 0.1, wspace=.3)
axs = axs.ravel()

crops = df['Crop']
for i, metric in enumerate(nutrient_total_keys):
    ax = axs[i]
    nut = df[metric + '/m3_of_water'] 
    name = metric+' per 1kL'
    ax.barh(crops, nut, WIDTH, label=name)
    ax.set_title(name, fontsize=10)
    ax.invert_yaxis() 
    ax.set_yticks(arange(len(crops)))
    ax.set_yticklabels(crops)
    for spine in ['top', 'right']:
        ax.spines[spine].set_visible(False)



axs[-1].set_yticks(arange(1))
axs[-1].set_yticklabels('')
axs[-1].set_xticklabels('')

# plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
# plt.show()
plt.savefig('figures/wi_nutrient_per_water.png', bbox_inches='tight', dpi=200, transparent=False)
