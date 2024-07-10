class Animal:
    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("Walk")


m = Mammal()
print(isinstance(m, Mammal))
print(isinstance(m, Animal))
print(isinstance(m, object))
print(issubclass(Mammal, Animal))
print(issubclass(Mammal, object))
