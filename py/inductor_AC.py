'''


import numpy as np
import matplotlib.pyplot as plt

# Параметры цепи
U = 230  # Напряжение источника, В
f = 50   # Частота тока, Гц
L = 0.1  # Индуктивность катушки, Гн
R = 10   # Активное сопротивление, Ом

# Угловая частота
omega = 2 * np.pi * f

# Время
t = np.linspace(0, 0.1, 1000)  # От 0 до 0.1 секунды, 1000 точек

# Напряжение на источнике
u = U * np.sin(omega * t)

# Импеданс цепи
Z = np.sqrt(R**2 + (omega * L)**2)

# Фазовый сдвиг
phi = np.arctan((omega * L) / R)

# Ток в цепи
i = (U / Z) * np.sin(omega * t - phi)

# Мощность в цепи
p = u * i

# Построение графиков
plt.figure(figsize=(12, 8))

# График напряжения
plt.subplot(3, 1, 1)
plt.plot(t, u, label='Напряжение (U)')
plt.title('Напряжение, ток и мощность в RL-цепи')
plt.ylabel('Напряжение, В')
plt.legend()
plt.grid(True)

# График тока
plt.subplot(3, 1, 2)
plt.plot(t, i, label='Ток (I)', color='orange')
plt.ylabel('Ток, А')
plt.legend()
plt.grid(True)

# График мощности
plt.subplot(3, 1, 3)
plt.plot(t, p, label='Мощность (P)', color='green')
plt.xlabel('Время, с')
plt.ylabel('Мощность, Вт')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()
'''

import numpy as np
import matplotlib.pyplot as plt

# Параметры цепи
U = 230  # Напряжение источника, В
f = 50   # Частота тока, Гц
L = 0.1  # Индуктивность катушки, Гн
R = 10   # Активное сопротивление, Ом

# Угловая частота
omega = 2 * np.pi * f

# Время
t = np.linspace(0, 0.1, 1000)  # От 0 до 0.1 секунды, 1000 точек

# Напряжение на источнике
u = U * np.sin(omega * t)

# Импеданс цепи
Z = np.sqrt(R**2 + (omega * L)**2)

# Фазовый сдвиг
phi = np.arctan((omega * L) / R)

# Ток в цепи
i = (U / Z) * np.sin(omega * t - phi)

# Мощность в цепи
p = u * i

# Построение графиков
plt.figure(figsize=(12, 10))

# График напряжения и тока с фазовым сдвигом
plt.subplot(4, 1, 1)
plt.plot(t, u, label='Напряжение (U)')
plt.plot(t, i, label='Ток (I)', color='orange')
plt.title('Напряжение и ток в RL-цепи с фазовым сдвигом')
plt.ylabel('Амплитуда')
plt.legend()
plt.grid(True)

# График напряжения
plt.subplot(4, 1, 2)
plt.plot(t, u, label='Напряжение (U)')
plt.ylabel('Напряжение, В')
plt.legend()
plt.grid(True)

# График тока
plt.subplot(4, 1, 3)
plt.plot(t, i, label='Ток (I)', color='orange')
plt.ylabel('Ток, А')
plt.legend()
plt.grid(True)

# График мощности
plt.subplot(4, 1, 4)
plt.plot(t, p, label='Мощность (P)', color='green')
plt.xlabel('Время, с')
plt.ylabel('Мощность, Вт')
plt.legend()
plt.grid(True)

plt.tight_layout()
plt.show()