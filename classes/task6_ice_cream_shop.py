#6 Магазин мороженого: Магазин мороженого - это особый
#вид ресторана. Напишите класс IceCreamStand и
#позвольте ему наследовать класс Restaurant, который
#вы написали для выполнения упражнения 1. Добавьте
#атрибут, называемый ароматизаторами, для хранения
#списка мороженого с различными вкусами. Напишите
#способ отображения этого мороженого. Создайте
#экземпляр IceCreamStand и вызовите этот метод.

#6 Ice Cream Shop: An ice cream shop is a special type
#of restaurant. Write an IceCreamStand class and let
#it inherit from the Restaurant class you wrote for
#exercise 1. Add an attribute called flavors to store a list
#of ice cream flavors. Write a way to display this ice
#cream. Instantiate IceCreamStand and call this method.

class Restaurant():
    def __init__(self, restaurant_name, kitchen_type):
        self.restaurant_name=restaurant_name
        self.kitchen_type=kitchen_type
    def describe_restaurant(self):
        print('RU: Приветствуем Вас в ресторане '+str(self.restaurant_name)+'!')
        print('EN: Welcome to the restaurant '+str(self.restaurant_name)+'!')
        print('Here you can taste', self.kitchen_type, 'kitchen.')
    def open_restaurant(self):
        print("\nRU: Ресторан", self.restaurant_name,"открыт.")
        print('EN: The restaurant',self.restaurant_name,'is open.')

class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, kitchen_type, flavors):
        super().__init__(restaurant_name, kitchen_type)
        self.flavors=flavors
    def flavors_print(self):
        print('\nIn our restautant we have this flavours:', end=' ')
        print(*self.flavors, sep=', ')
my_stand=IceCreamStand('Ice cream from the Himalayas', 'ice cream', ['chocolate', 'strawberry', 'cherry'])
my_stand.describe_restaurant()
my_stand.open_restaurant()
my_stand.flavors_print()
