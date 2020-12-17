import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm

def f(x,y): return (1-x/2+x**5+y**3)*np.exp(-x**2-y**2)

left  = 0.1  # the left side of the subplots of the figure
right = 0.9    # the right side of the subplots of the figure
bottom = 0.1   # the bottom of the subplots of the figure
top = 0.9      # the top of the subplots of the figure
wspace = 0.4   # the amount of width reserved for blank space between subplots
hspace = 0.4   # the amount of height reserved for white space between subplots


fig, axes = plt.subplots(nrows=2, ncols=2,figsize=(8, 8), dpi=100)
plt.subplots_adjust(left=left, bottom=bottom, right=right, top=top, wspace=wspace, hspace=hspace)

# Subplot 0, 0
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

axes[0,0].set_title('Histogram of IQ')
axes[0,0].set_xlabel('Smarts')
axes[0,0].set_ylabel('Probability')

# the histogram of the data
n, bins, patches = axes[0,0].hist(x, 50, density=1, facecolor='g', alpha=0.75)

axes[0,0].grid(True)
axes[0,0].text(60, .025, r'$\mu=100,\ \sigma=15$')

axes[0,0].axis([40, 160, 0, 0.03])

# Subplot 0, 1
n = 256
x = np.linspace(-3,3,n)
y = np.linspace(-3,3,n)
X,Y = np.meshgrid(x,y)

axes[0,1].contourf(X, Y, f(X,Y), 8, alpha=.75, cmap='jet')
C = axes[0,1].contour(X, Y, f(X,Y), 8, colors='black')
axes[0,1].set_title("Contour Plot")

# Subplot 1, 0
# Pie chart, where the slices will be ordered and plotted counter-clockwise:
labels = 'Frogs', 'Hogs', 'Dogs', 'Logs'
sizes = [15, 30, 45, 10]
explode = (0, 0.1, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')


axes[1,0].pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
axes[1,0].axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

# Subplot 1, 1
labels = ['T1', 'T2', 'T3', 'T4', 'T5']
gpu = [20, 34, 30, 35, 27]
cpu = [25, 32, 34, 20, 25]

x = np.arange(len(labels))  # the label locations
width = 0.35  # the width of the bars

rects1 = axes[1,1].bar(x - width/2, gpu, width, label='GPU')
rects2 = axes[1,1].bar(x + width/2, cpu, width, label='CPU')

# Add some text for labels, title and custom x-axis tick labels, etc.
axes[1,1].set_ylabel('Time[ms]')
axes[1,1].set_title('Time Comparision GPU/CPU')
axes[1,1].set_xticks(x)
axes[1,1].set_xticklabels(labels)
axes[1,1].legend()

plt.show()