


class Animal:
    def __init__(self, color, weight, food):
        self.color = color
        self.weight = weight
        self.food = food

    def move(self):
        print('Animal is moving!')

    def ate(self):
        print(f'Animal is eating {self.food}!')

    def drink(self):
        print('Animal is drinking!')



class Dog(Animal):
    def __init__(self, color, weight, food, name, age):
        super().__init__(color, weight, food)
        self.name = name
        self.age = age

    def voice(self):
        print(f'gaf-gaf!!!')

tuzik = Dog('bleck', '22', 'meat', 'tuzik', '10')

tuzik.voice()

























