import scipy.stats as stats
import numpy as np

sample_mean = 110
population_mean = 100
population_std = 15
sample_size = 50
alpha = 0.05

z_score = (sample_mean - population_mean) / (population_std / np.sqrt(sample_size))
print("z = ",z_score)

z_table_value = stats.norm.ppf(1-alpha)
print("z table value = ",z_table_value)

if (z_score < z_table_value):
    print("we accept the null hypo")
else:
    print("reject the null hypo")

p_value = 1 - stats.norm.cdf(z_score)
print("p value = ",p_value)
if (p_value < alpha):
    print("reject null hypo")
else:
    print("failed to reject null hypo")


"""
Z = X BAR - u / (SIGMA / ROOT N)
"""
