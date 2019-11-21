"""电动汽车的类"""

from car import Car

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