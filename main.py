import rasterio
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import BoundaryNorm, LinearSegmentedColormap

mars = rasterio.open('/Users/caleb/Documents/QGIS STUFF/Mars_MGS_MOLA_DEM_mosaic_global_463m.tif')
mars = mars.read()

print(mars.shape)
print(np.amin(mars[0]))
print(np.amax(mars[0]))
print(np.amax(mars[0]) + abs(np.amin(mars[0])))

custom_cmap = LinearSegmentedColormap.from_list('mars', ['#162252',
                                                         '#104E8B',
                                                         '#00B2EE',
                                                         '#00FF00',
                                                         '#FFFF00',
                                                         '#FFA500',
                                                         '#FF0000',
                                                         '#8b0000',
                                                         '#964B00',
                                                         '#808080',
                                                         '#FFFFFF'], N=2221)

bounds = np.arange(-8210, 14000, 10)
norm = BoundaryNorm(bounds, custom_cmap.N)


def label_features(ax):
    ax.text(5000, 8400, "Olympus\n Mons")
    ax.text(7000, 10000, "Ascreaus\n Mons")
    ax.text(6200, 11500, "Pavonis\n Mons")
    ax.text(5000, 13000, "Arsia\n Mons")
    ax.text(8500, 13000, "Tharsis", rotation=45)
    ax.text(12000, 14000, "Vallies\n Marineris")
    ax.text(17000, 18000, "Argyre")
    ax.text(20000, 2000, "Vastitas Borealis")
    ax.text(17000, 8500, "Chryse\n Planitia")
    ax.text(20000, 5000, "Acidalia Planitia")
    ax.text(30000, 16500, "Hellas", color='white')
    ax.text(37000, 5000, "Utopia\n Planitia")
    ax.text(41000, 8000, "Elysium")
    ax.text(34000, 9800, "Isidis")
    ax.text(7000, 5000, "Alba Patera")
    ax.text(2000, 6500, "Amazonis\n Planitia")

    return ax

fig, ax = plt.subplots()
fig.set_size_inches(14, 7)

ax.imshow(mars[0], cmap=custom_cmap, norm=norm)
ax = label_features(ax)
ax.axis('off')
newax = fig.add_axes([0.82, 0.13, 0.08, 0.08], anchor='NE')
newax.axis('off')
txt = ax.text(0.0, 0.02, "Martian Topography \n@PythonMaps",
              size=4,
              color='white',
              transform=ax.transAxes)
plt.show()
