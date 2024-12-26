import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    speed = 10

    def __init__(self, cords, speed):
        self.cords = cords
        self.speed = speed

    def move(self, dx, dy, dz):
        self.dx = self._cords[0] + dx * self.speed
        self.dy = self._cords[1] + dy * self.speed
        self.dz = self._cords[2] + dz * self.speed
        if self.dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[0] = self.dx
            self._cords[1] = self.dy
            self._cords[2] = self.dz

    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")

    def attack(self):
        if self._DEGREE_OF_DANGER < 5:  # если степень опасности меньше 5
            print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")  # , если равно или больше.

    def speak(self):
        print(self.sound)


class Bird(Animal):
    beak = True

    def __init__(self, cords, speed):
        super().__init__(cords, speed)

    def lay_eggs(self):
        print(f"Here are(is) {random.randint (1,4)} eggs for you")  # выводит строку "Here are(is) <случайное число от 1 до 4> eggs for you"

class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def __init__(self, cords, speed):
        super().__init__(cords, speed)

    def dive_in(self, dz):
        dz = abs(dz)
        self._cords[2] -= dz  # Уменьшаем z в _cords
        self.speed = self.speed / 2  # Уменьшаем скорость в 2 раза


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8

    def __init__(self, cords, speed):
        super().__init__(cords, speed)


class Duckbill(Bird, AquaticAnimal, PoisonousAnimal):
    _DEGREE_OF_DANGER = 7
    sound = "Click-click-click"

    def __init__(self, cords, speed):
        super().__init__(cords, speed)


db = Duckbill(1, 10)
print(db.live)
print(db.beak)
db.speak()
db.attack()
db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()
db.lay_eggs()

