from matplotlib import pyplot as plt
import numpy as np
import matplotlib.patches as mpatches
x_labels=[2006,2007,2008,2009,2010]
chattisgarh=[2694,3222,3346,3863,3887,4003]
goa=[1301,1488,1816,1896,1899,2237]
gujarat=[5912,7116,6854,7351,7043,6770]
haryana=[1148,1322,1255,1255,1180,1172]
plt.plot(chattisgarh,color='green')
plt.plot(goa,color='red')
plt.plot(gujarat,color='orange')
plt.plot(haryana,color='purple')
plt.title('number of road accidents')
plt.xlabel('years')
plt.ylabel('number of road accidents')

green_patch=mpatches.Patch(color='green',label='chattisgarh')
red_patch=mpatches.Patch(color='red',label='goa')
orange_patch=mpatches.Patch(color='orange',label='gujarat')
purple_patch=mpatches.Patch(color='purple',label='haryana')
plt.legend(handles=[green_patch,red_patch,orange_patch,purple_patch])