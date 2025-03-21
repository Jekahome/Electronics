import numpy as np
import matplotlib.pyplot as plt

# Параметры RLC-цепи
L = 1.2  # Индуктивность, Гн
C = 0.0000001  # Ёмкость, Ф
R = 0.01  # Сопротивление, Ом

# Коэффициенты характеристического уравнения: a*s^2 + b*s + c = 0
a = L * C
b = R * C
c = 1

# Вычисление дискриминанта
discriminant = b**2 - 4 * a * c

# Нахождение полюсов
if discriminant >= 0:
    # Действительные корни
    s1 = (-b + np.sqrt(discriminant)) / (2 * a)
    s2 = (-b - np.sqrt(discriminant)) / (2 * a)
else:
    # Комплексные корни
    s1 = (-b + 1j * np.sqrt(-discriminant)) / (2 * a)
    s2 = (-b - 1j * np.sqrt(-discriminant)) / (2 * a)

# Вывод полюсов
print(f"Полюс 1: {s1}")
print(f"Полюс 2: {s2}")

# Визуализация полюсов на комплексной плоскости
plt.figure(figsize=(8, 6))
plt.scatter(np.real(s1), np.imag(s1), color='red', label=f'Полюс 1: {s1:.2f}')
plt.scatter(np.real(s2), np.imag(s2), color='blue', label=f'Полюс 2: {s2:.2f}')

# Отрисовка осей
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)

# Подписи
plt.title('Полюса RLC-цепи на комплексной плоскости')
plt.xlabel('Re(s)')
plt.ylabel('Im(s)')
plt.legend()
plt.grid(True)

# Показать график
plt.show()
