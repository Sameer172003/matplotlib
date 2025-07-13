# How to Create a Scatterplot in Python Matplotlib?

import matplotlib.pyplot as plt

x=[1,2,3,4,5,6,7]
y=[3,2,5,4,6,1,8]

c=['r','b','g','m','y','c','k']
size=[10,20,30,40,50,60,70]
colors=[18,21,34,26,32,43,29]

plt.title("Scatter Plot")
plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")

# plt.scatter(x,y,color=c,s=size,alpha=0.7,marker="D",edgecolors='g',linewidths=1)

plt.scatter(x,y,c=colors,cmap="viridis")
plt.colorbar()

# plt.scatter(x,y,color='c')
plt.show()