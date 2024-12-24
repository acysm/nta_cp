import time
from math import gcd
from sympy import factorint

def build_table(alpha, p, prime_factors):
    tables = {}  # Словник для зберігання таблиць
    for prime, _ in prime_factors.items():  # Перебираємо кожний простий множник p-1
        table = {}  # Таблиця для поточного простого множника
        for j in range(prime):  # Обчислюємо значення r_{p_i, j} для кожного j
            # r_{p_i, j} = alpha^((p-1) * j / prime) mod p
            r_pj = pow(alpha, ((p - 1) * j) // prime, p)
            table[j] = r_pj
        tables[prime] = table  # Зберігаємо таблицю для поточного простого множника
    return tables  # Повертаємо всі таблиці

def modular_inverse(base, mod):
    if gcd(base, mod) != 1:
        raise ValueError(f"Основа {base} не є оберненою за модулем {mod}")
    return pow(base, -1, mod)

def solve_congruences(congruences, mod): # КТЛ
    x = 0
    N = 1
    for modulus, _ in congruences:
        N *= modulus
    for modulus, remainder in congruences:
        Ni = N // modulus
        inv = modular_inverse(Ni, modulus)
        x += remainder * Ni * inv
    return x % mod

def silver_pohlig_hellman(alpha, beta, p):
    p_minus_1 = p - 1  # Обчислюємо порядок групи (p-1)
    prime_factors = factorint(p_minus_1)  # Факторизуємо p-1 на прості множники
    tables = build_table(alpha, p, prime_factors)  # Будуємо таблиці r_{p_i, j}
    congruences = []  # Масив для зберігання систем конгруенцій

    for prime, power in prime_factors.items():
        m = prime ** power  # Обчислюємо m = prime^power
        x_p = 0  # Початкове значення x_p
        beta_i = beta  # Початкове значення beta_i

        for i in range(power):
            exponent = p_minus_1 // (prime ** (i + 1))  # Обчислюємо показник степеня
            beta_i_exp = pow(beta_i, exponent, p)  # Обчислюємо beta_i^exponent mod p
            table = tables[prime]  # Отримуємо таблицю для поточного prime

            for j in range(prime):  # Знаходимо j, для якого r_{p_i, j} == beta_i_exp
                if table[j] == beta_i_exp:
                    x_p += j * (prime ** i)  # Додаємо внесок j * (prime^i) до x_p
                    break

            # Оновлюємо beta_i для наступної ітерації
            alpha_xp_mod = pow(alpha, x_p, p)
            beta_i = (beta * modular_inverse(alpha_xp_mod, p)) % p

        congruences.append((m, x_p))  # Додаємо x_p до системи конгруенцій

    x = solve_congruences(congruences, p_minus_1)  # Розв'язуємо систему конгруенцій застосовуючи КТЛ
    return x

def main():
     
    alpha = 6  # Генератор групи
    beta = 7531  # Елемент групи
    p = 3257 # Модуль групи

    start_time = time.perf_counter()
    
    x = silver_pohlig_hellman(alpha, beta, p)
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    print(f"Дискретний логарифм: {x}")
    print(f"Час виконання: {elapsed_time:.9f} секунд")

if __name__ == "__main__":
    main()