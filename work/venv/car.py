"""表示汽车的类"""


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
        """增加增量里程"""
        self.odometer_reading += miles


