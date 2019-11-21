from random import randint

class Die():
    """一个骰子的类"""

    def __init__(self,num_sides=6):
        """骰子为6面"""
        self.num_sides = num_sides

    def roll(self):
        """返回随机数1-6"""
        return randint(1,self.num_sides)