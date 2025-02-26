import numpy as np

'''
 10*X_1-5*X_3=0
 -5*X_1+19*X_3-4*X_5=14
 -4*X_3+18*X_5=4

A = np.array([[a11, a21, a31], [a12, a22, a32], [a13, a23, a33]])
b = np.array([k1, k2, k3])
'''

# решение квадратных матриц
# метод solve быстрее и проще, если система квадратная.
def solve_system(A, b):
    """
    Решает квадратные матрицы для системы уравнений Ax = b.
    Возвращает вектор x.
    """
    try:
        x = np.linalg.solve(A, b)
        return x
    except np.linalg.LinAlgError:
        print("Система не имеет единственного решения.")
        return None

# Проверка решения разных размернойстей матриц
# Для квадратных матриц lstsq работает так же, как numpy.linalg.solve, 
# но возвращает дополнительную информацию (невязку, ранг, сингулярные значения)
def try_least_squares_solution(A, b):
    """
    Решает разных размернойстей матрицы для системы уравнений Ax = b.
    Возвращает вектор x.
    """
    try:
        # Решение методом наименьших квадратов
        x_lstsq, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

        print("Невязка:", residuals)
        print("Ранг матрицы A:", rank)
        print("Сингулярные значения A:", s)

        # Проверка невязки
        if residuals.size > 0:
            if np.all(residuals < 1e-10):  # Проверяем, что ВСЕ элементы residuals < 1e-10
                print("Решение точное.")
            else:
                print("Решение приближённое.")
        else:
            print("Невязка не вычислена. Система недоопределённая для не квадратных матриц.")
        return x_lstsq
    except np.linalg.LinAlgError:
        print("Система не имеет единственного решения.")
        return None

# Создание матрицы
A = np.array([[10, -5, 0], [-5, 19, -4], [0, -4, 18]]) # массивы колонок
b = np.array([0, 14, 4])
print("Матрица A:\n", A)
print("\nВектор b:\n", b)

print("\nНайти вектор неизвестных x, который удовлетворяет уравнению (Ax = b)")

x = solve_system(A, b)

if x is not None:
    print("\nРешение (solve):\n", x)
    #print(f"X_1: {x[0]}\nX_3: {x[1]}\nX_5: {x[2]}")

    print("\nПроверка решения A*x, результат должен быть близок к вектору b")
    result_solve = np.dot(A, x)
    print(result_solve)
    print("Сравнение с b (с учётом погрешностей):", np.allclose(result_solve, b, atol=1e-8))

x_lstsq = try_least_squares_solution(A, b)

if x_lstsq is not None:
    print("\nРешение (lstsq):\n", x_lstsq)
    #print(f"X_1: {x_lstsq[0]}\nX_3: {x_lstsq[1]}\nX_5: {x_lstsq[2]}")

    print("\nПроверка решения A*x, результат должен быть близок к вектору b")
    result_lstsq = np.dot(A, x_lstsq)
    result_lstsq_rounded = np.round(result_lstsq, decimals=8)
    print(result_lstsq_rounded)
    print("Сравнение с b (с учётом погрешностей):", np.allclose(result_lstsq_rounded, b, atol=1e-8))
    
    # Проверка с учётом погрешностей
    if np.allclose(result_lstsq_rounded, b, atol=1e-8):
        print("Решение корректно.")
    else:
        print("Решение некорректно.")
        

print("\n\n")

# ###################################################################
# Если матрица системы не квадратная 
# (то есть число уравнений не равно числу неизвестных)

'''
    # Решение методом наименьших квадратов
    x, residuals, rank, s = np.linalg.lstsq(A, b, rcond=None)

    print("Решение:", x)
    print("Невязка:", residuals)

    # Проверка невязки
    if residuals < 1e-10:
        print("Решение точное.")
    else:
        print("Решение приближённое.")

'''

# ###################################################################
'''
Собственные значения важны для динамических систем, где есть ёмкости и индуктивности (например, в RLC-цепях). 
В таких системах собственные значения определяют, как система ведёт себя со временем (устойчивость, колебания и т.д.).

В вашем случае система статическая (нет элементов, которые накапливают энергию), 
поэтому собственные значения не имеют прямого отношения к устойчивости.
'''

# Нахождение собственных значений и векторов
eigenvalues, eigenvectors = np.linalg.eig(A)

print("Собственные значения:", eigenvalues)
print("Собственные векторы:\n", eigenvectors)

# Извлекаем действительные части
real_parts = np.real(eigenvalues)

# Проверяем устойчивость
if np.all(real_parts < 0):
    print("Система устойчива: все собственные значения имеют отрицательную действительную часть.")
elif np.any(real_parts > 0):
    print("Система неустойчива: есть собственные значения с положительной действительной частью.")
else:
    print("Система на границе устойчивости: есть собственные значения с нулевой действительной частью.")

# Вывод действительных частей
print("Действительные части собственных значений:", real_parts)
# ###################################################################



import matplotlib.pyplot as plt

# Визуализация собственных значений
plt.figure(figsize=(6, 6))
plt.scatter(np.real(eigenvalues), np.imag(eigenvalues), color='red', label='Собственные значения')
plt.axvline(0, color='black', linestyle='--', label='Граница устойчивости')
plt.xlabel('Действительная часть')
plt.ylabel('Мнимая часть')
plt.title('Собственные значения на комплексной плоскости')
plt.legend()
plt.grid()
plt.show()