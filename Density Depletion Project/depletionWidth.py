from BaseFunctions import *


def widthVsSZA(dataPath):
    height = int(input("Figure height: "))
    width = int(input("Figure width: "))

    sName = 'final list'
    Rm = 3389.5
    lat1 = columnData(dataPath, sName, "F")
    lat2 = columnData(dataPath, sName, "R")

    long1 = columnData(dataPath, sName, "G")
    long2 = columnData(dataPath, sName, "S")

    locs1 = []
    locs2 = []
    for i in range(len(long1)):
        locs1.append((long1, lat1))
        locs2.append((long2, lat2))

    alt1 = columnData(dataPath, sName, "E")
    alt2 = columnData(dataPath, sName, "Q")

    sza1 = columnData(dataPath, sName, "D")
    sza2 = columnData(dataPath, sName, "P")

    widths = []
    SZAs = []
    avgSZA = []

    for i in range(len(lat1)):
        altChange = abs(float(alt2[i]) + Rm - float(alt1[i]))
        latChange = abs(float(lat2[i]) + Rm - float(lat1[i]))
        avgSZA.append((float(sza1[i])) + float((sza2[i]))/2)
        width = (abs(latChange ** 2 - altChange ** 2)) ** (1 / 2)
        widths.append(width)

    avgWidth = sum(widths) / len(widths)

    fig, (ax) = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    ax.scatter(avgSZA, widths)

    fig.savefig("test1")

    print(max(widths))
    print(min(widths))


widthVsSZA("best_depletions.xlsx")
