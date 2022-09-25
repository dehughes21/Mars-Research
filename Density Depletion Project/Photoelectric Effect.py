from BaseFunctions import *
import numpy as np
import matplotlib.ticker as plticker

path = "Photoelectric Effect.xlsx"


def photoPlot(dataPath):
    title = input("Plot Title: ")
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    freq = columnData(dataPath, sheet, 'B')
    voltage = columnData(dataPath, sheet, 'C')

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    x = np.linspace(5, 8.5, 100)
    y = 0.4186 * x - 1.8182

    ax.set_xlabel("Frequency (10^14 Hz)")
    ax.set_ylabel("Stopping Potential (V)")
    ax.set_title(title)
    ax.plot(x, y)
    ax.scatter(freq, voltage, s=30, c='r')
    plt.savefig(title + ".pdf")


photoPlot(path)


def constW(dataPath):
    title = input("Plot Title: ")
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    v1, v2, v3 = columnData(dataPath, sheet, 'E'), columnData(dataPath, sheet, 'H'), columnData(dataPath, sheet, 'K')
    c1, c2, c3 = columnData(dataPath, sheet, 'F'), columnData(dataPath, sheet, 'I'), columnData(dataPath, sheet, 'L')

    v2c = [float(i) for i in v2]
    v3c = [float(i) for i in v3]

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    ax.set_xlabel("Stopping Potential (V)")
    ax.set_ylabel("Current (A)")
    ax.set_title(title)
    ax.plot(v1, c1)
    ax.plot(v2, c2)
    ax.plot(v3, c3)
    start, end = ax.get_xlim()
    ax.xaxis.set_ticks(np.arange(start, end, 2))
    plt.savefig(title + ".pdf")





def constI(dataPath):
    title = input("Plot Title: ")
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    v1, v2, v3 = columnData(dataPath, sheet, 'N'), columnData(dataPath, sheet, 'Q'), columnData(dataPath, sheet, 'T')
    c1, c2, c3 = columnData(dataPath, sheet, 'O'), columnData(dataPath, sheet, 'R'), columnData(dataPath, sheet, 'U')

    v2c = [float(i) for i in v2]
    v3c = [float(i) for i in v3]

    fig, ax = plt.subplots()
    fig.set_figheight(height)
    fig.set_figwidth(width)

    ax.set_xlabel("Stopping Potential (V)")
    ax.set_ylabel("Current (A)")
    ax.set_title(title)
    ax.plot(v1, c1)
    ax.plot(v2, c2)
    ax.plot(v3, c3)
    plt.xticks(np.arange(-5, 40, 5))
    plt.yticks(np.arange(0, 700, 100))

    plt.savefig(title + ".pdf")



