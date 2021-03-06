from random import choice

class Randomwalk():
    '''generate a random walk class'''

    def __init__(self, num_points=5000):
        '''inicialize settings of random walk'''
        self.num_points = num_points

        #start from (0,0)
        self.x_value = [0]
        self.y_value = [0]

    def fill_walk(self):
        '''calculate all points'''
        '''do random walk untill reach the top point'''

        while len(self.x_value) < self.num_points:

            #decide orintation and step
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #no staying
            if x_step == 0 and y_step == 0:
                continue

            #calculate next point
            next_x = self.x_value[-1] + x_step
            next_y = self.y_value[-1] + y_step

            self.x_value.append(next_x)
            self.y_value.append(next_y)


walk = Randomwalk()
walk.fill_walk()