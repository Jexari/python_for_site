'''Ресторан: создайте класс с именем Restaurant,
и его метод __init __ () устанавливает два атрибута:
restaurant_name и kitchen_type. Создайте метод с
именем describe_restaurant () и метод с именем
open_restaurant (), где первый печатает два
вышеупомянутых элемента информации, а второй печатает
сообщение о том, что ресторан открыт.

Создайте экземпляр с именем restaurant на основе этого
класса, распечатайте два его атрибута соответственно,
а затем вызовите два вышеупомянутых метода.'''

'''Restaurant: Create a class named Restaurant and
its __init__() method sets two attributes:
restaurant_name and kitchen_type. Create a method
named describe_restaurant() and a method named
open_restaurant() where the first prints the above two
pieces of information and the second prints a message
that the restaurant is open.

Create an instance named restaurant based on this
class, print out its two attributes respectively, and
then call the above two methods.'''

class Restaurant():
    def __init__(self, restaurant_name, kitchen_type):
        self.restaurant_name=restaurant_name
        self.kitchen_type=kitchen_type        
    def describe_restaurant(self):
        print('RU: Приветствуем Вас в ресторане '+str(self.restaurant_name).title()+'!')
        print('EN: Welcome to the restaurant '+str(self.restaurant_name).title()+'!')
        print('Here you can taste', self.kitchen_type, 'kitchen.')
    def open_restaurant(self):
        print("RU: Ресторан", self.restaurant_name,"открыт.")
        print('EN: The restaurant',self.restaurant_name,'is open.')



restaurant=Restaurant('Tokyo', 'japanese')
restaurant.describe_restaurant()
restaurant.open_restaurant()
