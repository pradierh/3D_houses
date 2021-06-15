import matplotlib.pyplot as plt


# This function plots the GeoTiff file with dpi, palette and save custom parameters
def render(file, dpi=100, palette="BrBG", save=False):
    fig, ax = plt.subplots(figsize=(10, 10))
    # .read(1) extracts the raster band from .tif file
    dsmplot = ax.imshow(file.read(1), cmap=palette)
    ax.set_title("GeoTiff Plot", fontsize=14)
    cbar = fig.colorbar(dsmplot, fraction=0.035, pad=0.01)
    cbar.ax.get_yaxis().labelpad = 15
    cbar.ax.set_ylabel('Height (m)', rotation=270)
    if save:
        plt.savefig(f"Image at {dpi} dpi.png", dpi=dpi)
    plt.show()

