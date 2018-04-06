#This is numerical estimate of pi based on Monte Carlo method using unit circle inscribed in rectangle.
#Outputs pi estimate in terminal and also plot based on number of random points inputed by user.
#This code based on previous version at https://gist.github.com/louismullie/3769218.

import numpy as np
import matplotlib.pyplot as plt
import time as time

# input total number of random points
total_random = int(input("\nNumber of random points for Monte Carlo estimate of Pi?\n>"))

# start time of calculation
start_time = time.time()

# create x and y arrays with random generated numbers between 0 and 1 across input range.
x_array = np.random.rand(1,total_random)
y_array = np.random.rand(1,total_random)

# create array with radius values based on x and y random generated numbers
radius_array = np.sqrt(x_array**2 + y_array**2)

# boolean test for number of radius values less than one
inside_circle = np.sum(radius_array < 1.0)

# calc approximate value of pi
pi_approx = (inside_circle / total_random) * 4

# final numeric output for pi estimate
print ("\n--------------")
print (f"\nApproximate value for pi: {pi_approx}")
print (f"Difference to exact value of pi: {pi_approx - np.pi}")
print (f"Percent Error: (approx-exact)/exact*100: {(pi_approx - np.pi) / np.pi * 100}%")
print (f"Execution Time: {time.time() - start_time} seconds\n")

# plot output of random points and circle, top right quadrant only
random_points_plot = plt.scatter(x_array, y_array, color='blue', s=.1)
circle_plot = plt.Circle( ( 0, 0 ), 1, color='red', linewidth=2, fill=False)

ax = plt.gca()
ax.cla()

ax.add_artist(random_points_plot)
ax.add_artist(circle_plot)

plt.show()