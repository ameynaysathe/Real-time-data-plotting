from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('fivethirtyeight')

x_vals = []
y_vals = []

index = count()

def animate(i):

    data = pd.read_csv('database.csv')
    x = data['Population']
    y = data['Time']
    y1 = data['Covid_Cases']

    plt.cla()

    plt.tight_layout()
    plt.xlabel("Population")
    plt.ylabel("Time In Seconds")
    plt.title("Real Time Data Plotting")
    plt.plot(x, y, label='Population')
    # plt.plot(x)
    # plt.plot(x, y, label='Population')
    plt.plot(y1, label='Covid Cases')
    plt.legend(loc='upper left')

ani = FuncAnimation(plt.gcf(), animate, interval=1000)

plt.tight_layout()
plt.show()