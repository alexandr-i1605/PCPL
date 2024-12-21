import math

def get_coeff(name, value=None):
    while True:
        if value is not None:
            try:
                coeff = float(value)
                return coeff
            except ValueError:
                raise ValueError(f"Некорректное значение для коэфф. {name}: '{value}'. Нужно число.")


def solv(A, B, C):
    if A == 0:
        raise ValueError("Коэфф. A не должен быть = 0.")

    D = B**2 - 4*A*C
    if D < 0:
        return []

    y1 = (-B + math.sqrt(D)) / (2*A)
    y2 = (-B - math.sqrt(D)) / (2*A)

    roots = set()

    for y in [y1, y2]:
        if y < 0:
            continue
        elif y == 0:
            roots.add(0.0)
        else:
            sqrt_y = math.sqrt(y)
            roots.add(sqrt_y)
            roots.add(-sqrt_y)
    return sorted(roots)

if __name__ == "__main__":
    try:
        A = get_coeff("A", input("Введите коэфф. A: "))
        B = get_coeff("A", input("Введите коэфф. B: "))
        C = get_coeff("A", input("Введите коэфф. C: "))

        roots = solv(A, B, C)
        if not roots:
            print("Нет корней")
        else:
            print("Корни:")
            for root in roots:
                print(root)
    except ValueError as e:
        print(e)
