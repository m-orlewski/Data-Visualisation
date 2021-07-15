import matplotlib.pyplot as plt
from random_walk import RandomWalk

rw = RandomWalk(50_000)
rw.fill_walk()

plt.style.use('classic')
fig, ax = plt.subplots(figsize=(15,9), dpi=128)

point_numbers = range(len(rw.x))

ax.scatter(rw.x, rw.y, s=5, c=point_numbers, cmap=plt.cm.magma, edgecolors='none')

ax.scatter(0, 0, s=25, c='green', edgecolors='none')
ax.scatter(rw.x[-1], rw.y[-1], s=25, c='green', edgecolors='none')

ax.get_xaxis().set_visible(False)
ax.get_yaxis().set_visible(False)

plt.show()