from const import pi, d_min, d_max
from typing import Annotated

def cutting_speed(
    d: Annotated[float, "Диаметр заготовки, мм"],
    n: Annotated[float, "Частота вращения, об/мин"]):
    V = pi * d * n / 1000
    return V

def adjusted_speed(V: Annotated[float, "Скорость резания, м/мин"],
    k: Annotated[float, "Коэффициент режима"]):
    V_adj = V*k
    return V_adj

def d_class(d: Annotated[float, "Диаметр заготовки, мм"]):
    if d < d_max:
        diameter_class = "малый диаметр"
    elif d_min <= d <= d_max:
        diameter_class = "нормальный диаметр"
    else:
        diameter_class = "крупный диаметр"
    return diameter_class