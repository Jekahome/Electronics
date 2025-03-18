import numpy as np
import matplotlib.pyplot as plt

# Параметры цепи
U = 230  # Напряжение источника, В
R = 10   # Активное сопротивление, Ом
L = 0.1  # Индуктивность, Гн

# Постоянная времени
tau = L / R

# Время
t = np.linspace(0, 0.05, 1000)  # От 0 до 50 мс

# Ток короткого замыкания
i_kz = (U / R) * (1 - np.exp(-(R / L) * t))

# Построение графика
plt.figure(figsize=(10, 6))
plt.plot(t * 1000, i_kz, label='Ток короткого замыкания, А', color='b')
plt.axhline(y=23, color='r', linestyle='--', label='Установившийся ток (23 А)')
plt.title('Рост тока короткого замыкания в RL-цепи')
plt.xlabel('Время, мс')
plt.ylabel('Ток, А')
plt.legend()
plt.grid(True)
plt.show()