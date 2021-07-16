import matplotlib.pyplot as plt

x_values = range(1, 5001)
cubes = [x**3 for x in x_values]

fig, ax = plt.subplots()

# scattered points plot
ax.scatter(x_values, cubes, c=cubes, cmap=plt.cm.magma, s=3)

plt.show()