import matplotlib.pyplot as plt
import math
import numpy as np

def normalCurve(): # A
    x = np.arange(0, math.pi * 2, 0.05)
    y = np.sin(x)

    plt.plot(x,y)
    plt.xlabel("Angle")
    plt.ylabel("Sine")
    plt.show()

def scatterPlot(): # B
    x = np.random.randn(50)
    y1 = x * 5 + 3
    y2 = -5 * x
    y3 = np.random.randn(50)

    plt.scatter(x,y1,label='positive',color='green')
    plt.scatter(x,y2,label='negative',color='red')
    plt.scatter(x,y3,label='zero',color='blue')
    plt.legend()
    plt.show()

def corelationCoefficient(): # C
    x = np.random.randn(50)
    y1 = x * 5 + 3
    y2 = -5 * x
    y3 = np.random.randn(50)

    plt.scatter(x,y1,label=f'positive correlation coff = {np.round(np.corrcoef(x,y1)[0,1],1)}',color='green')
    plt.scatter(x,y2,label=f'negative correlation coff = {np.round(np.corrcoef(x,y2)[0,1],1)}',color='red')
    plt.scatter(x,y3,label=f'zero correlation coff = {np.round(np.corrcoef(x,y3)[0,1],1)}',color='blue')
    plt.legend()
    plt.show()
