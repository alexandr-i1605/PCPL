def field(items, *args):
    assert len(args) > 0, "Необходимо передать хотя бы одно поле для выборки."
    for item in items:
        if len(args) == 1:
            value = item.get(args[0])
            if value is not None:
                yield value
        else:
            filtered = {a: item[a] for a in args if item.get(a) is not None}
            yield filtered

if __name__ == "__main__":
    goods = [
        {'title': 'Ковер', 'price': 2000, 'color': 'green'},
        {'title': 'Диван для отдыха', 'color': 'black'},
        {'title': 'Стол', 'price': 1500, 'color': None},
    ]
    
    for i in field(goods, 'title'):
        print(i)
        
    for i in field(goods, 'title', 'price'):
        print(i)