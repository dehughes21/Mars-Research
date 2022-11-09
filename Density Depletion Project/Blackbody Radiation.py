from BaseFunctions import *
import numpy as np

path = "BlackBody Radiation.xlsx"


def best_fit(X, Y):
    xbar = sum(X) / len(X)
    ybar = sum(Y) / len(Y)
    n = len(X)  # or len(Y)

    numer = sum([xi * yi for xi, yi in zip(X, Y)]) - n * xbar * ybar
    denum = sum([xi ** 2 for xi in X]) - n * xbar ** 2

    b = numer / denum
    a = ybar - b * xbar

    print('best fit line:\ny = {:.2f} + {:.2f}x'.format(a, b))

    return a, b


def Power(dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    temps = columnData(dataPath, sheet, 'A')
    tempFourth = []
    for val in temps:
        fourth = val ** 4
        tempFourth.append(fourth)

    peakW = columnData(dataPath, sheet, 'C')
    power = columnData(dataPath, sheet, 'D')
    a, b = best_fit(tempFourth, power)
    yfit = [a + b * xi for xi in tempFourth]
    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax.set_xlabel("Temperature ($K^4$)")
    ax.set_ylabel("Power (rel*nm)")
    ax.scatter(tempFourth, power)
    ax.plot(tempFourth, yfit)
    ax.text(0.8*(10**14), 275, "P = (2 x 10$^-$$^1$$^2$)kT$^4$ - 59.637   R$^2$ = 0.9423", fontsize=15)
    plt.savefig("power" + ".pdf")


def wien(dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"

    temps = columnData(dataPath, sheet, 'A')

    peakW = columnData(dataPath, sheet, 'C')

    tempInv = []
    for val in temps:
        tempInv.append(1 / val)

    a, b = best_fit(tempInv, peakW)
    yfit = [a + b * xi for xi in tempInv]

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax.set_xlabel("Temperature ($K^-$$^1$)")
    ax.set_ylabel("Peak Wavelength (nm)")
    ax.scatter(tempInv, peakW)
    ax.plot(tempInv, yfit)
    ax.text(0.00026, 705, "\u03BB = 369.79 + 978636.37$T^-$$^1$    $R^2$ = 0.8787 ", fontsize=15)
    plt.savefig("wien" + ".pdf")

Power(path)
#wien(path)
