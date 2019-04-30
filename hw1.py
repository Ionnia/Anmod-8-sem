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
    # print("n = ", i, "Probability is ", v_otkaza[i-1][1])
    # print("Числитель:", pow(alpha, i) * calc_P0(i, alpha), "  Знаменатель: ", factorial(i))

# График вероятности отказа
# plt.plot([x[0] for x in v_otkaza], [y[1]*100 for y in v_otkaza])
# plt.xticks([x[0] for x in v_otkaza][1::2])
# plt.xlabel("Количество операторов")
# plt.ylabel("Вероятность отказа, %")
# plt.title("График вероятности отказа")
# plt.show()

def N_srednee(n):
    result = 0
    for i in range(1, n+1):
        result += i * calc_Pi(i, n, alpha)
    return result

def calc_q(n):
    return N_srednee(n)/n

q_zagruzki = []
for i in range(1, 21):
    q_zagruzki.append([i, calc_q(i)])
    # print("n = ", i, "q is ", q_zagruzki[i-1][1])

# # График занятости
# plt.plot([x[0] for x in q_zagruzki], [y[1] for y in q_zagruzki])
# plt.xticks([x[0] for x in q_zagruzki][1::2])
# plt.xlabel("Количество операторов")
# plt.ylabel("Занятость")
# plt.title("Занятость операторов")
# plt.show()

def calc_P0_ochered(n, m, alpha):
    sum1 = 0
    sum2 = 0
    for i in range(1, n+1):
        sum1 += (pow(alpha, i)/factorial(i))
    for i in range(n+1, n+m+1):
        sum2 += pow( (alpha/n), i-n) * (pow(alpha, n)/factorial(n))
    return 1/(sum1+sum2)

def calc_Pi_ochered(i, n, m, alpha):
    return pow(alpha/n, i-n) * (pow(alpha, n)/factorial(n)) * calc_P0_ochered(n, m, alpha)

izm_otkazov_pri_zamene_na_ochered = []

for i in range(0, 16):
    izm_otkazov_pri_zamene_na_ochered.append([i, calc_Pi_ochered(16, 16, i, alpha)])

# # График изменения отказов в зависимости от количества мест в очереди
plt.plot([x[0] for x in izm_otkazov_pri_zamene_na_ochered], [y[1]*100 for y in izm_otkazov_pri_zamene_na_ochered])
plt.xticks([x[0] for x in izm_otkazov_pri_zamene_na_ochered][1::2])
plt.xlabel("Мест в очереди")
plt.ylabel("Отказы, %")
plt.title("Изменение отказов от мест в очереди")
plt.show()