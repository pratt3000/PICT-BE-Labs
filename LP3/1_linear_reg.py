import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(rc = {'figure.figsize':(8,8)})

data = [
        (10, 95),
        (9, 80),
        (2, 10),
        (15, 50),
        (10, 45),
        (16, 98),
        (11, 38),
        (16, 93),
]

x = [pt[0] for pt in data]
y = [pt[1] for pt in data]

sns.scatterplot(x=x, y=y, s=100)

n = len(x)
xx = [a * a for a in x]
xy = [x[i] * y[i] for i in range(n)]

sum_x = np.sum(x)
sum_y = np.sum(y)
sum_xx = np.sum(xx)
sum_xy = np.sum(xy)

m = (n * sum_xy - sum_x * sum_y) / (n * sum_xx - sum_x * sum_x)

b = (sum_y - m * sum_x) / n

print(f'LINE EQUATION: y = {round(m,2)} * x + {round(b,2)}')

def plot_graph(x, y, slope, intercept):
    axes = sns.scatterplot(x=x, y=y, s=100)
    x_vals = np.array(axes.get_xlim())
    y_vals = intercept + slope * x_vals
    plt.plot(x_vals, y_vals, '-', color='red')

plot_graph(x, y, m, b)

