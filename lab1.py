# Лабораторна робота №1 на тему "Обчислення показників надійності за даними випробувань"
# Виконав студент групи ІО-71 Морозов-Леонов О.С., варіант №16

# Вхідна вибірка наробітків до відмови (у годинах)

hour_table = [233, 303, 81, 129, 200, 82, 115, 228, 64, 17,
              67, 648, 29, 39, 210, 10, 94, 465, 135, 312,
              606, 698, 15, 764, 32, 45, 54, 13, 116, 24,
              477, 16, 841, 95, 3, 79, 118, 208, 9, 59, 171,
              295, 78, 67, 38, 57, 91, 18, 39, 324, 416,
              270, 114, 25, 675, 287, 374, 119, 227, 5,
              109, 94, 171, 226, 183, 350, 27, 64, 433, 88,
              167, 152, 159, 319, 8, 162, 36, 488, 65, 77,
              307, 522, 140, 65, 355, 482, 180, 29, 342,
              233, 117, 182, 184, 113, 86, 630, 476, 136,
              397, 66]

# Завдання за варіантом:
# 1. Середній наробіток до відмови Tср,
# 2. γ-відсотковий наробіток на відмову Tγ при γ = 0.62,
# 3. ймовірність безвідмовної роботи на час 275 годин,
# 4. інтенсивність відмов на час 648 годин

gamma = 0.62
time1 = 275
time2 = 648

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
    interval_len = (sorted_table[-1] - sorted_table[0]) / 10

    for i in range(0, 10):
        ten_intervals.append([a for a in sorted_table if (i * interval_len <= a <= (i + 1) * interval_len)])

    stat_densities = [len(interval) / (len(sorted_table) * interval_len) for interval in ten_intervals]
    area_sum = 1
    for i in range(10):
        P_list.append(area_sum)
        area_sum -= stat_densities[i] * interval_len

    p_less = max([p for p in P_list if p < gamma])
    p_more = min([p for p in P_list if p > gamma])

    #index_less = P_list.index(p_less)
    index_more = P_list.index(p_more)

    d = (p_more - gamma) / (p_more - p_less)
    T = index_more + interval_len * d
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
