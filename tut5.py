# How to make more than two scatter graph in one

import matplotlib.pyplot as plt
import random

x=[]
y=[]
z=[]
colors=[]

size=10

for i in range(0,size):
    x.append(random.randint(1,11))

for i in range(0,size):
    y.append(random.randint(1,11))

for i in range(0,size):
    z.append(random.randint(1,11))

for i in range(0,size):
    colors.append(random.randint(20,50))

print(x)
print()
print(y)
print()
print(z)
print()
print(colors)
print()


plt.title("Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.scatter(x,y,c=colors,cmap='viridis',label='DATA_1')
plt.scatter(x,z,c=colors,cmap='viridis',label='DATA_2')

plt.legend()
plt.colorbar()
plt.show()
