import time
import tracemalloc

# Ввод данных
a, b = map(int, input().split())

# Начинаем замер времени и памяти
start_time = time.time()
tracemalloc.start()


def factor(x):
    factors = {}
    while x % 2 == 0:
        factors[2] = factors.get(2, 0) + 1
        x //= 2
    i = 3
    while i * i <= x:
        while x % i == 0:
            factors[i] = factors.get(i, 0) + 1
            x //= i
        i += 2
    if x > 1:
        factors[x] = 1
    return factors

a_factors = factor(a)
b_factors = factor(b)

for p in a_factors:
    if p not in b_factors:
        print(-1)
        exit()

max_n = 0
for p in a_factors:
    k = a_factors[p]
    m = b_factors[p]
    current_n = (k + m - 1) // m
    if current_n > max_n:
        max_n = current_n

print(max_n)

# Завершаем замер времени и памяти
end_time = time.time()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()

print(f"Время выполнения: {end_time - start_time:.6f} секунд")
print(f"Пиковое использование памяти: {peak / 1024 / 1024:.6f} МБ")
print("Выполнил: Балилый Андрей Андреевич")
print("Группа: АИСа-024")
