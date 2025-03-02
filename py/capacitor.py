import numpy as np
import matplotlib.pyplot as plt

# Данные
E = 9  # Напряжение источника (В)
R = 10  # Сопротивление (Ом)
C = 200e-6  # Ёмкость (Ф)
t_max = 0.01  # Время до 10 мс (с)

# Постоянная времени
tau = R * C

# Время от 0 до 10 мс
t = np.linspace(0, t_max, 1000)

# Напряжение на конденсаторе
U_C = E * (1 - np.exp(-t / tau))

# Ток в цепи
I = (E / R) * np.exp(-t / tau)

# Заряд на конденсаторе
Q = C * U_C

# Энергия в конденсаторе
W = 0.5 * C * U_C**2

# Построение графиков
plt.figure(figsize=(10, 6))

# График напряжения
plt.plot(t * 1000, U_C, label="Напряжение на конденсаторе, $U_C(t)$ (В)", color="blue")

# График тока
plt.plot(t * 1000, I, label="Ток в цепи, $I(t)$ (А)", color="red", linestyle="--")

# График заряда
plt.plot(t * 1000, Q * 1000, label="Заряд на конденсаторе, $Q(t)$ (мКл)", color="green", linestyle="-.")

# График энергии
plt.plot(t * 1000, W * 1000, label="Энергия в конденсаторе, $W(t)$ (мДж)", color="purple", linestyle=":")

# Настройки графика
plt.title("Изменение напряжения, тока, заряда и энергии при заряде конденсатора")
plt.xlabel("Время, $t$ (мс)")
plt.ylabel("Напряжение (В) / Ток (А) / Заряд (мКл) / Энергия (мДж)")
plt.grid(True)
plt.legend()
plt.show()