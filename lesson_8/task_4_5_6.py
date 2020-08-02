class Store:
    Equipments = {
        'printer': [],
        'notebook': [], 
        'monitor': [],
    }

    @classmethod
    def show_info(cls, category='all'):
        if category == 'all':
            categories = list(cls.Equipments.keys())
        else:
            categories = [category]
        for category in categories:
            print('\t', category.upper())
            for obj in cls.Equipments[category]:
                print(obj)
            print()

    @classmethod
    def to_location(cls, category:str, location, dep:str, quantity:int):
        if Store.quantity_valid(quantity, category, location):
            count = 0
            for obj in cls.Equipments[category]:
                if obj['location'] != dep:
                    obj['location'] = dep
                    count += 1
                    if count >= quantity: break

    @staticmethod
    def quantity_valid(quantity, category, location):
        count = 0
        for obj in Store.Equipments[category]:
            if obj['location'] == location:
                count += 1
        if count < quantity:
            print(f'Неверное количество {category}. В {location} имеется {count} шт.')
            return False
        else: return True


class Equipment(Store):
    def __init__(self, category, name, model, location):
        self.category = category
        self.name = name
        self.model = model
        self.location = location
        
    def __str__(self):
        for attr in list(self.__dict__)[1:]:
            print(f'{attr} = {getattr(self, attr)}')
        return str()

    def __getitem__(self, attr):
        return self.__dict__[attr]

    def __setitem__(self, attr, value):
        self.__dict__[attr] = value

    def make_record(self):
        Store.Equipments[self.category].append(self)

class Printer(Equipment):
    def __init__(self, category, name, model, location, ptype, capasity):
        Equipment.__init__(self, category, name, model, location)
        self.ptype = ptype          # тип:лазерный, струйный
        self.capasity = capasity    # ёмкость лотка
        self.make_record()

class Notebook(Equipment):
    def __init__(self, category, name, model, location, CPU, RAM):
        Equipment.__init__(self, category, name, model, location)
        self.CPU = CPU              # процессор
        self.RAM = RAM              # оперативная память
        self.make_record()

class Monitor(Equipment):
    def __init__(self, category, name, model, location, diagonal, permission):
        Equipment.__init__(self, category, name, model, location)
        self.diagonal = diagonal        
        self.permission = permission     # разрешение
        self.make_record()

if __name__ == "__main__":
    printer1 = Printer('printer', 'HP', 'hp23', 'store', 'laser', '150')
    printer2 = Printer('printer', 'Xerox', 'X234', 'store', 'inkjet', '200')
    notebook1 = Notebook('notebook', 'ASUS', 'A123', 'store', 'AMD', '8Gb')
    notebook2 = Notebook('notebook', 'Lenovo', 'LV987', 'store', 'Intel', '4Gb')
    monitor1 = Monitor('monitor', 'Sony', 'S45', 'store', '27inch', 'FullHD')
    monitor2 = Monitor('monitor', 'HP', 'hp3456', 'store', '27inch', 'FullHD')
    print('Склад')
    Store.show_info()
    print()
    print('Перемещение одного принтера в отдел менеджеров')
    Store.to_location('printer', 'store', 'managers', 1)
    Store.show_info('printer')
    print()
    print('Отдать со склада 2 принтера')
    Store.to_location('printer', 'store', 'managers', 2)