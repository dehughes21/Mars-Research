from BaseFunctions import *


def plot_magData_individual(magData, dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "final list"
    orbit = int(input("Orbit number: "))

    orbits = columnData(dataPath, sheet, 'A')

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

    plotLats_s = []
    plotLongs_s = []
    plotLats_e = []
    plotLongs_e = []

    pathLongs = []
    pathLats = []

    i = 0
    for orb in orbits:
        if orb == orbit:
            plotLats_s.append(startlats[i])
            plotLongs_s.append(startElongs[i])
            plotLats_e.append(endlats[i])
            plotLongs_e.append(endElongs[i])

            pathLongs.append(startElongs[i])
            pathLongs.append(endElongs[i])
            pathLats.append(startlats[i])
            pathLats.append(endlats[i])
        i += 1

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
    ax.set_title(orbit)
    ax.set_xlim([0, 359])
    ax.scatter(plotLongs_s, plotLats_s, c='g', marker='o', edgecolor='#000000', zorder=1, label='Depletions')
    ax.scatter(plotLongs_e, plotLats_e, c='r', marker='o', edgecolor='#000000', zorder=1, label='Depletions')
    color = next(ax._get_lines.prop_cycler)['color']
    ax.plot(pathLongs, pathLats, linestyle='-', color=color)
    fig.savefig(str(orbit) + "tracjectory.png")


path = 'best_depletions.xlsx'

magField, magFieldR, magFieldV, magFieldLog, magLocs = MagData_Morsch()

active = 'yes'

while active == 'yes':

    magChoice = eval(input("Magnetic Field Data Choice: Choose 'magField', 'magFieldR', 'magFieldV', or 'magFieldLog' "))

    plot_magData_individual(magChoice, path)

    active = input("Plot another orbit? Choose 'yes' or 'no': ")
    if active == 'no':
        print("Program stopped")
