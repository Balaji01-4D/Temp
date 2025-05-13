import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Load dataset
mtcars = sns.load_dataset('mpg')

# Create new columns mimicking original 'gear' and 'disp' logic
mtcars['gear'] = mtcars['cylinders']
mtcars['disp'] = mtcars['displacement']

# Boxplot
plt.figure(figsize=(8, 6))
sns.boxplot(x='gear', y='disp', data=mtcars)
plt.xlabel('Gear')
plt.ylabel('Disp')
plt.title('Boxplot of disp by gear')
plt.show()

# One-way ANOVA
group_3 = mtcars[mtcars['gear'] == 3]['disp']
group_4 = mtcars[mtcars['gear'] == 4]['disp']
group_5 = mtcars[mtcars['gear'] == 5]['disp']

f_statistic, p_value = stats.f_oneway(group_3, group_4, group_5)

print(f"F-statistic: {f_statistic}")
print(f"P-value: {p_value}")