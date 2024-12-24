import time

def discrete_log(a, b, p, time_limit=300):
    start_time = time.perf_counter() # Початковий час
    # Перебираємо всі можливі значення x від 0 до p-2 (оскільки порядок групи Zp* дорівнює p-1)
    for x in range(p - 1):
        # Перевіряємо, чи виконується рівність a^x ≡ b (mod p)
        if pow(a, x, p) == b:
            elapsed_time = time.perf_counter() - start_time
            print(f"Час виконання: {elapsed_time:.9f} секунд")
            return x
        if time.perf_counter() - start_time > time_limit: 
            print("Час вичерпано")
            return None

a = 47 # генератор
b = 655 # елемент
p = 719 # модуль

log_result = discrete_log(a, b, p)
       


print(f"Дискретний логарифм числа beta = {b}, за основою alpha = {a}, по модулю p = {p} дорівнює: {log_result}")