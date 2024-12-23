class Vehicle:
    __COLOR_VARIANTS = ['черный', 'серый', 'белый', 'красный', 'зеленый'] # Атрибут класса, в который записан список
                                                                          # допустимых цветов для окрашивания.
    def __init__(self, owner, model, engine_power, color):
        self.owner = owner                 # владелец транспорта. (владелец может меняться)
        self.__model = model               # модель (марка) транспорта. (мы не можем менять название модели)
        self.__engine_power = engine_power # мощность двигателя. (мы не можем менять мощность двигателя самостоятельно)
        self.__color = color               # название цвета. (мы не можем менять цвет автомобиля своими руками)

    def get_model(self):
        return f"Модель: {self.__model}"                     # возвращает строку: "Модель: <название модели транспорта>"

    def get_horsepower(self):
        return f"Мощность двигателя: {self.__engine_power}" #- возвращает строку: "Мощность двигателя: <мощность>"

    def get_color(self):
        return f"Цвет: {self.__color}"                      #- возвращает строку: "Цвет: <цвет транспорта>"

    def print_info(self):                                   # - распечатывает результаты методов (в том же порядке):
        print(self.get_model())# get_model, get_horsepower, get_color; а так же владельца в конце в формате "Владелец: <имя>"
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
#        if new_color in self.__COLOR_VARIANTS:
        if new_color.lower() in (color.lower() for color in self.__COLOR_VARIANTS):
            self.__color = new_color  # - принимает аргумент new_color(str), меняет цвет __color на new_color,
            # если он есть в списке __COLOR_VARIANTS, в противном случае выводит на экран надпись: "Нельзя сменить цвет на <новый цвет>".
        else:
            print(f'Нельзя сменить цвет на {new_color}')

class Sedan(Vehicle):
    __PASSENGERS_LIMIT = 5

    def __init__(self, owner, model, engine_power, color):
        super().__init__(owner, model, engine_power, color)


vehicle1 = Sedan('Тояма Токанава', 'Toyota Mark II', '500', 'Серый')

vehicle1.print_info()          # Изначальные свойства

# Меняем свойства (в т.ч. вызывая методы):
vehicle1.set_color('розовенький')
vehicle1.set_color('ЧЕРНЫЙ')
vehicle1.owner = 'Василиса'

vehicle1.print_info()          # Проверяем что поменялось