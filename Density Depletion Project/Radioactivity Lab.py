from BaseFunctions import *

path = "Radioactivity Lab .xlsx"
sheet = "Sheet1"


def voltageP(path, sheet):
    title = input("Plot Title: ")
    height = int(input("Enter height value for plot image: "))
    width = int(input("Enter width value for plot image: "))
    xlabel = input("X axis label: ")
    ylabel = input("Y axis label: ")

    x = columnData(path, sheet, "AD")
    y = columnData(path, sheet, "AH")

    fig, ax = plt.subplots(nrows=1)
    fig.set_figheight(height)
    fig.set_figwidth(width)

    ax.plot(x, y)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    ax.set_title(title)

    plt.savefig(title + ".pdf")

voltageP(path, sheet)