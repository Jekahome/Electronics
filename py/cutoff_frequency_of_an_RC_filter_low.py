import numpy as np
import matplotlib.pyplot as plt

# Параметры схемы
f_c = 1350        # Частота среза в Гц
Vin = 10          # Входное напряжение, В
R = 117892.55     # Сопротивление, Ом
C = 1e-9          # Емкость, Ф

# Генерация частот
frequencies = np.linspace(500, 10000, 500)

# Расчет выходного напряжения
Vout = Vin / np.sqrt(1 + (2 * np.pi * frequencies * R * C)**2)

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(frequencies / 1000, Vout, color='b', label='Выходное напряжение', linewidth=2)
plt.axvline(x=f_c / 1000, color='red', linestyle='--', label='Частота среза (1.35 кГц)')
plt.xlabel('Частота (Гц)')
plt.ylabel('Выходное напряжение (В)')
plt.title('График зависимости выходного напряжения от частоты')
plt.grid()
plt.legend()
plt.show()

 
 
