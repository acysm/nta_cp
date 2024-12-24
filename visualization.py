import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Дані вимірювань методу перебору 1 тип
brute_force_first_p = [3, 4, 5, 6, 7, 8, 9, 10]
brute_force_first_seconds = [0.000046500, 0.000783100, 0.009179000, 0.105196000, 0.773626300, 31.841241000, 200.379076900, 300]

# Дані вимірювань методу перебору 2 тип
brute_force_second_p = [3, 4, 5, 6, 7, 8, 9]
brute_force_second_seconds = [0.000042900, 0.002705700, 0.029112600, 0.134254400, 3.095641300, 45.529286200, 243.52472400]

# Дані вимірювань алгоритму С-П-Г 1 тип
sph_first_p = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sph_first_seconds = [0.000051300, 0.000243600, 0.000763100, 0.002549300, 0.004535100, 0.005322400, 0.021864300, 0.012629300, 0.008762000, 0.021003300]

# Дані вимірювань алгоритму С-П-Г 2 тип
sph_second_p = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sph_second_seconds = [0.003805000, 0.020709600, 0.078945100, 0.114467400, 0.214115100, 6.855616400, 84.628680600, 300, None, None]

# Розмір графіку
plt.figure(figsize=(24, 12))

plt.plot(brute_force_first_p, brute_force_first_seconds, label="МП 1", marker='o', color='red')

plt.plot(brute_force_second_p, brute_force_second_seconds, label="МП 2", marker='o', color='blue')

# Графік алгоритму С-П-Г першого типу
plt.plot(sph_first_p, sph_first_seconds, label="СПГ 1", marker='o', color='green')

# Графік алгоритму С-П-Г другого типу
plt.plot(sph_second_p, sph_second_seconds, label="СПГ 2", marker='o', color='purple')

# Заголовки та легенда
plt.title("Залежність часу роботи від вхідного праметру p", fontsize=16)
plt.xlabel("Порядок числа, p", fontsize=12)
plt.ylabel("Час виконання, с", fontsize=12)
plt.yscale('log')  # Логарифмічна шкала
plt.grid(True, which="both", linestyle='--', linewidth=0.5)
plt.legend(fontsize=12)

# Збільшення точності до 10^-6
def scientific_formatter(y, pos):
    return f'{y:.6f}'

# форматування для осі y під нашу точність
plt.gca().yaxis.set_major_formatter(FuncFormatter(scientific_formatter))

plt.show()