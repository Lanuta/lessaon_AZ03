import numpy as np
import matplotlib.pyplot as plt

# Параметры нормального распределения
mean = 0         # Среднее значение
std_dev = 1      # Стандартное отклонение
num_samples = 1000  # Количество выборок

# Генерация случайных данных
data = np.random.normal(mean, std_dev, num_samples)

# Построение гистограммы
plt.figure(figsize=(8, 5))
plt.hist(data, bins=30, color='skyblue', edgecolor='black')
plt.title('Гистограмма нормального распределения')
plt.xlabel('Значения')
plt.ylabel('Частота')
plt.grid(True)
plt.show()