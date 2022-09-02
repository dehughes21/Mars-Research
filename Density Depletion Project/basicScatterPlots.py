from BaseFunctions import *


def avg_Alts(alt, sza):
    bins = np.array([0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
                     150, 160, 170])
    A = np.vstack((np.digitize(sza, bins), alt)).T
    res = [np.mean(A[A[:, 0] == i, 1]) for i in np.unique(A[:, 0])]
    return res


def getPDF(altData, alts, szas):
    height = int(input("Figure height: "))
    width = int(input("Figure width: "))

    szaBins = [15, 25, 35, 45, 55, 65, 75, 85, 95, 105, 115, 125, 135, 145, 155, 165]

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    ax.scatter(szas, alts, s=30, c='r', marker='o', edgecolor='#000000',
               zorder=1, label='Depletions')
    ax.scatter(szaBins, altData, s=100, c='g', marker='o', edgecolor='#000000',
               zorder=1, label='Depletions')
    ax.set_xlabel("Solar Zenith Angle (degrees)")
    ax.set_ylabel("Altitude (km)")
    ax.set_title("SZA vs. Altitude")

    plt.savefig("SZA vs Alt (All Data, Binned Averages).pdf")


pathG = 'best_depletions.xlsx'
sheet = 'final list'

szasG = columnData(pathG, sheet, "D")
altsG = columnData(pathG, sheet, "E")

aAlts = avg_Alts(altsG, szasG)
getPDF(aAlts, altsG, szasG)