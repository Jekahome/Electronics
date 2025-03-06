# Мы изобразим, как выходное напряжение зависит от частоты сигнала для заданной RC-цепи.

import numpy as np
import matplotlib.pyplot as plt

# Данные
f_c = 1590  # Частота среза в Гц
R = 10000   # Сопротивление в Ом
C = 10e-9   # Ёмкость в Фарад
V_in = 10   # Входное напряжение в Вольтах

# Частоты от 0.5 до 10 кГц
frequencies = np.linspace(500, 10000, 500)

# Расчёт выходного напряжения
V_out = V_in * (2 * np.pi * frequencies * R * C) / np.sqrt(1 + (2 * np.pi * frequencies * R * C)**2)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(frequencies / 1000, V_out, color='blue', linewidth=2)
plt.axvline(x=f_c / 1000, color='red', linestyle='--', label='Частота среза (1.59 кГц)')

# Настройки графика
plt.xlabel('Частота (кГц)')
plt.ylabel('Выходное напряжение (В)')
plt.title('Зависимость выходного напряжения от частоты')
plt.grid()
plt.legend()
plt.show()
