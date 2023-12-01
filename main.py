import hypothesis_test
import numpy as np
import warnings
warnings.filterwarnings('ignore')

np.random.seed(42)
data1 = np.random.normal(loc=5, scale=2, size=100)
data2 = np.random.normal(loc=6, scale=2, size=100)
alpha = 0.05

hypothesis_test.plot(data1, data2)
hypothesis_test.t_test(data1, data2, alpha)

