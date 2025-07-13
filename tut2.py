#  How to Plot a Line Chart in Python

import matplotlib.pyplot as plt

# Bar Plot

x=["Python","C","C++","Java"]
y=[88,75,68,83]
plt.title("Languages VS Popularity")
plt.xlabel("Languages")
plt.ylabel("Popularity")
c=["y","b","g","m"]
plt.bar(x,y,width=0.4,color=c,edgecolor='r',linewidth=3,linestyle=":",alpha=0.6,label="popularity")
plt.legend()
plt.show()