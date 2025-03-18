import matplotlib.pyplot as plt
import numpy as np

# Данные
frequencies = [6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12,12.5,13]  # Частоты в кГц
voltages = [1.168, 1.180, 1.195, 1.204, 1.211, 1.216, 1.219, 1.220, 1.220, 1.217, 1.214, 1.210, 1.205,1.200,1.194]  # Напряжения в В

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(frequencies, voltages, marker='o', linestyle='-', color='b', label='АЧХ')

# Настройка графика
plt.title('Амплитудно-частотная характеристика (АЧХ)')
plt.xlabel('Частота, кГц')
plt.ylabel('Напряжение, В')
plt.grid(True)
plt.legend()
plt.xticks(np.arange(6, 13, 0.5))  # Шаг по оси X
plt.yticks(np.arange(1.15, 1.25, 0.02))  # Шаг по оси Y

# Показать график
plt.show()