from operator import itemgetter

class Program:
    """Программа"""

    def __init__(self, id, name, price, computer_id=None):
        self.id = id
        self.name = name
        self.price = price
        self.computer_id = computer_id

class Computer:
    """Компьютер"""

    def __init__(self, id, name):
        self.id = id
        self.name = name

class ComputerProgram:
    """
    'Компьютеры-программы' для реализации связи многие-ко-многим
    """

    def __init__(self, computer_id, program_id):
        self.computer_id = computer_id
        self.program_id = program_id

computers = [
    Computer(1, 'Компьютер Alpha'),
    Computer(2, 'Компьютер Beta'),
    Computer(3, 'Компьютер Gamma'),
    Computer(4, 'Персональный Компьютер Delta'),
]

programs = [
    Program(1, 'Антивирус Kaspersky', 500, 1),
    Program(2, 'Браузер Yandex', 150, 2),
    Program(3, 'Графический редактор Adobe', 1200, 3),
    Program(4, 'Текстовый редактор Word', 300, 1),
    Program(5, 'Античит Faceit', 800, 4),
]

computers_programs = [
    ComputerProgram(1, 1),
    ComputerProgram(1, 4),
    ComputerProgram(2, 2),
    ComputerProgram(3, 3),
    ComputerProgram(4, 5),
    ComputerProgram(2, 5),
    ComputerProgram(3, 1),
    ComputerProgram(4, 3),
]

def res1(computers, programs):
    """Список компьютеров с названием 'Компьютер' и программами"""

    sort_computers = [c for c in computers if 'Компьютер' in c.name]
    comp_progs = {}

    for comp in sort_computers:
        progs_otm = [p.name for p in programs if p.computer_id == comp.id]
        progs_mtm = [
            p.name for cp in computers_programs 
            if cp.computer_id == comp.id 
            for p in programs if p.id == cp.program_id
        ]
        all_progs = list(set(progs_otm + progs_mtm))
        comp_progs[comp.name] = all_progs

    return comp_progs

def res2(computers, programs):
    """Список компьютеров со средней ценой программ, отсортированный по средней цене"""

    computer_avg_prices = []

    for comp in computers:
        prog_otm = [p.price for p in programs if p.computer_id == comp.id]
        prog_mtm = [
            p.price for cp in computers_programs 
            if cp.computer_id == comp.id 
            for p in programs if p.id == cp.program_id
        ]
        all_prices = prog_otm + prog_mtm

        if all_prices:
            avg_price = round(sum(all_prices) / len(all_prices), 2)
            computer_avg_prices.append((comp.name, avg_price))
    comp_avg_prices_sort = sorted(computer_avg_prices, key=itemgetter(1))

    return comp_avg_prices_sort

def res3(computers, programs):
    """Список программ начинающихся с 'А' и компьютеров"""

    sort_programs = [p for p in programs if p.name.startswith('А')]
    comp_dict = {c.id: c.name for c in computers}
    prog_comps = {}

    for program in sort_programs:
        comp_list = []
        if program.computer_id:
            comp_list.append(comp_dict.get(program.computer_id))

        for cp in computers_programs:
            if cp.program_id == program.id:
                comp_list.append(comp_dict.get(cp.computer_id))

        comp_uniq = list(filter(None, set(comp_list)))
        prog_comps[program.name] = comp_uniq

    return prog_comps

def main():

    #Запрос 1
    res_1 = res1(computers, programs)
    print('Задание Е1')
    for comp, progs in res_1.items():
        print(f"{comp}: {progs}")
    
    #Запрос 2
    res_2 = res2(computers, programs)
    print('\nЗадание Е2')
    for comp, avg in res_2:
        print(f"{comp}: Средняя цена программ = {avg}")
    
    #Запрос 3
    res_3 = res3(computers, programs)
    print('\nЗадание Е3')
    for prog, comps in res_3.items():
        print(f"{prog}: Установлено на компьютерах = {comps}")

if __name__ == '__main__':
    main()