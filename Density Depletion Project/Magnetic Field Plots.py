from BaseFunctions import *


def plot_magData_scatter(magData, dataPath):
    title = input("Plot Title: ")
    position = input("Enter 'start', 'mid', or 'end' for desired data points: ")
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "final list"

    if position == "start":
        lats = columnData(dataPath, sheet, 'F')
        Wlongs = columnData(dataPath, sheet, 'G')

    elif position == "mid":
        lats = columnData(dataPath, sheet, 'L')
        Wlongs = columnData(dataPath, sheet, 'M')

    elif position == "end":
        lats = columnData(dataPath, sheet, 'R')
        Wlongs = columnData(dataPath, sheet, 'S')

    Elongs = []
    for val in Wlongs:
        eLong = 360 - val
        Elongs.append(eLong)

    x = np.arange(-0.5, 359, 1)
    y = np.arange(-90.5, 89, 1)
    magDir = np.array(magData)

    zInc = np.reshape(magDir, (359, 179))
    zInc = np.transpose(zInc)

    levels = MaxNLocator(nbins=15).tick_values(zInc.min(), zInc.max())

    cmap = plt.get_cmap('coolwarm')
    norm = BoundaryNorm(levels, ncolors=cmap.N, clip=True)

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    im = ax.pcolormesh(x, y, zInc, cmap=cmap, norm=norm, zorder=-1)
    fig.colorbar(im, ax=ax)
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.set_title(title)
    ax.set_xlim([0, 359])
    ax.scatter(Elongs, lats, c='r', marker='o', edgecolor='#000000', zorder=1, label='Depletions')
    fig.savefig("test.png")


path = 'C:/Users/dehug/PycharmProjects/Mars-Research/Density Depletion Project/best_depletions.xlsx'

magField, magFieldR, magFieldV, magFieldLog, magLocs = MagData_Morsch()

plot_magData_scatter(magFieldV, path)