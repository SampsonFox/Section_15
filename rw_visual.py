import matplotlib.pyplot as plt

from randomwalk import Randomwalk

rw = Randomwalk()
rw.fill_walk()
plt.scatter(rw.x_value, rw.y_value,s=5)
plt.show()