# Домашнее задание по ТМО. Задание #1
# Баймаканов В.К. РК6-81Б

from matplotlib import pyplot as plt
import math

# Условия
t_c = 25 # Среднее время звонка
t_s = 213 # Среднее время обслуживания

lam = 1/t_c
mu = 1/t_s

# lam - интенсивность потока заявок, mu
def p_n(n, lam, mu):
    p = lam/mu
    p0 = 1
    for i in range(1, n+1):
        p0 += p**i/math.factorial(i)
    p0 = p0**(-1)
    p_n = []
    p_n.append(p0)
    for i in range(1, n+1):
        p_n.append(p0 * p**i/math.factorial(i))
    return p_n

def p_otkaza(n, lam, mu):
    p_otkaza = p_n(n, lam, mu)
    return p_otkaza[n]

# Задание 1
p_n_otkaza = []
q_n_zagruzka = []
p_x_axis = []
for i in range(1, 25):
    p_n_otkaza.append(p_otkaza(i, 1/t_c, 1/t_s))
    Q = 1 - p_n_otkaza[i-1]      # Относительная пропускная способность
    A = lam * Q                 # Абсолютная пропускная способность
    k_zan = A/mu                # Среднее число занятых каналов
    q_zag = k_zan/i             # Коэффициент загрузки каналов
    p_x_axis.append(i)
    q_n_zagruzka.append(q_zag)
    print("Доля отказов для", i, "операторов:", p_n_otkaza[i-1])

p_n_otkaza = [100*otk for otk in p_n_otkaza]

plt.plot(p_x_axis, p_n_otkaza)
plt.title("Вероятность отказа в зависимости от числа операторов")
plt.show()
plt.close()

plt.plot(p_x_axis, q_n_zagruzka)
plt.title("Коэффициент загрузки в зависимости от числа операторов")
plt.show()
plt.close()