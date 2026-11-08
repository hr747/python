class person:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def eat(self):
        print('vat mangso')

    def exeracisr(self):
        raise NotADirectoryError


class cricketer (person):
    def __init__(self, name, age, height, weight, team):
        self.team = team
        super().__init__(name, age, height, weight)
        # overriad

    def eat(self):
        print("vegatable")

    def exeracisr(self):
        print('tk diya gim a ja')
    def __add__(self, other):
        return self.age+other.age
    def __mul__(self, other):
        return self.weight*other.weight
    

    

sakib = cricketer('sakib', 40, 5, 70, 'bd')
muspik = cricketer('muspik', 35, 6, 60, 'bd')
sakib.eat()
sakib.exeracisr()


# overload
# print(45+45)
# print('sakib'+'rtakin')

# print([2, 4, 5, 6]+[3, 5, 77,])
print(sakib+muspik)
print(sakib*muspik)
