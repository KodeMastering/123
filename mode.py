from const import k1, k2, k3

def prmode():

    print("Режим обработки:")
    print("1 — черновая")
    print("2 — получистовая")
    print("3 — чистовая")

def selmode():
    while True:
        mode = input("Введите номер режима: ").strip()
        match mode:
            case "1":
                return k1
            case "2":
                return k2
            case "3":
                return k3
            case _:
                print("1, 2 или 3")

def oper(k):
    match k:
        case 1.0:
            return "черновая"
        case 0.85:
            return "получистовая"
        case 0.7:
            return "чистовая"
        case _:
            return "неизвестный"