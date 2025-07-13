# How to Create a Pie Chart in Python Matplotlib?

import matplotlib.pyplot as plt

x=[10,20,30,40]
y=["C","C++","Python","Java"]
ex=[0.3,0.0,0.0,0.0]
c=['y','r','b','g']

plt.pie(x,labels=y,explode=ex,autopct="%0.1f%%",colors=c,radius=0.7,shadow=True)

plt.title("Pie Chart")
plt.legend()
plt.show()