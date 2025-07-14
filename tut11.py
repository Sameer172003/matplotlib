# How to Create Step Plot in Python Matplotlib?

import matplotlib.pyplot as plt
import random

x=[1,2,3,4,5]
y=[1,2,3,4,5]

# for i in range(1,6):
#     x.append(random.randint(1,5))

# for i in range(1,6):
#     y.append(random.randint(5,10))

# print(x)
# print(y)

plt.title("Step Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.step(x,y,marker="o",color="r",mfc="g")

plt.grid()
plt.show()

