from gen_random import gen_random

class Unique:
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.items = iter(items)
        self.seen = set()

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case and isinstance(item, str) else item
            if key not in self.seen:
                self.seen.add(key)
                return item

if __name__ == "__main__":

    data1 = [1, 1, 1, 1, 1, 2, 2, 2, 2, 2]
    unique1 = Unique(data1)
    print("Пример 1:")
    for i in unique1:
        print(i)

    data2 = gen_random(10, 1, 3)
    unique2 = Unique(data2)
    print("Пример 2:")
    for i in unique2:
        print(i)

    data3 = ['a', 'A', 'b', 'B', 'a', 'A', 'b', 'B']
    unique3 = Unique(data3)
    print("Пример 3:")
    for i in unique3:
        print(i)

    unique4 = Unique(data3, ignore_case=True)
    print("Пример 4:")
    for i in unique4:
        print(i)