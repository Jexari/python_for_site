'''9 Обновление батареи: В последней версии
electric_car.py в этом разделе добавьте метод с именем
upgrade_battery () к классу Battery. Этим методом
проверяется емкость батареи, если она не 85,
установите на 85. Создайте электромобиль с
аккумулятором по умолчанию, вызовите метод get_range(),
затем обновите аккумулятор и снова вызовите get_range().
Вы увидите, что запас хода машины увеличился.'''

'''9 Battery Upgrade: In the latest version of
electric_car.py, in this section, add a method called
upgrade_battery() to the Battery class. This method
checks the battery capacity, if it's not 85, set it
to 85. Create an EV with the default battery, call the
get_range() method, then update the battery and call
get_range() again. You will see that the range of the
machine has increased.'''

class Car():
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year
    def get_descriptive_name(self):
        long_name = str(self.year) + ' ' + self.make + ' ' + self.model
        return long_name.title()

class Battery():
    def __init__(self,battery_size=70):
        self.battery_size = battery_size
    def descriptive_battery(self):
        print("This car has a " + str(self.battery_size) + "-kwh battery.")
    def get_range(self):
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately " + str(range)
        message += " miles on a full charge."
        print(message) 
    def upgrade_battery(self):
        if self.battery_size != 85:
            self.battery_size = 85

class ElectricCar(Car):
    def __init__(self,make,model,year):
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla','model s',2016)
my_tesla.battery.get_range()
my_tesla.battery.upgrade_battery()
my_tesla.battery.get_range()
