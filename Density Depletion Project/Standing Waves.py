from BaseFunctions import *

dataPath = "Standing Waves.xlsx"


def polarPlot(path):
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))

    sheet = "Sheet1"
    amp = columnData(path, sheet, "R")
    theta = []
    for i in range(len(amp)):
        theta.append(i * 10)

    fig, ax = plt.subplots(subplot_kw={'projection': 'polar'})
    fig.set_figheight(height)
    fig.set_figwidth(width)
    ax.scatter(theta, amp)
    ax.set_rmax(2)
    ax.set_rticks([0.5, 1, 1.5, 2])
    ax.set_rlabel_position(-22.5)

    ax.set_title("Hydrogen Orbital 2D Map")
    plt.savefig("hydrogen" + ".pdf")


polarPlot(dataPath)
