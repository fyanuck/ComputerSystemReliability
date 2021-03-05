# Лабораторна робота №1 на тему "Обчислення показників надійності за даними випробувань"
# Виконав студент групи ІО-71 Морозов-Леонов О.С., варіант №16

# Вхідна вибірка наробітків до відмови (у годинах)

hour_table = [644, 1216, 2352, 1386, 1280, 903, 607, 2068,
4467, 835, 313, 555, 307, 508, 1386, 2895, 583,
292, 5159, 1107, 181, 18, 1247, 125, 1452, 4211,
890, 659, 1602, 2425, 214, 68, 21, 1762, 1118,
45, 1803, 1187, 2154, 19, 1122, 278, 1622, 702,
1396, 694, 45, 1739, 3483, 1334, 1852, 96, 173,
7443, 901, 2222, 4465, 18, 1968, 1426, 1424,
1146, 435, 1390, 246, 578, 281, 455, 609, 854,
436, 1762, 444, 466, 1934, 681, 4539, 164, 295,
1644, 711, 245, 740, 18, 474, 623, 462, 605, 187,
106, 793, 92, 296, 226, 63, 246, 446, 2234, 2491,
315]

# Завдання за варіантом:
# 1. Середній наробіток до відмови Tср,
# 2. γ-відсотковий наробіток на відмову Tγ при γ = 0.62,
# 3. ймовірність безвідмовної роботи на час 275 годин,
# 4. інтенсивність відмов на час 648 годин

gamma = 0.9
time1 = 2000
time2 = 2000

sorted_table = sorted(hour_table)
interval_len = 0
ten_intervals = []
stat_densities = []
P_list = []

if not 0 <= gamma <= 1 or not len(hour_table) or time1 > max(hour_table) or time2 > max(hour_table) \
        or time1 < 0 or time2 < 0:
    print("Incorrect values")
    exit(0)


def get_Tcp():
    return sum(hour_table) / len(hour_table)


def get_T(gamma):
    global interval_len, stat_densities, ten_intervals, P_list
    #interval_len = (sorted_table[-1] - sorted_table[0]) / 10
    interval_len = (max(sorted_table) - min(sorted_table)) / 10

    for i in range(0, 10):
        ten_intervals.append([a for a in sorted_table if (i * interval_len <= a <= (i + 1) * interval_len)])

    stat_densities = [len(interval) / (len(sorted_table) * interval_len) for interval in ten_intervals]
    area_sum = 1
    for i in range(10):
        P_list.append(area_sum)
        area_sum -= stat_densities[i] * interval_len

    p_less = max([p for p in P_list if p < gamma])
    p_more = min([p for p in P_list if p > gamma])

    index_less = P_list.index(p_less)
    index_more = P_list.index(p_more)

    #interval_len = 744.3

    d = (p_less - gamma) / (p_less - p_more)
    T = (interval_len * index_less) - interval_len * d
    return T


def p_unfail(time):
    Sum = 1
    whole_intervals = int(time // interval_len)
    for i in range(whole_intervals):
        Sum -= stat_densities[i] * interval_len
    Sum -= stat_densities[whole_intervals] * (time % interval_len)
    return Sum


def fail_freq(time):
    f = stat_densities[int(time // interval_len)]
    p = p_unfail(time)
    return f / p


# 1. Середній наробіток до відмови Tср
print("Середній наробіток до відмови Tср:", get_Tcp())

# 2. γ-відсотковий наробіток на відмову Tγ при γ = 0.62
print("γ-відсотковий наробіток на відмову Tγ при γ = 0.62:", get_T(gamma))

# 3. ймовірність безвідмовної роботи на час 275 годин
print("ймовірність безвідмовної роботи на час 275 годин:", p_unfail(time1))

# 4. інтенсивність відмов на час 648 годин
print("інтенсивність відмов на час 648 годин:", fail_freq(time2))
