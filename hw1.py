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
for i in range(1, 16):
    p_n_otkaza.append(p_otkaza(i, 1/t_c, 1/t_s))
    Q = 1 - p_n_otkaza[i-1]      # Относительная пропускная способность
    A = lam * Q                 # Абсолютная пропускная способность
    k_zan = A/mu                # Среднее число занятых каналов
    q_zag = k_zan/i             # Коэффициент загрузки каналов
    p_x_axis.append(i)
    q_n_zagruzka.append(q_zag)
    # print("Доля отказов для", i, "операторов:", p_n_otkaza[i-1])

p_n_otkaza = [100*otk for otk in p_n_otkaza]

# plt.plot(p_x_axis, p_n_otkaza, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Вероятность отказа в зависимости от числа операторов")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, q_n_zagruzka, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Коэффициент загрузки в зависимости от числа операторов")
# plt.show()
# plt.close()

# Задание 2

def p_n_m(n, m, lam, mu):
    p = lam/mu
    p0 = 1
    for i in range(1, n+1):
        p0 += p**i/math.factorial(i)
    p0 += ( p**(n+1)) / (n*math.factorial(n) ) * ( ( 1 - (p/n)**m ) / (1 - p/n) )
    p0 = p0**(-1)
    p_n_m = []
    p_n_m.append(p0)
    for i in range(1, n+1):
        p_n_m.append(p0 * (p**i/math.factorial(i)))
    counter = 1
    for i in range(n+1, n+m+1):
        p_n_m.append(p0 * (p**i/(n**counter * math.factorial(n))))
        counter += 1
    return p_n_m

def p_n_m_otkaz(n, m, lam, mu):
    p_n_m_list = p_n_m(n, m, lam, mu)
    return p_n_m_list[n+m]

def get_L_och(p0, n, m, lam, mu):
    p = lam/mu
    # L_och = p**(n+1)/( n * math.factorial(n))
    # L_och *= ( 1 - (p/n)**m * (m + 1 - (m/n)*p) ) / ( 1 - (p/n))**2
    L_och = 0
    for i in range(n, n+m+1):
        L_och += (p/n)**(i-n) * p**n/math.factorial(n) * (i-n) * p0
    return L_och

# При 16 операторах доля отказов меньше 1%
n = 16
m = 0
p_n_m_otkaz_list = []
p_n_m_zagruzka_list = []
L_och_list = []
p_n_m_zanyatost_och_list = []
T_och_list = []
p_x_axis.clear()
for i in range(1, 16):
    m = n - i
    p_n_m_list = p_n_m(i, m, lam, mu)
    p_otkaz = p_n_m_list[i+m]
    p_n_m_otkaz_list.append(p_otkaz)
    p0 = p_n_m_list[0]
    Q = 1 - p_n_m_otkaz_list[i-1]      # Относительная пропускная способность
    A = lam * Q                 # Абсолютная пропускная способность
    k_zan = A/mu                # Среднее число занятых каналов
    q_zag = k_zan/i             # Коэффициент загрузки каналов
    p_n_m_zagruzka_list.append(q_zag)
    L_och_list.append(get_L_och(p0, i, m, lam, mu)) # Мат. ожидание длины очереди
    p_n_m_zanyatost_och_list.append(L_och_list[i-1]/m)
    T_och_list.append(L_och_list[i-1]/lam)  # Мат. ожидание времени пребывания в очереди

    p_x_axis.append(i)

# plt.plot(p_x_axis, p_n_m_otkaz_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Вероятность отказа")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, p_n_m_zagruzka_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Коэффициент загрузки")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, L_och_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Средняя длина очереди")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, p_n_m_zanyatost_och_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Коэффициент занятости мест в очереди")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, T_och_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Время в очереди")
# plt.show()
# plt.close()

# Задание 3
def get_P0_inf_queue(n, lam, mu):
    p = lam/mu
    p0 = 1
    for i in range(1, n):
        p0 += p**i/math.factorial(i)
    p0 += (p**n/math.factorial(n)) * (1/(n-p))
    return p0**(-1)

