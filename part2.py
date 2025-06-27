import numpy as np
import matplotlib.pyplot as plt

# Генерируем два массива по 100 случайных чисел от 0 до 1
x = np.random.rand(100)
y = np.random.rand(100)

# Строим диаграмму рассеяния
plt.figure(figsize=(7, 5))
plt.scatter(x, y, color='mediumseagreen', alpha=0.7, edgecolor='black')
plt.title('Диаграмма рассеяния для случайных данных')
plt.xlabel('X значения')
plt.ylabel('Y значения')
plt.grid(True)
plt.show()