from math import gcd
from sympy import factorint

def build_table(alpha, p, prime_factors):
    tables = {}
    for prime, _ in prime_factors.items():
        table = {}
        for j in range(prime):
            r_pj = pow(alpha, ((p - 1) * j) // prime, p)
            table[j] = r_pj
        tables[prime] = table
    return tables

def modular_inverse(base, mod):
    if gcd(base, mod) != 1:
        raise ValueError(f"Основа {base} не є оборотною за модулем {mod}")
    return pow(base, -1, mod)

def solve_congruences(congruences, mod):
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
    p_minus_1 = p - 1
    prime_factors = factorint(p_minus_1)
    tables = build_table(alpha, p, prime_factors)
    congruences = []

    for prime, power in prime_factors.items():
        m = prime ** power
        x_p = 0
        beta_i = beta

        for i in range(power):
            exponent = p_minus_1 // (prime ** (i + 1))
            beta_i_exp = pow(beta_i, exponent, p)
            table = tables[prime]

            for j in range(prime):
                if table[j] == beta_i_exp:
                    x_p += j * (prime ** i)
                    break

            alpha_xp_mod = pow(alpha, x_p, p)
            beta_i = (beta * modular_inverse(alpha_xp_mod, p)) % p

        congruences.append((m, x_p))

    x = solve_congruences(congruences, p_minus_1)
    return x

if __name__ == "__main__":
    p = 3257  # Просте число (модуль групи)
    alpha = 6  # Генератор групи
    beta = 7531  # Елемент групи
    
    x = silver_pohlig_hellman(alpha, beta, p)
    print(f"x = {x}")  # Виводимо результат