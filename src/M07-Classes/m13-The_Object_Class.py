class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 1


class Mammal(Animal):
    def __init__(self):
        print("Mammal Constructor")
        self.weight = 2
        super().__init__()


m = Mammal()
print(m.age)
print(m.weight)
