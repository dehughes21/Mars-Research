from BaseFunctions import *
import numpy as np

path = "BlackBody Radiation.xlsx"


def Power(dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    temps = columnData(dataPath, sheet, 'A')
    tempFourth = []
    for val in temps:
        fourth = val ** 4
        tempFourth.append(val)

    peakW = columnData(dataPath, sheet, 'C')
    power = columnData(dataPath, sheet, 'D')

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax.set_xlabel("Temperature ($K^4$)")
    ax.set_ylabel("Power (rel*nm)")
    ax.plot(tempFourth, power)
    plt.savefig("power" + ".pdf")


def wien(dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    temps = columnData(dataPath, sheet, 'A')

    peakW = columnData(dataPath, sheet, 'C')

    tempInv = []
    for val in temps:
        tempInv.append(1/val)

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax.set_xlabel("Temperature ($K^-$$^1$)")
    ax.set_ylabel("Peak Wavelength (nm)")
    ax.plot(tempInv, peakW)
    plt.savefig("wien" + ".pdf")


Power(path)
wien(path)
