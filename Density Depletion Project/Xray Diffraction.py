from BaseFunctions import *
import numpy as np
import matplotlib.ticker as plticker

path = "sodium x-ray diffraction.xlsx"


def lambdaVintensity(dataPath):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    sheet = "Sheet1"
    wavelengths = []

    deg = columnData(dataPath, sheet, 'A')
    for i in range(len(deg)):
        wavelength = 2 * 0.282 * math.sin(math.radians(deg[i] / 2))
        wavelengths.append(wavelength)
    intensity = columnData(dataPath, sheet, 'B')

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    x = np.linspace(5, 8.5, 100)
    y = 0.4186 * x - 1.8182

    ax.set_xlabel("Wavelength, nm")
    ax.set_ylabel("Counting Rate, cps")
    ax.plot(wavelengths, intensity)
   #plt.savefig("diffrac" + ".pdf")

    print(max(intensity))
    print(intensity.index(max(intensity)))
    print(wavelengths[160])

    intensity.remove(intensity.index(max(intensity)))
    wavelengths.remove(wavelengths[160])

    print(max(intensity))
    print(intensity.index(max(intensity)))


lambdaVintensity(path)
