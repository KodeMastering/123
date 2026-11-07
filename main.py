from mode import prmode, selmode, oper
from input_data import frequency, diametr
from calculations import cutting_speed, adjusted_speed, d_class

def main():
    prmode()
    k = selmode()
    op = oper(k)
    d = diametr()
    n = frequency()
    V = cutting_speed(d, n)
    V_adj = adjusted_speed(d, n)
    diameter_class = d_class(d)

    print("\nРезультаты расчёта:")
    print(f"Режим обработки: {op}")
    print(f"Коэффициент k: {k}")
    print(f"Скорость резания V = {V:.2f} м/мин")
    print(f"Скорректированная скорость V_adj = {V_adj:.2f} м/мин")
    print(f"Класс диаметра: {diameter_class}")


main()

    




