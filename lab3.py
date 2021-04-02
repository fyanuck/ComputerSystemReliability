#import math
from math import factorial, e, log

P1 = 0.75
P2 = 0.10
P3 = 0.87
P4 = 0.55
P5 = 0.60
P6 = 0.28
P7 = 0.36
P8 = 0.76


def calc(P1, P2, P3, P4, P5, P6, P7, P8):
    # Трикутник 123 - у зірку
    P12 = 1 - (1 - P1) * (1 - P2)
    P13 = 1 - (1 - P1) * (1 - P3)
    P23 = 1 - (1 - P2) * (1 - P3)

    # Об'єднання послідовних P13 та P4, P23 та P5
    P134 = P13 * P4
    P235 = P23 * P5

    # Трикутник 678 - у зірку
    P67 = 1 - (1 - P6) * (1 - P7)
    P68 = 1 - (1 - P6) * (1 - P7)
    P78 = 1 - (1 - P7) * (1 - P8)

    # Об'єднання послідовних P134 та P67, P235 та P68
    P13467 = P134 * P67
    P23568 = P235 * P68

    # Об'єднання паралельних P13467 та P23568
    P_paral = 1 - (1 - P13467) * (1 - P23568)

    # Сумарне P - об'єднання послідовних P12, P_paral та P78
    P = P12 * P_paral * P78
    return P


print("Ймовірність безвідмовної роботи системи протягом 10 годин = ", calc(P1, P2, P3, P4, P5, P6, P7, P8))

time = 2403
k1 = k2 = 1

P_system = calc(P1, P2, P3, P4, P5, P6, P7, P8)
Q_system = 1 - P_system
T_system = -time / log(P_system, e)

Q_reserved_system = Q_system * Q_system / factorial(k1 + 1) # При K = 1 и произведении до К+1 считается Q^2
P_reserved_system = 1 - Q_reserved_system
T_reserved_system = -time / log(P_reserved_system, e)
G_q = Q_reserved_system / Q_system
G_p = P_reserved_system / P_system
G_t = T_reserved_system / T_system

Q_reserved_1 = (1 - P1)**(k2 + 1)
Q_reserved_2 = (1 - P2)**(k2 + 1)
Q_reserved_3 = (1 - P3)**(k2 + 1)
Q_reserved_4 = (1 - P4)**(k2 + 1)
Q_reserved_5 = (1 - P5)**(k2 + 1)
Q_reserved_6 = (1 - P6)**(k2 + 1)
Q_reserved_7 = (1 - P7)**(k2 + 1)
Q_reserved_8 = (1 - P8)**(k2 + 1)

P_reserved_1 = 1 - Q_reserved_1
P_reserved_2 = 1 - Q_reserved_2
P_reserved_3 = 1 - Q_reserved_3
P_reserved_4 = 1 - Q_reserved_4
P_reserved_5 = 1 - Q_reserved_5
P_reserved_6 = 1 - Q_reserved_6
P_reserved_7 = 1 - Q_reserved_7
P_reserved_8 = 1 - Q_reserved_8

P_all_reserved_system = calc(P_reserved_1, P_reserved_2, P_reserved_3, P_reserved_4, P_reserved_5, P_reserved_6,
                             P_reserved_7, P_reserved_8)
Q_all_reserved_system = 1 - P_all_reserved_system
T_all_reserved_system = -time / log(P_all_reserved_system, e)
G_all_q = Q_all_reserved_system / Q_system
G_all_p = P_all_reserved_system / P_system
G_all_t = T_all_reserved_system / T_system

print("Базова імовірність безвідмовної роботи = {}\n"
      "Базова імовірність відмови = {}\n"
      "Базовий середній наробіток на відмову = {}\n".format(P_system, Q_system, T_system))

print("Імовірність безвідмовної роботи системи з навантаженим загальним резервуванням = {}\n"
      "Імовірність відмови системи з ненавантаженим загальним резервуванням = {}\n"
      "Середній час роботи системи з ненавантаженим загальним резервуванням = {}".format(P_reserved_system,
                                                    Q_reserved_system, T_reserved_system))
print("Виграш системи з ненавантаженим загальним резервуванням по імовірності безвідмовної роботи = {}\n"
      "Виграш системи з ненавантаженим загальним резервуванням по імовірності відмови = {}\n"
      "Виграш системи з ненавантаженим загальним резервуванням по середньому часу роботи = {}\n".format(G_p, G_q, G_t))

print("Імовірність безвідмовної роботи системи з навантаженим розподіленим резервуванням = {}\n"
      "Імовірність відмови системи з навантаженим розподіленим резервуванням = {}\n"
      "Середній час роботи системи з навантаженим розподіленим резервуванням = {}".format(P_all_reserved_system,
                                                                Q_all_reserved_system, T_all_reserved_system))
print("Виграш системи з навантаженим розподіленим резервуванням по імовірності безвідмовної роботи = {}\n"
      "Виграш системи з навантаженим розподіленим резервуванням по імовірності відмови = {}\n"
      "Виграш системи з навантаженим розподіленим резервуванням по середньому часу роботи = {}\n".format(G_all_p,
                                                                                        G_all_q, G_all_t))