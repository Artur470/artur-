                             ###ИНКАПСУЛЯЦИЯ####
"""class Africa:
    def init(self, arg_lion, arg_giraffe, arg_crocodile, arg_zebra,
                       arg_jakal, arg_rhinoceros, arg_elephant, arg_name):

        self.lion = arg_lion
        self.__giraffe = arg_giraffe
        self.__crocodile = arg_crocodile
        self.__zebra = arg_zebra
        self.__jakal = arg_jakal
        self.__rhinoceros = arg_rhinoceros
        self.__elephant = arg_elephant
        self.__name = arg_name


    def lion_is_the_king_of_the_animals(self):
        print(f'lion_and_di_hunt_for_any_promise_of_africa!!!')

    def giraffe_walks_with_both_rigth_legs_at_the_same_time(self):
        print(f'giraffe_run_fast_with_both_feet!!!')

    def the_crocodile_has_a_very_strong_jaw_and_teeth(self):
        print(f'crocodile_bites_off_one_of_the_victims_legs_the_first_time!!!')

    def zebra_has_very_good_hearing(self0):
        print(f'zebra_protects_its_family_froom_danger!!!')

    def a_jacal_can_store_food_in_itself(self):
        print(f'jacal_hroni_food_supply_for_a_month!!!')

    def rhinoceros_has_goot_vision_power(self):
        print(f'rhinoceros_go_turn_the_car_over!!!')

    def elephant_cant_jump(self):
        print(f'elephant_learn_to_jump!!!')



    def get_lion(self):
        return self.__lion

    def get_giraffe(self):
        return self.__giraffe

    def get_crocodile(self):
        return self.__crocodile

    def get_zebra(self):
        return self.__zebra

    def get_jakal(self):
        return self.__jakal

    def get_rhinoceros(self):
        return self.__rhinoceros

    def get_elephant(self):
        return self.__elephant


    def set_lion(self, new_lion):
        self.__lion = new_lion

    def set_giraffe(self, new_giraffe):
        self.__giraffe = new_giraffe

    def set_crocodile(self, new_crocodile):
        self.__crocodile = new_crocodile

    def set_zebra(self, new_zebra):
        self.__zebra = new_zebra

    def set_jakal(self, new_jakal):
        self.__zebra = new_jakal

    def set_rhinoceros(self, new_rhinoceros):
        self.__rhinoceros = new_rhinoceros

    def set_elephant(self, new_elephant):
        self.__elephant = new_elephant


    def show_info(self):
        print(f'name:  {self.__name}'
              f'lion : {self.get_lion()}\n'
              f'giraffe: {self.get_giraffe()}\n'
              f'crocodile: {self.get_crocodile()}\n'
              f'zebra: {self.get_zebra()}\n'
              f'jacal: {self.get_jakal()}\n'
              f'ghinoceros: {self.get_rhinoceros()}\n'
              f'elephant: {self.get_elephant()}\n')



savanna = Africa('lion', 'giraffe', 'crocodile', 'zebra',

                 'jakal', 'rhinoceros','elephant ', 'savanna')


savanna.show_info()

savanna.lion_is_the_king_of_the_animals()
savanna.giraffe_walks_with_both_rigth_legs_at_the_same_time()
savanna.the_crocodile_has_a_very_strong_jaw_and_teeth()
savanna.zebra_has_very_good_hearing()
savanna.a_jacal_can_store_food_in_itself()
savanna.rhinoceros_has_goot_vision_power()
savanna.elephant_cant_jump()
"""






   ### НАСЛЕДИЕ ###

"""
class Animal:
    def __init__(self, color, weight, food):
        self.__color = color
        self.__weight = weight
        self.__food = food

    def move(self):
        print('animals is moving!')

    def ate(self):
        print(f'animals is eating ')

    def drink(self):
        print('animals is drinking!')


class Dog(Animal):
    def __init__(self, color, weight, food, name, age):
        super().__init__(color, weight, food)

        self.name = name
        self.age = age
    def voice(self):
        print('gaf-gaf')

reks = Dog('bleck', '15', 'meat', 'reks', '11')
reks.voice()

"""

"""
class Animal:
    def __init__(self, color, weight, food):
        self.color = color
        self.weight = weight
        self.food = food

    def move(self):
        print('Animal is moving!')

    def ate(self):
        print(f'Animal is eating {self.food} ')

    def drink(self):
        print('Animal is drinking!')


class Dog(Animal):
    def __init__(self, color, weight, food, name, age):
        super().__init__(color, weight, food)
        self.name = name
        self.age = age


    def voice(self):
        print(f'gaf-gaf!')


    def get_name(self):
        return self.name


    def set_name(self, new_reks):
        self.name = new_reks

tuzik = Dog('bleck', '22', 'meat', 'tuzik', '9')

tuzik.set_name('reks')


"""



