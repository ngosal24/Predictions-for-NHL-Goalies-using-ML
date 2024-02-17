import pandas as pd
import scipy.stats as stats

# import data
goalieData = pd.read_csv('data.csv', header = 0)

# run PearsonR test for correlation
corrtest = stats.pearsonr(goalieData['sv_pct'], goalieData['next_sv_pct'])

print('Correlation coefficient:', corrtest.statistic)
print('P-value:', corrtest.pvalue)