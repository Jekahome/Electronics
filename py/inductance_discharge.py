import numpy as np
import matplotlib.pyplot as plt

# Параметры цепи
I0 = 1.2  # Начальный ток, А
R = 10  # Сопротивление, Ом
L = 0.5  # Индуктивность, Гн
tau = L / R  # Постоянная времени, с

# Временные точки
t = np.linspace(0, 0.25, 1000)  # От 0 до 250 мс

# Ток в цепи
I_t = I0 * np.exp(-t / tau)

# Напряжение на катушке
U_L_t = I0 * R * np.exp(-t / tau)

# Энергия в катушке
W_t = 0.5 * L * I_t**2

# Построение графиков
plt.figure(figsize=(10, 8))

# График тока
plt.subplot(3, 1, 1)
plt.plot(t * 1000, I_t, label="Ток I(t)")
plt.xlabel("Время, мс")
plt.ylabel("Ток, А")
plt.grid()
plt.legend()

# График напряжения
plt.subplot(3, 1, 2)
plt.plot(t * 1000, U_L_t, label="Напряжение U_L(t)", color="orange")
plt.xlabel("Время, мс")
plt.ylabel("Напряжение, В")
plt.grid()
plt.legend()

# График энергии
plt.subplot(3, 1, 3)
plt.plot(t * 1000, W_t, label="Энергия W(t)", color="green")
plt.xlabel("Время, мс")
plt.ylabel("Энергия, Дж")
plt.grid()
plt.legend()

plt.tight_layout()
plt.show()