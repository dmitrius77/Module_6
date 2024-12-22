class Animal:
    def __init__(self, name):
        self.alive = True  # (живой)
        self.fed = False  # (накормленный)
        self.name = name
    def eat(self, food):
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # (съедобность)

class Mammal(Animal):
    pass
#    def eat(self, food):
#        if food.edible:
#            print(f"{self.name} съел {food.name}")
#            self.fed = True
#        else:
#            print(f"{self.name} не стал есть {food.name}")
#            self.alive = False
#class Predator(Mammal):
class Predator(Animal):
    pass
#    def eat(self, food):
#       if food.edible:
#           print(f"{self.name} съел {food.name}")
#           self.fed = True
#       else:
#           print(f"{self.name} не стал есть {food.name}")
#           self.alive = False


class Flower(Plant):
    pass
#    flower = Flower
#    flower.edible = False
#    def __init__(self, name):
#        name = self.name

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True

a1 = Predator('Крокодил Геннадий')
a2 = Mammal('Чебурашка')

p1 = Flower('Репейник')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)

a1.eat(p1)
a2.eat(p2)

print(a1.alive)
print(a2.fed)