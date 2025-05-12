import math
from statistics import variance
from sys import flags
import pandas as pd
import numpy as np

def frequency_distribution(data: list):
    intervals = ['1-3','4-6','7-9','total']
    f1 = sum(1 for i in data if 1 <= i <= 3)
    f2 = sum(1 for i in data if 4 <= i <= 6)
    f3 = sum(1 for i in data if 7 <= i <= 9)

    total = f1 + f2 + f3
    frequency = [f1, f2, f3, total]

    df = pd.DataFrame({'intervals':intervals, "frequecny":frequency})
    print(df)

def average(data: list) -> None:
    mean = sum(data) / len(data)
    print(mean)

def variability(data):
    intervals = [(1,3),(4,6),(7,9)]

    midpoints = []
    frequency = []
    for lower, upper in intervals:
        mid = (lower + upper) / 2
        midpoints.append(mid)
        count = sum(1 for i in data if lower <= i <= upper)
        frequency.append(count)

    midpoints = np.array(midpoints, dtype=float)
    frequency = np.array(frequency, dtype=float)

    total_frequency = np.sum(frequency)
    weight_sum = np.sum(frequency * midpoints)

    mean = weight_sum / total_frequency

    squared_diff = (midpoints - mean) ** 2

    variance = np.sum(frequency * squared_diff) / (total_frequency - 1)

    standard_dev = math.sqrt(variance)


    print("standard deviation :",standard_dev)
    print("variance ",variance)

a = [2,6,5,3,6,7,9,2,1,4,2]
frequency_distribution(a)
variability(a)

var = np.var(a)
standard_deviation = np.std(a)
