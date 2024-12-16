def discrete_log(a, b, p):
    for x in range(p - 1):
        if pow(a, x, p) == b:
            return x
    return None

a = 3  # генератор
b = 6  # елемент
p = 7  # модуль

log_result = discrete_log(a, b, p)

print(f"Дискретний логарифм числа {b} за основою {a} по модулю {p} дорівнює: {log_result}")