import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import stats


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

# проверка статистической значимости I
# Теперь, когда у нас есть интуитивное представление о статистической значимости и p-значениях, мы применим его к данным о результатах нашего тестирования.
# Здесь мы рассчитываем размер тестовой и контрольной групп и их соответствующие коэффициенты конверсии.
def stat_sign_I(data1, data2):
