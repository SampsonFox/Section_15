from random import randint


class Die():
    '''表示一个骰子的类'''

    def __init__(self, num_sides=6):
        '''默认骰子是6面'''
        self.num_side = num_sides

    def roll(self):
        '''返回一个随机数'''
        return randint(1, self.num_side)