import numpy as np
import matplotlib.pyplot as plt

'''intitial condition'''
y_initial = 3

def get_dy_dt(current_y_value):
    return 1.01 - current_y_value - (0.01 * (current_y_value**4))

num_of_intervals = 11
time = np.linspace(0, 2, num=num_of_intervals)
time_interval = time[1] - time[0]
y_value = np.zeros(num_of_intervals)


y_value[0] = y_initial

for i in range (1, num_of_intervals):
    y_value[i] = y_value[i-1] + (get_dy_dt(y_value[i-1]) * time_interval)


print(y_value[10])
plt.plot(time, y_value)
plt.show()