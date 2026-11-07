from const import d_min, d_max, n_min, n_max
from logger import log_error

def validate_range(value: float, low: float, high: float) -> tuple[bool, str]:
    if value < low:
        return False, f"Ошибка: значение меньше нижней границы ({low})."
    elif value > high:
        return False, f"Ошибка: значение больше верхней границы ({high})."
    else:
        return True, ""

def input_number(promt: str, low: float, high: float):
    while True:
        r_num = input(promt).strip()
        try:
            r_num = float(r_num)
        except ValueError as e:
            msg = str(e.args[0]) if e.args else str(e)
            msg = f"Ошибка: введено не число ('{r_num}'). {msg}"
            print(msg)
            log_error(msg)
            continue
    
        ok, msg = validate_range(r_num, low, high)
        if ok:
            return r_num
        print(msg + " Повторите ввод.")
        log_error(msg)



def diametr():
    d = input_number("Введите диаметр заготовки D, мм (1..500): ", d_min, d_max)
    return d

def frequency():
    n = input_number("Введите частоту вращения n, об/мин (50..3000): ", n_min, n_max)
    return n