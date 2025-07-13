# Stem Plots with Matplotlib

import matplotlib.pyplot as plt
import random

x=[]
y=[]

for i in range(0,7):
    x.append(random.randint(-4,10))

print(x)

for i in range(0,7):
    y.append(random.randint(-4,10))

print(y)


plt.stem(x,y,linefmt=":",markerfmt="ro")
plt.show()
