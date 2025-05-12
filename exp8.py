""" T TEST """
import numpy as np
from scipy import stats

N = 10

x = np.random.randn(N) + 2
y = np.random.randn(N)
print(x,y)

var_x = x.var(ddof=1)
var_y = y.var(ddof=1)

std = np.sqrt((var_x + var_y )/ 2)
print("standard deviation = ",std)

t_value = (x.mean() - y.mean()) / (std * np.sqrt(2/N))

print("T = ",t_value)

df = 2 * N -2

p_val = 1 - stats.t.cdf(t_value, df)
print("P = ", p_val)
