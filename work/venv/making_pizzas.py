class Car():
    """汽车类"""

    def __init__(self,make,model,year):
        """初始化"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """描述性信息"""
        long_name = str(self.year)+" "+self.make+" "+self.model
        return long_name.title()

    def  read_odometer(self):
        """汽车里程"""
        print("This car has "+str(self.odometer_reading)+" miles on it.")

    def update_odometer(self,mileage):
        """指定里程数"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self,miles):
        """增加指定量里程"""
        if miles >= 0:
            self.odometer_reading += miles
        else:
            print("Increments are forbidden to be negative!")

class Battery():
    """动力电池"""

    def __init__(self,battery_size=70):
        """初始化属性"""
        self.battery_size = battery_size

    def describe_battery(self):
        """描述电池"""
        print("This car has a "+str(self.battery_size)+"-kWh battery.")

    def get_range(self):
        """续驶里程"""
        if self.battery_size == 70:
            range = 240
        elif self.battery_size == 85:
            range = 270
        message = "This car can go approximately "+str(range)
        message += " miles on a full charge."
        print(message)

class ElectricCar(Car):
    """电动汽车独特"""

    def __init__(self,make,model,year):
        """初始化父类的属性"""
        super().__init__(make,model,year)
        self.battery = Battery()

my_tesla = ElectricCar('tesla',"model s",2016)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

