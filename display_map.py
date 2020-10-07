import matplotlib.pyplot as plt

import cartopy.crs as ccrs                   # import projections
import cartopy.feature as cf                 # import features
ax = plt.axes(projection = ccrs.EqualEarth())  # create a set of axes with Mercator projection
ax.add_feature(cf.COASTLINE)                 # plot some data on them
ax.add_feature(cf.BORDERS)
ax.set_title("Title")                        # label it
plt.show()
