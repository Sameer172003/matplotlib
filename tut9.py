# How do you Plot a Box and Whisker Plot?

import matplotlib.pyplot as plt

x=[10,20,30,40,50,60,70]

plt.boxplot(x,notch=True)

plt.boxplot(x,vert=False)

plt.boxplot(x,widths=0.6)

plt.boxplot(x,showmeans=True)

plt.boxplot(x,patch_artist=True)


y=[10,20,30,40,50,60,70,120]

plt.boxplot(y)

plt.boxplot(y,whis=3.5)


# Plot two boxplot in one frame

z=[x,y]

plt.boxplot(z,label=["Data_1","Data2"],whis=2)

plt.show()