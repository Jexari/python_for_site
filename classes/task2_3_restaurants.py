#2. Три ресторана. Создайте три экземпляра класса,
#который вы написали для выполнения упражнения 9-1, и
#вызовите метод describe_restaurant () для каждого
#экземпляра.

#2. Three restaurants. Create three instances of the
#class you wrote for Exercise 9-1 and call the
#describe_restaurant() method on each instance.

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

restaurant_tokyo=Restaurant('tokyo', 'japanese')
restaurant_sakhalin=Restaurant('sakhalin', 'russian')
restaurant_777=Restaurant(777, 'european')
restaurant_tokyo.describe_restaurant()
print()
restaurant_sakhalin.describe_restaurant()
print()
restaurant_777.describe_restaurant()
