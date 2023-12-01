import numpy as np
from matplotlib import pyplot as plt
from scipy.stats import stats, norm
import scipy.stats as sps
from statsmodels.stats import power as pwr


def plot(control_data, test_data):
    plt.figure(figsize=(8, 6))
    plt.plot(control_data, label='Control group')
    plt.plot(test_data, label='Test group')
    plt.title('Сравнение двух шумных рядов')
    plt.xlabel('Номер точки данных')
    plt.ylabel('Значение')
    plt.legend()
    plt.grid(True)
    plt.show()

def t_test(control_data, test_data, alpha):
    t_stat, p_value = stats.ttest_ind(control_data, test_data)
    print(f"Значение t-статистики: {t_stat}")
    print(f"p-value: {p_value}")
    if p_value < alpha:
        print("РЕЗУЛЬТАТ: Существует статистически значимая разница в доходах между контрольной и тестовой группами.")
        if test_data.mean() > control_data.mean():
            print("РЕЗУЛЬТАТ: тестовая группа привела к увеличению доходов.")
        else:
            print("РЕЗУЛЬТАТ: Контрольная группа получила более высокие доходы.")
        #print("Разница между средними значима")
    else:
        print("РЕЗУЛЬТАТ: Статистически значимой разницы в доходах между контрольной и тестовой группами нет.")
        #print("Разница между средними не значима")

def mean_12(control_data, test_data):
    print("Среднее для контрольной группы:", control_data.mean())
    print("Среднее для тестовой группы: ", test_data.mean())

# вот квантили, а как их сравнивать
def quantiles(control_data, test_data, q):
    print('Квантили контрольной группы:', np.quantile(control_data, q))
    print('Квантили тестовой группы:', np.quantile(test_data, q))


# кринж функция, я пока не знаю как нормально определить размер выборки и как правильно её сузить
def size(control_data, test_data, alpha, power):
    min_sample_size = min(len(control_data), len(test_data))

    print(f'Min sample Size: {min_sample_size}')


# проверка статистической значимости I
# Теперь, когда у нас есть интуитивное представление о статистической значимости и p-значениях, мы применим его к данным о результатах нашего тестирования.
# Здесь мы рассчитываем размер тестовой и контрольной групп и их соответствующие коэффициенты конверсии.

#def stat_sign_I(data1, data2):

