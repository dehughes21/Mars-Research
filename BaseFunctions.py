import numpy as np
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import BoundaryNorm
from matplotlib.ticker import MaxNLocator
import openpyxl
from openpyxl import load_workbook
import statistics
import datetime


def MagData_Morsch(file):
    magField = []
    magFieldR = []
    magFieldV = []
    magFieldLog = []
    magLocs = []

    with open(file, 'r') as mag:
        for line in mag:
            mag = float(line.split()[2])
            magR = float(line.split()[3])
            magV = magR / mag
            magLog = math.log(float(line.split()[0]), 10)

            lat = float(line.split()[0])
            long = float(line.split()[0])
            loc = (lat, long)

            magLocs.append(loc)
            magField.append(mag)
            magFieldR.append(magR)
            magFieldV.append(magV)
            magFieldLog.append(magLog)

            return magField, magFieldR, magFieldV, magFieldLog, magLocs


def columnData(path, shName, col):
    headerRows = int(input("How many rows is the header? (input 0 if no header)"))
    workbook = load_workbook(filename=path)
    sheet = workbook[shName]
    dataList = []
    n = 0
    for cell in sheet[col]:
        if n > (headerRows - 1):
            dataList.insert(n - 1, cell.value)
        n += 1
    dataList = [data for data in dataList if data is not None]
    return dataList

def test():
    print("valid")
