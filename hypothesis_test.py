import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import stats
from statsmodels.stats import power as pwr


def plot(data1, data2):
    plt.figure(figsize=(8, 6))
    plt.plot(data1, label='Data 1')
    plt.plot(data2, label='Data 2')
    plt.title('Сравнение двух шумных рядов')
    plt.xlabel('Номер точки данных')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid(True)
    plt.show()



def t_test(data1, data2, alpha):
    t_stat, p_value = stats.ttest_ind(data1, data2)
    print(f"Значение t-статистики: {t_stat}")
    print(f"p-value: {p_value}")
    if p_value < alpha:
        print("Разница между средними значима")
    else:
        print("Разница между средними не значима")

def mean_12(data1, data2):
    print("Среднее для data1:", data1.mean())
    print("Среднее для data2: ", data2.mean())


def size(data1, data2, alpha, power):
    # Calculate conversion rate mean and std
    data1_mean = data1.mean()
    data1_std = data1.std()

    # Setting the parameters and we want to increase the purchase_mean to 0.1 in this experiment
    effect_size = (0.1 - data1_mean) / data1_std

    # Calculate ratio
    test_n = len(data2)
    cont_n = len(data1)
    sizes = [cont_n, test_n]
    ratio = max(sizes) / min(sizes)

    # Initialize analysis and calculate sample size
    analysis = pwr.TTestIndPower()
    ssresult = analysis.solve_power(effect_size=effect_size, power=power, alpha=alpha, nobs1=None, ratio=ratio)

    print(f'Sample Size: {int(ssresult)}')


# проверка статистической значимости I
# Теперь, когда у нас есть интуитивное представление о статистической значимости и p-значениях, мы применим его к данным о результатах нашего тестирования.
# Здесь мы рассчитываем размер тестовой и контрольной групп и их соответствующие коэффициенты конверсии.

#def stat_sign_I(data1, data2):