"""
class Human:

    def __init__(self, speak,  brain,  movement, intelligence, ):
        self.speak = speak
        self.brain = brain
        self.movement = movement
        self.intelligence = intelligence


    def think(self):
        print('Human is thinking!!!')

    def talk(self):
        print('Human is talking!!!')

    def eat(self):
        print('Human is eating!!!')

class Student(Human):

    def __init__(self, speak, brain, movement, intelligence,
                 name, age, study):

        super().__init__(speak, brain, movement, intelligence)
        self.name = name
        self.age = age
        self.study = study

    def study_well(self):
        print('student study well!!!')

    def be_hungry(self):
        print('student  go hungry for two days!!!')

    def without_education(self):
        print('student get an education!!!')


bekjan = Student('english', 'smart', 'write',
                 'effectively', 'bekjan','20', 'third year')
bekjan.study_well()


class Teacher(Human):

    def __init__(self, speak, brain, movement, intelligence, name,age, weight):
        super().__init__(speak, brain, movement, intelligence)
        self.name = name
        self.age = age
        self.weight = weight

    def teaches(self):
        print('teacher is teaching biology!!!')

    def there_is_education (self):
        print('let there be the highest!!!')

    def biology_teacher(self):
        print('learn biology well!!!')

maksim = Teacher('Russian', 'very smart', 'read the topic',
                 'effectively', 'maksim', '44', '71')
maksim.there_is_education()

"""

                       ###ПОЛИМАРФИЗМ###
"""
class Transport:

    def __init__(self,  model,   control, fara, weight, salon, color, year):
        self.__model = model
        self.__control = control
        self.__fara = fara
        self.__weight = weight
        self.__salon = salon
        self.__color = color
        self.__year = year

    def move(self):
        print('transport is moving!')

    def add_more(self):
        print('transport is add moreing!')

    def change_speed(self):
        print('transport change speeding!')

    def transport_sound(self):
        ...

class Car(Transport):

    def __init__(self, model,  control, fara,  weight, color,salon,
                 door, rul, motor, coleso, year):
        super().__init__(model,  control, fara, weight, salon,  color, year)
        self.__door = door
        self.__rul = rul
        self.__motor = motor
        self.__coleso = coleso

    def load_cargo(self):
         print('load cargo into storage!')

    def turn_on_the_music(self):
         print('turn on the music!')

    def put_the_phone_on_charge(self):
        print('put your phone on charge!')

    def transport_sound(self):
        print('run run ')

    def get_rul(self):
        return self.__rul

    def set_rul(self, new_bogaj):
        self.__rul = new_bogaj


class Truck(Transport):
    def __init__(self, model, control, fara,  weight, color, salon, year, trailer, dop_coleso,
                 rul, two_door, fuel):
        super().__init__(model, control, fara, weight, color, salon, year, )
        self.__trailer = trailer
        self.__dop_coleso = dop_coleso
        self.__rul = rul
        self.__two_door = two_door
        self.__fuel = fuel

    def transport_goods(self):
        print('transport cars!')
    def transport_sound(self):
        print('run run !!!')


class Train(Transport):

    def __init__(self, model, control, fara,  weight, color,
                 salon, year,vogons, pair_of_wheels, control_panel):
        super().__init__(model, control, fara,  weight, color, salon, year)

        self.__vogons = vogons
        self.__pair_of_wheels = pair_of_wheels
        self.__control_panel = control_panel


    def ride_on_rails(self):
        print('rude on a different track!')

    def pull_vogons(self):
        print('pull 12 vogons!')
    def transport_sound(self):
        print('tu tU!!!')

bmw = Car('bmw', 'mechanics','dark', 'high_speed','1,5t', 'bleck',
          'leather', 'closed', 'sport', 'powerful', 'titanium', )
bmw.load_cargo()
bmw.transport_sound()
bmw.set_rul("bogaj")
print(bmw.get_rul())


        
mers = Truck('mers', 'avtomat', 'big', '90', '20t', 'white','panel',
             '2001', '6,5', 'sport', 'open', 'fuel')

mers.transport_sound()

"""

"""
class Point:
    def __init__(self, x, y):

        self.x = x
        self.y = y

    def draw(self):
        ...

class Circle(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def draw(self):
        print('D----PI =3,14 ')


class Line(Point):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.x = x
        self.y = y

    def draw(self):
        print('. .')


class Box(Point):
    def __init__(self, x, y, a, b):
        super().__init__(x, y)
        self.a = a
        self.b = b

    def draw(self):
        print('. . . .')



krug = Circle(' shir  kruga',  'dl kruga')
krug.draw()

line = Line('a', 'b')
line.draw()

box = Box('a', 'b', 'd', 'c')
box.draw()

"""
"""

a = [
    [1,2,3,],
    [4,5,6,],
    [7,8,9,],
]
for i in range(len(a)):
    for j in range(len(a[i])):
"""











