import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import matplotlib.pyplot as plt


def drawPlot(data, labels):
    plt.bar(labels, data)
    plt.show()

def drawDictPlot(dictionary):
    drawPlot(dictionary.values(), dictionary.keys())

def drawTupleList(tab):
    keys = []
    values = []
    for i in tab:
        keys.append(i[0])
        values.append(i[1])
    drawPlot(values, keys)

