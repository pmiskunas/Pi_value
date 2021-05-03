import pandas as pd
import random
import time
import matplotlib.pyplot as plt


num_point_circle = 0
num_point_total = 0
xx, yy, dd = [], [], []
start_time = time.time()  # we start counting time how long the program compiles
n = int(input('how many dots: '))
for a in range(n):  # getting random coordinates and calculating distance from (0;0)
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    distance = abs(x)**2 + abs(y)**2
    xx.append(x)
    yy.append(y)
    if distance <= 1:
        dd.append('in a circle')
    else:
        dd.append('out of circle')
    if distance <= 1:
        num_point_circle += 1
    num_point_total += 1
pi = 4 * num_point_circle / num_point_total  # pi value=points in a circle(when distance < 1) divided by total points.
print("--- %s seconds to calculate value of \u03C0 ---" % round((time.time() - start_time), 4))
print(f'--- calculated value of \u03C0 is {pi} ---')

# making dataframes for plotting (it could not be the best way):
points = {'x': xx, 'y': yy, 'distance': dd}
df = pd.DataFrame(points)
in_c = df.loc[df['distance'] == 'in a circle']
out_c = df.loc[df['distance'] == 'out of circle']

# changing marker size according to number of dots:
if n <= 1000:
    s = 30
elif 1000 < n <= 10000:
    s = 10
else:
    s = 1

# graph with pandas, matplotlib:
plt.style.use("seaborn")
dots = in_c.plot(kind='scatter', x='x', y='y', c='#306998', s=s)
out_c.plot(kind='scatter', x='x', y='y', c='#ffd43b', s=s, ax=dots)
dots.set_aspect(aspect=1)  # setting the aspect ration 1:1 (square graph)
dots.set_title(f'Calculated \u03C0 value is {pi} \nusing {n} random coordinates from -1 to 1')
plt.show()
