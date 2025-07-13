# How to make more than two bar graph in one

import matplotlib.pyplot as plt
import numpy as np

x=["Python","C","C++","Java"]
y=[88,78,65,82]
z=[45,37,41,47]

width=0.2

p=np.arange(len(x))
p1=[j+width for j in p]


plt.title("Popularity")
plt.xlabel("Languages")
plt.ylabel("Number of Users")


plt.bar(p,y,width,color='r',label="Popularity_1")
plt.bar(p1,z,width,color='y',label="Popularity_2")

# If we want a horizontal bar graph

# plt.barh(p,y,width,color='r',label="Popularity_1")
# plt.barh(p1,z,width,color='y',label="Popularity_2")

plt.xticks(p+width/2,x,rotation=15)

plt.legend()
plt.show()