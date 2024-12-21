import math

def get_coeff(name, value=None):
    while True:
        if value is not None:
            try:
                coeff = float(value)
                return coeff
            except ValueError:
                print(f"Некорректное значение для коэфф. {name}: '{value}'. Нужно число.")
                value = None
        value = input(f"Введите коэфф. {name}: ")
        

def solv(A, B, C):
    if A == 0:
        print("Коэфф. A не должен быть = 0")
        return

    D = B**2 - 4*A*C
    print(f"D = {D}")

    if D < 0:
        print("Нет корней")
        return

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

    if not roots:
        print("Нет корней")
    else:
        sorted_roots = sorted(roots)
        print("Корни:")
        for root in sorted_roots:
            print(root)


def main():
    coefs = {}
    A = get_coeff('A', coefs.get('A'))
    B = get_coeff('B', coefs.get('B'))
    C = get_coeff('C', coefs.get('C'))

    solv(A, B, C)

if __name__ == "__main__":
    main()