# How do you Plot Stack and Area Plot 

import matplotlib.pyplot as plt
import random

x=[1,2,3,4,5]
a1=[]
a2=[]
a3=[]
l=["area1","area2","area3"]

for i in range(1,6):
    a1.append(random.randint(1,10))

for i in range(1,6):
    a2.append(random.randint(1,10))

for i in range(1,6):
    a3.append(random.randint(1,10))

print(a1)
print(a2)
print(a3)

plt.title("Stack Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

plt.stackplot(x,a1,a2,a3,labels=l)

plt.legend()
plt.show()
