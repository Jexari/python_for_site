class Car():
    def __init__(self, make, model, year):
        self.make=make
        self.model=model
        self.year=year
        self.odometer_reading=0
    def update_odometer(self, new_odometer):
        self.odometer_reading=new_odometer
    def get_descriptive_name(self):
        long_name=str(self.year)+' '+self.make+' '+self.model
        return long_name
    def read_odometer(self):
        print('This car has '+str(self.odometer_reading)+' miles on it.')
class ElectricCar(Car):
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
my_tesla=ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive_name())
