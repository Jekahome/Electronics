import matplotlib.pyplot as plt
import numpy as np

# Задаем коэффициенты линейной функции y = kx + b
k = 0  # угловой коэффициент
b = 5  # смещение

# Создаем массив значений x
x = np.linspace(-10, 10, 100)  # 100 точек от -10 до 10

# Вычисляем соответствующие значения y
y = k * x + b

# Строим график
plt.plot(x, y)
 
# Добавляем заголовок к графику
plt.title("График линейной функции: y = b")

# Включаем сетку для лучшей читаемости
plt.grid(True)

# Перемещаем оси в центр графика
ax = plt.gca()
ax.spines['left'].set_position('zero')
ax.spines['bottom'].set_position('zero')
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

# Добавляем подписи к осям
plt.xlabel("x", loc="right", fontweight="bold")
plt.ylabel("y", loc="top", fontweight="bold")

plt.errorbar(x, y, xerr=0.1, xlolims=False, label='xlolims=False')
plt.legend()
# Показываем график
plt.show()