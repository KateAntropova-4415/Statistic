import hypothesis_test as ab_test
import numpy as np
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
data1 = np.random.normal(loc=5, scale=2, size=100)
data2 = np.random.normal(loc=6, scale=2, size=100)
print("Контрольная группа (data1): ", data1)
print("Тестовая группа (data2): ", data2)
alpha = 0.05
print("")
ab_test.mean_12(data1, data2)
ab_test.plot(data1, data2)
print("")
ab_test.t_test(data1, data2, alpha)
print("")
#ab_test.size(data1, data2, alpha, 0.8)
#print("")
#ab_test.quantiles(data1, data2, 0.5)
#print("")
ab_test.shapiro_kolmog(data1, data2, alpha)

