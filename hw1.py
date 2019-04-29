# Баймаканов В.К. РК6-81
# Вариант 1

from math import factorial, pow
import matplotlib.pyplot as plt

Tc = 25
Ts = 213
Tw = 514

lam = 1/Tc
mu = 1/Ts

alpha = lam/mu

def calc_P0(n, alpha):
    denominator = 1
    for i in range(0, n):
        denominator += pow(alpha, i+1)/factorial(i+1)
    return 1/denominator

def calc_Pi(i, n, alpha):
    return (pow(alpha, i)/factorial(i)) * calc_P0(n, alpha)

# Вероятность отказа
v_otkaza = []
for i in range(1, 21):
    v_otkaza.append([i, calc_Pi(i, i, alpha)])
    print("n = ", i, "Probability is ", v_otkaza[i-1][1])

# График вероятности отказа
plt.plot([x[0] for x in v_otkaza], [y[1]*100 for y in v_otkaza])
plt.xticks([x[0] for x in v_otkaza][1::2])
plt.xlabel("Количество операторов")
plt.ylabel("Вероятность отказа, %")
plt.show()