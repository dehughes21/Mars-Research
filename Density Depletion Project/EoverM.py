from BaseFunctions import *
import numpy as np
import matplotlib.ticker as plticker

path = "EoverM.xlsb.xlsx"


def currentANDradius(dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    c1 = columnData(dataPath, sheet, 'B')
    c2 = columnData(dataPath, sheet, 'C')
    c3 = columnData(dataPath, sheet, 'D')

    c1inv = []
    c2inv = []
    c3inv = []
    rInv = []

    distance = columnData(dataPath, sheet, 'A')

    for val in c1:
        inv = 1 / (val ** 2)
        c1inv.append(inv)
    for val in c2:
        inv = 1 / (val ** 2)
        c2inv.append(inv)
    for val in c3:
        inv = 1 / (val ** 2)
        c3inv.append(inv)

    for val in distance:
        inv = (val ** 2)
        rInv.append(inv)

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    x1 = np.linspace(5, 8.5, 100)
    y = 128.87 * x1 + 0.0157

    ax.set_xlabel("$r^2$ (m)")
    ax.set_ylabel("1/$I^2$ (A)")
    ax.plot(rInv, c1inv, label='23.03 V')
    ax.plot(rInv, c2inv, label='24.91 V')
    ax.plot(rInv, c3inv, label='28.1 V')
    ax.legend()
    plt.savefig("currentTest" + ".pdf")


currentANDradius(path)
