import matplotlib.pyplot as plt
import numpy as np

# Sample data
categories = ['cadical-113B', 'cadical-134B', 'cadical-1227B','kissat-1802B']

# # L1D size varying
# data1 = [0.154601, 0.168512, 0.15586,0.299755]
# data2 = [0.154627, 0.16852, 0.155863, 0.299931]
# data3 = [0.154631, 0.16852, 0.155863, 0.299964]
# data4= [0.154629, 0.16852, 0.155861,0.299973]


# # L2 size varying
# data1 = [0.154591, 0.16852, 0.15584,0.299936]
# data2 = [0.154631, 0.16852, 0.155863, 0.299964]
# data3 = [0.154591, 0.16852, 0.15584, 0.299936]


# # LLC size varying
# data1 = [0.153488, 0.167936, 0.153698,0.297317]
# data2 = [0.153833, 0.167964, 0.154273, 0.297866]
# data3 = [0.154631, 0.16852, 0.155863, 0.299964]
# data4= [0.156791, 0.1701, 0.157458,0.303419]
# # data5= [0.159295, 0.175113, 0.160439, 0.307927]
# data5= [0.169081, 0.193178, 0.184256, 0.309718]


# # L1D size varying
# data1 = [0.154601, 0.168512, 0.15586,0.299755]
# data2 = [0.154627, 0.16852, 0.155863, 0.299931]
# data3 = [0.154631, 0.16852, 0.155863, 0.299964]
# data4= [0.154629, 0.16852, 0.155861,0.299973]




# Setting up the bar chart
bar_width = 0.15
x = np.arange(len(categories))

# Plotting the bars
fig, ax = plt.subplots()
rects1 = ax.bar(x -2*bar_width, data1, bar_width, label='16x512')
rects2 = ax.bar(x-bar_width, data2, bar_width, label='16x1024')
rects3 = ax.bar(x, data3, bar_width, label='16x2048')
rects4 = ax.bar(x + bar_width, data4, bar_width, label='16x4096')
rects5 = ax.bar(x + 2*bar_width, data5, bar_width, label='16x32768')

# Adding labels, title and ticks to the chart
ax.set_yscale('log')
ax.set_xlabel('Traces')
ax.set_ylabel('IPC')
ax.set_title('Multi Bar Histogram')
ax.set_xticks(x)
ax.set_xticklabels(categories)
ax.legend()

# Show the plot
plt.show()
