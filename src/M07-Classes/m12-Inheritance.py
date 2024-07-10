class Animal:
    def eat(self):
        print("Eat")


class Mammal(Animal):
    def walk(self):
        print("Walk")


class Fish(Animal):
    def swim(self):
        print("Swim")


m = Mammal()
m.eat()
