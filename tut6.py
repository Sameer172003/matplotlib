# How to Plot HISTOGRAM CHART IN MATPLOTLIB

import matplotlib.pyplot as plt
import random

x=[]
size=50

for i in range(1,size):
    x.append(random.randint(10,100))

print(x)

plt.title("Histogram Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.hist(x,color='b',edgecolor='k')

plt.hist(x,"auto",(0,200),edgecolor='k',cumulative=-1)

plt.hist(x,edgecolor='k',histtype="step")

plt.hist(x,edgecolor='k',orientation="horizontal")

plt.hist(x,edgecolor='k',rwidth=0.8)

plt.grid()
plt.show()