def get_L_och_inf_queue(n, lam, mu):
    p = lam/mu
    p0 = get_P0_inf_queue(i, lam, mu)
    print("P0", p0)
    L_och = p0
    L_och *= p**(n+1)/(n * math.factorial(n))
    L_och /= (1 - (p/n))**2
    return L_och

n_start = math.ceil(lam/mu) + 1
p = lam/mu
L_och_list.clear()
p_n_m_zagruzka_list.clear()
T_och_list.clear()
p_x_axis.clear()

for i in range(n_start, 25):
    L_och = get_L_och_inf_queue(n, lam, mu)
    q_zag = p/i
    L_och_list.append(L_och)
    p_n_m_zagruzka_list.append(q_zag)
    T_och_list.append(L_och/lam)
    p_x_axis.append(i)

# plt.plot(p_x_axis, L_och_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Средняя длина очереди")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, p_n_m_zagruzka_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Коэффициент загрузки")
# plt.show()
# plt.close()

# plt.plot(p_x_axis, T_och_list, "b-o")
# plt.grid(linestyle='--', linewidth=0.5)
# plt.title("Средняя время в очереди")
# plt.show()
# plt.close()

# Задача 4

END_OF_QUEUE = 10

def get_P_0_inf_wait_queue(n, lam, mu, v):
    p = lam/mu
    p0 = 1
    for i in range(0, n):
        p0 += p**i / math.factorial(i)
    
    p0_sum_of_products = 0
    for i in range(1, END_OF_QUEUE):
        product = 1
        for j in range (1, i):
            product *= (n * mu + j * v)
        p0_sum_of_products += lam**i / product
    
    p0 += (p**n / math.factorial(n)) * p0_sum_of_products
    return p0**(-1)

def get_P_n_inf_wait_queue(n, lam, mu, v):
    p_n_wait_queue_list = []
    p0 = get_P_0_inf_wait_queue(n, lam, mu, v)
    p_n_wait_queue_list.append(p0)
    for i in range(1, n+1):
        p_n_wait_queue_list.append( p0 * (p**i/math.factorial(i)) )
    p_n = p_n_wait_queue_list[n]
    for i in range(1, END_OF_QUEUE+1):
        product = 1
        for j in range(1, i):
            product *= (n*mu + j*v)
        p_n_wait_queue_list.append( p_n * (lam**i / product) )
    return p_n_wait_queue_list

def get_L_och_inf_wait_queue(n, lam, mu, v):
    p_n_list = get_P_n_inf_wait_queue(n, lam, mu ,v)
    L_och = 0
    for i in range(n+1, n+END_OF_QUEUE+1):
        L_och += (i-n) * p_n_list[i]
    return L_och

def get_Zanyatost(n, lam, mu, v):
    p_n_list = get_P_n_inf_wait_queue(n, lam, mu ,v)
    k_zan = 0
    for i in range(1, n+1):
        k_zan += i * p_n_list[i]
    for i in range(n+1, n+END_OF_QUEUE+1):
        k_zan += n * p_n_list[i]
    return k_zan

t_w = 514
v = 1/t_w

L_och_list.clear()
q_n_zagruzka.clear()
T_och_list.clear()
p_x_axis.clear()

for i in range(1, 16):
    L_och_list.append(get_L_och_inf_wait_queue(i, lam, mu, v))
    q_n_zagruzka.append(get_Zanyatost(i, lam, mu, v))
    T_och_list.append(L_och_list[i-1]/lam)
    p_x_axis.append(i)

plt.plot(p_x_axis, L_och_list, "b-o")
plt.grid(linestyle='--', linewidth=0.5)
plt.title("Средняя длина очереди")
plt.show()
plt.close()

plt.plot(p_x_axis, q_n_zagruzka, "b-o")
plt.grid(linestyle='--', linewidth=0.5)
plt.title("Коэффициент загрузки")
plt.show()
plt.close()

plt.plot(p_x_axis, T_och_list, "b-o")
plt.grid(linestyle='--', linewidth=0.5)
plt.title("Средняя время в очереди")
plt.show()
plt.close()