#This is numerical estimate of pi based on Monte Carlo method using unit circle inscribed in rectangle.
#Outputs pi estimate in terminal and also plot based on number of random points inputed by user.
#This code based on previous version at https://gist.github.com/louismullie/3769218.

import random as r
import numpy as np
import matplotlib.pyplot as plt

# input total number of random points
total_random_points = int(input("\nNumber of random points for Monte Carlo estimate of Pi?\n>"))

# number of random points inside unit cicrle and total random points
inside_circle = 0

# create empty x and y arrays for eventual scatter plot of generated random points
x_plot_array = np.empty((0,total_random_points))
y_plot_array = np.empty((0,total_random_points))

# generate random points and count points inside unit circle
# top right quadrant of unit cicrle only
for i in range(0, total_random_points):
    # print(f'\nIteration: {i + 1}')
    # generate random x, y in range [0, 1]
    x = r.random()
    x_plot_array = np.append(x_plot_array, [x])
    #print(f'{x_plot_array}')
    # print(f'x value: {x}')
    y = r.random()
    y_plot_array = np.append(y_plot_array, [y])
    #print(f'{y_plot_array}')
    # print(f'y value: {y}')
    # calc x^2 and y^2 values
    x_squared = x**2
    y_squared = y**2
    # count if inside unit circle, top right quadrant only
    if np.sqrt(x_squared + y_squared) < 1.0:
        inside_circle += 1
    # print(f'Points inside circle {inside_circle}')
    # print(f'Number of random points {i+1}')
    # calc approximate pi value
    pi_approx = (float(inside_circle) / (i+1)) * 4
    # print(f'Approximate value for pi: {pi_approx}')

# final numeric output for pi estimate
print ("\n--------------")
print (f"\nApproximate value for pi: {pi_approx}")
print (f"Difference to exact value of pi: {pi_approx-np.pi}")
print (f"Percent Error: (approx-exact)/exact * 100: {(pi_approx-np.pi)/np.pi*100} %\n")

# plot output of random points and circle, top right quadrant only
random_points_plot = plt.scatter(x_plot_array, y_plot_array, color='blue', s=.1)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)

ax = plt.gca()
ax.cla()

ax.add_artist(random_points_plot)
ax.add_artist(circle_plot)

plt.show()
