import time

def discrete_log(a, b, p, time_limit=300):
    start_time = time.time() # Початковий час
    # Перебираємо всі можливі значення x від 0 до p-2 (оскільки порядок групи Zp* дорівнює p-1)
    for x in range(p - 1):
        # Перевіряємо, чи виконується рівність a^x ≡ b (mod p)
        if pow(a, x, p) == b:
            elapsed_time = time.time() - start_time
            print(f"Час виконання: {elapsed_time:.2f} секунд")
            return x
        if time.time() - start_time > time_limit: 
            print("Час вичерпано")
            return None

a = 342 # генератор
b = 4297301 # елемент
p = 5786947 # модуль

log_result = discrete_log(a, b, p)

print(f"Дискретний логарифм числа beta = {b}, за основою alpha = {a}, по модулю p = {p} дорівнює: {log_result}")