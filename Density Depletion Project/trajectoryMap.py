from BaseFunctions import *


def plot_magData_trajectories(magData, dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    title = input("Plot title: ")
    sheet = "final list"

    startlats = columnData(dataPath, sheet, 'F')
    startWlongs = columnData(dataPath, sheet, 'G')

    endlats = columnData(dataPath, sheet, 'R')
    endWlongs = columnData(dataPath, sheet, 'S')

    startElongs = []
    endElongs = []

    for val in startWlongs:
        starteLong = 360 - val
        startElongs.append(starteLong)

    for val in endWlongs:
        endeLong = 360 - val
        endElongs.append(endeLong)

    x = np.aramge(-0.5, 359, 1)
    y = np.arange(-90.5, 89, 1)
    magDir = np.array(magData)

    z = np.reshape(magDir, (359,179))
    z = np.transpose(z)
    levels = MaxNLocator(nbins=15).tick_values(z.min(),z.max())

    cmap = plt.get_cmap('coolwarm')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    fig, (ax) = plt.subplots(nrows=1)

    fig.set_figheight(height)
    fig.set_figwidth(width)

    im = ax.pcolormesh(x, y, z, cmap=cmap, norm=norm, zorder = -1)
    fig.colorbar(im, ax=ax)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(title)
    ax.set_xlim([0,359])
    ax.set_ylim([-90,86])
    ax.scatter(startElongs)


